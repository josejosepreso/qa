from config.enums import *
import config.user as user

ENV = "uat" if user.ENVIRONMENT == Environment.UAT else "dev"

class Configuration:
	RETRIES_LIMIT = 20
	BANCA_DIGITAL_LOGIN_URL = f"https://fab-{ ENV }.bancocuscatlan.com.hn/banca-personas/inicio/login"
	BANCA_DIGITAL_HOME_URL = f"https://fab-{ ENV }.bancocuscatlan.com.hn/banca-personas/home"
	AUTH_SERVICE_URL = f"https://apigw{ ENV }.bancocuscatlan.com.hn/authenticate/authFromICService"
	DOWNLOAD_VOUCHER_SERVICE_URL = f"https://apigw{ ENV }.bancocuscatlan.com.hn/transaction-details/download-voucher?transactionId=.*"
	DOWNLOAD_VOUCHER_SERVICE_URL_PATTERN = ".*download-voucher.*"
	OTPS_FILE = "otps.txt"
	HISTORY_FILE = "history.json"
	TIMEOUT_LIMIT = 60
	DEFAULT_AMOUNT = 100

	ACH_CLIENT_NAME = "Jose Bautista"
	ACH_CLIENT_DOCUMENT_TYPE = DocumentType.IDENTITY_NUMBER
	ACH_CLIENT_IDENTITY_NUMBER = "0801197906854"
	ACH_ACCOUNT_NUMBER = "230503000186"
	ACH_ACCOUNT_BANK = ACH.LAFISE
	ACH_ACCOUNT_TYPE = AccountType.SAVINGS

	THIRD_PARTY_CREDIT_CARD_NUMBER = "4551460024206295"

	THIRD_PARTY_LOAN_NUMBER = "101056910862"

	ACH_CREDIT_CARD_NUMBER = "4568240009141811"
	ACH_CREDIT_CARD_BANK = ACH.DAVIVIENDA

	ACH_LOAN_NUMBER = ""
	ACH_LOAN_BANK = ACH.DAVIVIENDA
