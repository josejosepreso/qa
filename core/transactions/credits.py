from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from core.driver_common import get_driver
from config.const import Configuration
from core.elements_selectors import Selector
from core.actions import Action
from config.enums import *
from utils.history import History

driver = get_driver()

class CreditPayment:
	@History.register_transaction(TransactionType.CREDIT_PAYMENT)
	@staticmethod
	def own(credit_number: str):
		Action.click(Selector.BTN_CREDIT_PAYMENT_HOMESCREEN)
		pass

	@History.register_transaction(TransactionType.CREDIT_PAYMENT)
	@Action.navigate(TransactionType.CREDIT_PAYMENT)
	@staticmethod
	def third_party(
			credit_number: str = Configuration.THIRD_PARTY_CREDIT_NUMBER,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_OTHER_CREDIT)

		if origin_account_number is not None:
			Action.change_origin_account(origin_account_number)

		Action.type(Selector.INPUT_THIRD_PARTY_CREDIT_NUMBER, credit_number)

		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_THIRD_PARTY_CREDIT_NUMBER)).click()

		Action.click(Selector.BTN_DO_THIRD_PARTY_CREDIT_PAYMENT)
		Action.click(Selector.BTN_CONFIRM_AMOUNT_THIRD_PARTY_CREDIT_PAYMENT)

		#
		Action.type(Selector.INPUT_FIRST_OTP_DIGIT_MODAL, Action.get_OTP())
		
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_OTP_MODAL)).click()
		
		#
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.APP_VOUCHER))
		
		Action.click(Selector.BTN_DOWNLOAD_VOUCHER)
		
		download_voucher_response = Action.get_response_body(Configuration.DOWNLOAD_VOUCHER_SERVICE_URL_PATTERN, True)
		
		#
		Action.click(Selector.LINK_HOME_SCREEN)
		
		time.sleep(1)
