from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re
import json

from core.driver_common import get_driver
from config.const import Configuration
from utils.database import DBRequest
from core.elements_selectors import Selector
from core.exceptions import TimeoutException
import config.user as user
from config.enums import ACH, TransactionType

driver = get_driver()

class Action:
	@staticmethod
	def get_element(selector_type, selector_str: str):
		element = []
		retries = 0

		while not element:
			if retries > Configuration.RETRIES_LIMIT:
				raise TimeoutException(f"Timeout getting element { selector_str } by { selector_type }")
			
			element = driver.find_elements(selector_type, selector_str)
			retries += 1

			time.sleep(1)
			
		assert len(element) == 1
		
		return element[0]

	@staticmethod
	def click(selector):
		Action.get_element(*selector).click()

	@staticmethod
	def type(selector, user_input: str):
		Action.get_element(*selector).send_keys(user_input)

	@staticmethod
	def get_OTP():
		otp = DBRequest.get_most_recent_OTP(user.USER_DNI)
		
		with open(Configuration.OTPS_FILE, "r") as f:
			for line in f:
				digits, hashed = line.strip().split(",")
				
				if hashed == otp:
					return digits
					
		raise Exception
		
	@staticmethod
	def get_response_body(url: str, regex = False):
		retries = 0
		
		while True:
			if retries > Configuration.RETRIES_LIMIT:
				raise TimeoutException(f"Timeout expecting response from { url }")
			
			time.sleep(1)
			
			def exact_match(req):
				return url == req.url
			def regex_match(req):
				pattern = url
				return re.match(pattern, req.url)
				
			cond = regex_match if regex else exact_match
			
			auth_requests = list(filter(cond, driver.requests))
			
			for req in auth_requests:
				if req.response:
					res = req.response
					
					if res.status_code != 200:
						raise Exception
					
					return json.loads(res.body)
					
			retries += 1

	@staticmethod
	def navigate(transaction_type: TransactionType):
		def decorator(transaction):
			def wrapper( *args, **kwargs ):
				if driver.current_url != Configuration.BANCA_DIGITAL_HOME_URL:
					driver.get(Configuration.BANCA_DIGITAL_HOME_URL)

				driver.find_element(*Selector.HOMESCREEN_BTN_BG_BLUE_00).click()

				WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.CONTAINER_TRANSACTION_OPTIONS))
				labels = {
						TransactionType.TRANSFER: "Transferir",
						TransactionType.CREDIT_CARD_PAYMENT: "Pagar Tarjeta de Crédito",
						TransactionType.CREDIT_PAYMENT: "Pagar Préstamo"
				}

				label = labels.get(transaction_type)
				if not label:
					raise Exception

				transaction_options = list(filter(lambda l: l.text.strip() == label, driver.find_elements(*Selector.P_TRANSACTION_OPTION_LABEL)))
				if not transaction_options:
					raise Exception

				assert len(transaction_options) == 1

				transaction_options[0].click()

				return transaction(*args, **kwargs)
			return wrapper
		return decorator

	@staticmethod		
	def login():
		driver.get(Configuration.BANCA_DIGITAL_LOGIN_URL)
		
		#
		input_username = Action.get_element(*Selector.INPUT_USERNAME_LOGIN)
		input_password = Action.get_element(*Selector.INPUT_USERNAME_PASSWORD)

		#
		input_username.clear()
		input_password.clear()
		
		input_username.send_keys(user.USERNAME)
		input_password.send_keys(user.USER_PASSWORD)
		time.sleep(0.5)
        #
		Action.click(Selector.BTN_LOGIN)
		
		#
		response = Action.get_response_body(Configuration.AUTH_SERVICE_URL).get("data", {})
		
		session_id = response.get("sessionId")
			
		#
		if response.get("duplicateSession", {}).get("active", False):
			Action.click(Selector.BTN_DISMISS_DUPLICATE_SESSION)
		
		#
		if response.get("daysRemaining") == 0:
			Action.click(Selector.BTN_CHANGE_PASSWORD)
			Action.click(Selector.LINK_HOME_SCREEN)
			
		#
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.HOMESCREEN_SIDEBAR_MENU_OPTIONS))

	@staticmethod
	def select_destination_account(destination_account_number: str):
		retries = 0
		own_accounts = []
		while not own_accounts:
			if retries > Configuration.RETRIES_LIMIT:
				driver.execute_script('alert("Usuario no tiene cuentas propias")')
				raise Exception

			if re.match("\\d+", driver.find_element(*Selector.P_OWN_ACCOUNT_NUMBER).text):
				own_accounts = driver.find_elements(*Selector.P_OWN_ACCOUNT_NUMBER)

			retries += 1
			time.sleep(1)

		if destination_account_number is None:
			own_accounts[0].click()
			return

		# TODO

	@staticmethod
	def select_origin_account(origin_account_number: str):
		Action.click(Selector.DIV_ADD_ORIGIN_ACCOUNT)

		if origin_account_number is None:
			Action.click(Selector.BTN_SELECT_ORIGIN_FIRST_OWN_ACCOUNT)

	@staticmethod
	def change_origin_account(origin_account_number: str):
		if origin_account_number is None:
			raise Exception

		if Action.get_element(*Selector.P_SELECTED_ORIGIN_ACCOUNT_NUMBER).text.strip() == origin_account_number:
			return

		Action.click(Selector.BTN_CHANGE_ORIGIN_ACCOUNT_NUMBER)

		idx = 3

		while True:
			try:
				if Action.get_element(*Selector.get_p_origin_account_number(idx)).text.strip() == origin_account_number:
					Action.click(Selector.get_button_select_origin_account(idx))
					return
			except Exception:
				driver.execute_script('alert("Cuenta origen no encontrada")')
				raise

			idx += 1

	@staticmethod
	def select_ach(ach: ACH):
		shift = ach.value - 1

		if shift <= 0:
			return

		ach_swiper = Action.get_element(*Selector.ACH_BANK_SWIPER)
		#
		ach_swiper_options = ach_swiper.find_elements(*Selector.ACH_SWIPER_SLIDE)
		ach_swiper_next = ach_swiper.shadow_root.find_element(*Selector.BTN_SWIPER_NEXT_ACH_BANK)

		for _ in range(shift):
			ach_swiper_next.click()

		ach_swiper_slide = ach_swiper_options[ ach.value ]
		ach_swiper_slide.click()
