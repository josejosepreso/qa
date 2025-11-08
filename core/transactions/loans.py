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

class LoanPayment:
	@History.register_transaction(TransactionType.LOAN_PAYMENT)
	@Action.navigate(TransactionType.LOAN_PAYMENT)
	@staticmethod
	def own(loan_number: str):
		pass

	@History.register_transaction(TransactionType.LOAN_PAYMENT)
	@Action.navigate(TransactionType.LOAN_PAYMENT)
	@staticmethod
	def third_party(
			loan_number: str = Configuration.THIRD_PARTY_LOAN_NUMBER,
			origin_account_number: str = None
	):
		Action.click(Selector.BTN_OTHER_LOAN)

		if origin_account_number is not None:
			Action.set_origin_account(origin_account_number)

		Action.type(Selector.INPUT_THIRD_PARTY_LOAN_NUMBER, loan_number)

		WebDriverWait(driver, Configuration.TIMEOUT_LIMIT).until(EC.element_to_be_clickable(Selector.BTN_CONFIRM_THIRD_PARTY_LOAN_NUMBER)).click()

		Action.click(Selector.BTN_DO_THIRD_PARTY_LOAN_PAYMENT)
		Action.click(Selector.BTN_CONFIRM_AMOUNT_THIRD_PARTY_LOAN_PAYMENT)

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

	@History.register_transaction(TransactionType.LOAN_PAYMENT)
	@Action.navigate(TransactionType.LOAN_PAYMENT)
	@staticmethod
	def ach(
			loan_number: str = Configuration.ACH_LOAN_NUMBER,
			loan_bank: ACH = Configuration.ACH_LOAN_BANK,
			origin_account_number: str = None
	):
		pass
