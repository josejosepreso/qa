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

class Transfer:
	@History.register_transaction(TransactionType.TRANSFER)
	@staticmethod
	def third_party(
			destination_account,
			amount = Configuration.DEFAULT_AMOUNT,
			origin_account = None
	):
		Action.click(Selector.BTN_TRANSFER_HOMESCREEN)

		#
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.BTN_TRANSFER_OTHER_ACCOUNT)).click()
		
		#
		if origin_account is not None:
			Action.change_origin_account(origin_account)
		
		Action.type(Selector.INPUT_ACCOUNT_NUMBER, destination_account)

		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_ACCOUNT_NUMBER)).click()
		
		Action.type(Selector.INPUT_TRANSFER_AMOUNT, amount)
		
		# btn_confirm_amount = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Selector.BTN_CONFIRM_TRANSFER_AMOUNT)))
		# time.sleep(0.5)
		# btn_confirm_amount.click()
		
		Action.click(Selector.BTN_CONFIRM_TRANSFER_AMOUNT)
		Action.click(Selector.BTN_CONFIRM_TRANSFER_AMOUNT_MODAL)
		Action.type(Selector.INPUT_FIRST_OTP_DIGIT_MODAL, Action.get_OTP())
		
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_OTP_MODAL)).click()
		
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.APP_VOUCHER))
		
		Action.click(Selector.BTN_DOWNLOAD_VOUCHER)
		
		download_voucher_response = Action.get_response_body(Configuration.DOWNLOAD_VOUCHER_SERVICE_URL_PATTERN, True)
		
		Action.click(Selector.LINK_HOME_SCREEN)
		
		time.sleep(1)
		
	@History.register_transaction(TransactionType.TRANSFER)
	@staticmethod
	def own_account(
			destination_account_number = None,
			amount = Configuration.DEFAULT_AMOUNT,
			origin_account_number = None
	):
		Action.click(Selector.BTN_TRANSFER_HOMESCREEN)

		Action.click(Selector.CHECKBOX_DESTINATION_ACCOUNT_TYPE)
		
		Action.select_destination_account(destination_account_number)

		Action.select_origin_account(origin_account_number)
		
		Action.type(Selector.INPUT_TRANSFER_AMOUNT, amount)
		Action.click(Selector.BTN_DO_TANSFER)
		Action.click(Selector.BTN_CONFIRM_TRANSFER_AMOUNT_MODAL)
		
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.APP_VOUCHER))
		
		Action.click(Selector.BTN_DOWNLOAD_VOUCHER)
		
		download_voucher_response = Action.get_response_body(Configuration.DOWNLOAD_VOUCHER_SERVICE_URL_PATTERN, True)
		
		Action.click(Selector.LINK_HOME_SCREEN)
		
		time.sleep(1)

	@History.register_transaction(TransactionType.TRANSFER)
	@staticmethod
	def ach(
			destination_account_number = Configuration.ACH_ACCOUNT_NUMBER,
			destination_account_bank: ACH = Configuration.ACH_ACCOUNT_BANK,
			destination_account_type: AccountType = Configuration.ACH_ACCOUNT_TYPE,
			amount: int = Configuration.DEFAULT_AMOUNT,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_TRANSFER_HOMESCREEN)

		#
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.visibility_of_element_located(Selector.BTN_TRANSFER_OTHER_ACCOUNT)).click()

		#
		Action.select_ach(destination_account_bank)

		#
		Action.type(Selector.INPUT_ACCOUNT_NUMBER, destination_account_number)

		if destination_account_type != AccountType.SAVINGS:
			Action.click(Selector.BTN_SELECT_CHECK_ACCOUNT_TYPE)

		#
		ach_client_document_type = Configuration.ACH_CLIENT_DOCUMENT_TYPE
		if ach_client_document_type != DocumentType.IDENTITY_NUMBER:
			# TODO
			pass

		Action.type(Selector.INPUT_ACH_CLIENT_NAME, Configuration.ACH_CLIENT_NAME)
		Action.type(Selector.INPUT_ACH_CLIENT_ID_NUMBER, Configuration.ACH_CLIENT_IDENTITY_NUMBER)

		#
		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_DESTINATION_ACCOUNT_NUMBER)).click()

		#
		Action.type(Selector.INPUT_TRANSFER_AMOUNT, amount)
		Action.click(Selector.BTN_CONFIRM_TRANSFER_AMOUNT)
		Action.click(Selector.BTN_CONFIRM_TRANSFER_AMOUNT_MODAL)

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
