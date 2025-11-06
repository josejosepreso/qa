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
