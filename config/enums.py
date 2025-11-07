from enum import Enum

class ACH(Enum):
	CUSCATLAN = 1
	BAC = 2
	ATLANTIDA = 3
	FICOHSA = 4
	DAVIVIENDA = 5
	OCCIDENTE = 6
	LAFISE = 7
	CITI = 8
	BANRURAL = 9

class AccountType(Enum):
	SAVINGS = 1

class DocumentType(Enum):
	IDENTITY_NUMBER = 1

class Currency(Enum):
	LPS = 1
	USD = 2

class Environment(Enum):
	UAT = 1
	DEV = 2
	
class TransactionType(Enum):
	TRANSFER = 1
	CREDIT_CARD_PAYMENT = 2
	CREDIT_PAYMENT = 3
	SERVICE_PAYMENT = 4

class CreditCardPaymentAmountType(Enum):
	MINIMUM = 1
	CUSTOM = 2
