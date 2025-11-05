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
