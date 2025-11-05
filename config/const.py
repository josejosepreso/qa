from config.enums import *

class Configuration:
	RETRIES_LIMIT = 10
	BANCA_DIGITAL_LOGIN_URL = "https://fab-uat.bancocuscatlan.com.hn/banca-personas/inicio/login"
	AUTH_SERVICE_URL = "https://apigwuat.bancocuscatlan.com.hn/authenticate/authFromICService"
	DOWNLOAD_VOUCHER_SERVICE_URL = "https://apigwuat.bancocuscatlan.com.hn/transaction-details/download-voucher?transactionId=.*"
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

	ACH_CREDIT_CARD_NUMBER = "4568240009141811"
	ACH_CREDIT_CARD_BANK = ACH.DAVIVIENDA
