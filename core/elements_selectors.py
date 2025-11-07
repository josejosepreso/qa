from selenium.webdriver.common.by import By
from config.enums import *

def css(selector_str: str): return By.CSS_SELECTOR, selector_str
def xpath(selector_str: str): return By.XPATH, selector_str
def name(selector_str: str): return By.NAME, selector_str

class Selector:
	# by css
	LINK_HOME_SCREEN = css("img.desktop-image")
	HOMESCREEN_SIDEBAR_MENU_OPTIONS = css("app-menu-management")
	BTN_TRANSACTION_OPTION = css("app-options-management")
	P_TRANSACTION_OPTION_LABEL = css("p.u-text-blue-00.u-text-center.u-text-blue-80")
	CONTAINER_TRANSACTION_OPTIONS = css("div.container-all-transactions")
	#
	INPUT_USERNAME_LOGIN = css('[formcontrolname="username"]')
	INPUT_USERNAME_PASSWORD = css('[formcontrolname="password"]')
	INPUT_TRANSFER_AMOUNT = css('[inputcontroller="financial"]')
	APP_VOUCHER = css("app-voucher")
	CHECKBOX_DESTINATION_ACCOUNT_TYPE = css('input[type="checkbox"]')
	DIV_ADD_ORIGIN_ACCOUNT = css('app-add-product-card')
	INPUT_ACH_CLIENT_NAME = css('[formcontrolname="fullname"]')
	INPUT_ACH_CLIENT_ID_NUMBER = css('[formcontrolname="idNumber"]')
	ACH_BANK_SWIPER = css("swiper-container")
	ACH_SWIPER_SLIDE = css("swiper-slide")
	BTN_SWIPER_NEXT_ACH_BANK = css(".swiper-button-next")
	APP_MY_PRODUCTS = css("app-my-products")
	BTN_TRANSFER_OTHER_ACCOUNT = css("div.btn-other")
	BTN_OTHER_CREDIT_CARD = css("div.btn-other")
	# DIV_OWN_ACCOUNT_CARD = css("app-favorite-card")
	P_OWN_ACCOUNT_NUMBER = css("p.u-b-menu.text-ellipsis.text-ellipsis--card-large-v3")
	DIV_OWN_CREDIT_CARD_CARD = css("app-favorite-card")
	HOMESCREEN_BTN_BG_BLUE_00 = css("div.u-bg-blue-00")

	## Pago TCR
	CONTAINER_SELECT_CREDIT_CARD_PAYMENT_CURRENCY = css("app-selected-payment-currency")
	BTN_SELECT_CREDIT_CARD_PAYMENT_CURRENCY = css("button.buttton-currency")
	BTN_SELECT_CREDIT_CARD_PAYMENT_AMOUNT = css("div.chip")
	CONTAINER_SELECT_CREDIT_CARD_PAYMENT_AMOUNT_TYPE = css("app-transaction-quicks-amout")

	## Pago prestamo
	BTN_OTHER_CREDIT = css("div.btn-other")
	
	# by xpath
	BTN_LOGIN = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-sing-in/div/div[7]/app-login-form/div/div[2]/form/button")
	BTN_DISMISS_DUPLICATE_SESSION = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-duplicate-session/div/div[5]/button')
	BTN_CHANGE_PASSWORD = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-dialog-common/div/button')
	# LINK_HOME_SCREEN = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/app-toolbar/mat-toolbar/div/div[1]/div[1]')

	## Pago prestamo
	### A terceros
	BTN_CONFIRM_THIRD_PARTY_CREDIT_NUMBER = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-loans/app-home-transaction-third-party/div/div/div/app-step-one/div/div[3]/button")
	BTN_DO_THIRD_PARTY_CREDIT_PAYMENT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-loans/app-home-transaction-third-party/div/div/div/app-step-two/div/button")
	BTN_CONFIRM_AMOUNT_THIRD_PARTY_CREDIT_PAYMENT = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-dialog-confirm-transaction/div/div[2]/button[1]')

	## Pago TCR
	BTN_CREDIT_CARD_PAYMENT_HOMESCREEN = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[1]/div[1]/app-menu-management/div/div/app-options-management[2]/div/div[1]')
	# BTN_SELECT_LPS_CURRENCY = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-own-credit-card/div/div/div[2]/app-selected-payment-currency/div/button[1]")
	# BTN_SELECT_USD_CURRENCY = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-own-credit-card/div/div/div[2]/app-selected-payment-currency/div/button[2]")
	# BTN_CREDIT_CARD_CUSTOM_AMOUNT_PAYMENT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-own-credit-card/div/div/div[2]/app-transaction-quicks-amout/div/div[3]")
	BTN_DO_CREDIT_CARD_PAYMENT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-own-credit-card/div/div/div[2]/button")
	BTN_CONFIRM_AMOUNT_CREDIT_CARD_PAYMENT = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-dialog-confirm-transaction/div/div[2]/button[1]')
	# BTN_OTHER_CREDIT_CARD = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-credit-card/div/app-dynamic-transaction-and-favorite/div/div[3]/div[2]/button")
	BTN_CONFIRM_CREDIT_CARD_NUMBER = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-credit-card/app-home-transaction-third-party/div/div/div/app-tcr-step-one/div/div[3]/button")
	BTN_SELECT_USD_CURRENCY_THIRD_PARTY_CREDIT_CARD_PAYMENT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-credit-card/app-home-transaction-third-party/div/div/div/app-tcr-step-two/div/div[2]/app-currency-selector/div/button[2]")

	### Pago TCR a terceros
	BTN_DO_THIRD_PARTY_CREDIT_CARD_PAYMENT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-credit-card/app-home-transaction-third-party/div/div/div/app-tcr-step-two/div/button")

	# Transferencias
	BTN_TRANSFER_HOMESCREEN = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[1]/div[1]/app-menu-management/div/div/app-options-management[1]/div/div[1]')
	# BTN_TRANSFER_HOMESCREEN xpath(= '/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[1]/div[2]/app-mobile-menu/div/swiper-container/swiper-slide[1]/div/app-options-management/div')
	# BTN_TRANSFER_OTHER_ACCOUNT = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-transfer/div/app-dynamic-transaction-and-favorite/div/div[3]/div[2]/button')
	BTN_CONFIRM_ACCOUNT_NUMBER = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/div/app-step-one/div/div[3]/button')
	BTN_CONFIRM_TRANSFER_AMOUNT = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/div/app-step-two/div/button')
	BTN_CONFIRM_TRANSFER_AMOUNT_MODAL = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-dialog-confirm-transaction/div/div[2]/button[1]')
	INPUT_FIRST_OTP_DIGIT_MODAL = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-otp/div/app-inputs/form/input[1]')
	BTN_CONFIRM_OTP_MODAL = xpath('//*[contains(@id, "mat-mdc-dialog-")]/div/div/app-otp/div/div[2]/button[1]')
	BTN_DOWNLOAD_VOUCHER = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-own-success/app-voucher/div/div/div[2]/div[2]/button')
	BTN_CHANGE_ORIGIN_ACCOUNT_NUMBER = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/app-product-card/div/div/div[2]/button')
	BTN_GO_BACK_CHANGE_ORIGIN_ACCOUNT = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-account-selector/app-product-switcher-list/div/div[1]/app-back-button/div/i")
	P_FIRST_ORIGIN_ACCOUNT_NUMBER = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-account-selector/app-product-switcher-list/div/div[2]/div[2]/app-product-card/div/div/div[1]/div/p")
	P_SELECTED_ORIGIN_ACCOUNT_NUMBER = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/app-product-card/div/div/div[1]/div/p")
	## Transferencia a cta propia
	# DIV_FIRST_OWN_ACCOUNT_CARD = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-transfer/div/app-dynamic-transaction-and-favorite/div/div[4]/div[2]/app-favorite-card[1]')
	BTN_SELECT_ORIGIN_FIRST_OWN_ACCOUNT = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-account-own-selector/app-product-switcher-list/div/div[2]/div[2]/app-product-card/div/div/div[2]/button')
	BTN_DO_TANSFER = xpath('/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-transfer-own-accounts/div/div/div[2]/button')

	## Transferencia ach
	BTN_SELECT_CHECK_ACCOUNT_TYPE = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/div/app-step-one/div/app-external-destination-account/div/div/button[2]")
	BTN_CONFIRM_DESTINATION_ACCOUNT_NUMBER = xpath("/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-third-accounts/app-home-transaction-third-party/div/div/div/app-step-one/div/div[3]/button")
	
	# by name
	INPUT_ACCOUNT_NUMBER = name("accountNumber")
	INPUT_CREDIT_CARD_PAYMENT_AMOUNT = name("amount")
	INPUT_THIRD_PARTY_CREDIT_CARD_PAYMENT_AMOUNT = name("amountToTransfer")
	INPUT_CREDIT_CARD_NUMBER = name("accountNumber")

	## Pago prestamo
	INPUT_THIRD_PARTY_CREDIT_NUMBER = name("accountNumber")

	@staticmethod
	def get_button_select_origin_account(idx: int):
		return xpath(f"/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-account-selector/app-product-switcher-list/div/div[2]/div[{ idx }]/app-product-card/div/div/div[2]/button")

	@staticmethod
	def get_p_origin_account_number(idx: int):
		return xpath(f"/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-account-selector/app-product-switcher-list/div/div[2]/div[{ idx }]/app-product-card/div/div/div[1]/div/p")

	@staticmethod
	def get_own_credit_card(idx: int):
		return xpath(f"/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home-credit-card/div/app-dynamic-transaction-and-favorite/div/div[2]/div[2]/app-favorite-card[{ idx }]")
