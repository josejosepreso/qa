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

class CreditCardPayment:
	@History.register_transaction(TransactionType.CREDIT_CARD_PAYMENT)
	@staticmethod
	def third_party(
			credit_card_number: str = Configuration.THIRD_PARTY_CREDIT_CARD_NUMBER,
			amount: int = Configuration.DEFAULT_AMOUNT,
			currency: Currency = Currency.LPS,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_CREDIT_CARD_PAYMENT_HOMESCREEN)

		Action.click(Selector.BTN_OTHER_CREDIT_CARD)

		if origin_account_number is not None:
			Action.change_origin_account(origin_account)

		Action.type(Selector.INPUT_CREDIT_CARD_NUMBER, credit_card_number)

		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_CREDIT_CARD_NUMBER)).click()

		if currency != Currency.LPS:
			Action.click(Selector.BTN_SELECT_USD_CURRENCY_THIRD_PARTY_CREDIT_CARD_PAYMENT)

		#
		Action.type(Selector.INPUT_THIRD_PARTY_CREDIT_CARD_PAYMENT_AMOUNT, amount)
		Action.click(Selector.BTN_DO_THIRD_PARTY_CREDIT_CARD_PAYMENT)
		Action.click(Selector.BTN_CONFIRM_AMOUNT_CREDIT_CARD_PAYMENT)

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

	@History.register_transaction(TransactionType.CREDIT_CARD_PAYMENT)
	@staticmethod
	def own(
			credit_card_number: str = None,
			amount: int = Configuration.DEFAULT_AMOUNT,
			currency: Currency = Currency.LPS,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_CREDIT_CARD_PAYMENT_HOMESCREEN)

		credit_card = Action.get_element(*Selector.get_own_credit_card(1))

		if credit_card_number is not None:
			# TODO
			idx = 1

			while True:
				pass

		credit_card.click()

		if origin_account_number is not None:
			Action.change_origin_account(origin_account)

		if currency == Currency.LPS:
			Action.click(Selector.BTN_SELECT_LPS_CURRENCY)
		elif currency == Currency.USD:
			Action.click(Selector.BTN_SELECT_USD_CURRENCY)
		else:
			raise Exception

		Action.click(Selector.BTN_CREDIT_CARD_CUSTOM_AMOUNT_PAYMENT)
		#
		Action.type(Selector.INPUT_CREDIT_CARD_PAYMENT_AMOUNT, amount)
		Action.click(Selector.BTN_DO_CREDIT_CARD_PAYMENT)
		Action.click(Selector.BTN_CONFIRM_AMOUNT_CREDIT_CARD_PAYMENT)
		
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.APP_VOUCHER))
		
		Action.click(Selector.BTN_DOWNLOAD_VOUCHER)
		
		download_voucher_response = Action.get_response_body(Configuration.DOWNLOAD_VOUCHER_SERVICE_URL_PATTERN, True)
		
		Action.click(Selector.LINK_HOME_SCREEN)
		
		time.sleep(1)

	@History.register_transaction(TransactionType.CREDIT_CARD_PAYMENT)
	@staticmethod
	def ach(
			credit_card_number: str = Configuration.ACH_CREDIT_CARD_NUMBER,
			credit_card_bank: ACH = Configuration.ACH_CREDIT_CARD_BANK,
			amount: int = Configuration.DEFAULT_AMOUNT,
			currency: Currency = Currency.LPS,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_CREDIT_CARD_PAYMENT_HOMESCREEN)

		Action.click(Selector.BTN_OTHER_CREDIT_CARD)

		if origin_account_number is not None:
			Action.change_origin_account(origin_account)

		Action.select_ach(credit_card_bank)

		Action.type(Selector.INPUT_CREDIT_CARD_NUMBER, credit_card_number)
		"""
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_CREDIT_CARD_NUMBER)).click()

		if currency != Currency.LPS:
			Action.click(Selector.BTN_SELECT_USD_CURRENCY_THIRD_PARTY_CREDIT_CARD_PAYMENT)

		#
		Action.type(Selector.INPUT_CREDIT_CARD_PAYMENT_AMOUNT, amount)
		Action.click(Selector.BTN_DO_CREDIT_CARD_PAYMENT)
		Action.click(Selector.BTN_CONFIRM_AMOUNT_CREDIT_CARD_PAYMENT)

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
		"""
