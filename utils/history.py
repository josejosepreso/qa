from config.enums import *

class History:
	@staticmethod
	def register_transfer(transfer):
		def wrapper( *args, **kwargs ):
			transfer()

			#
			origin_account: str = kwargs.get("origin_account_number")
			origin_account_currency: Currency = kwargs.get("origin_account_currency", Currency.LPS)
			destination_account: str = kwargs.get("destination_account_number")
			destination_account_currency: Currency = kwargs.get("destination_account_currency", Currency.PS)
			amount: int = kwargs.get("amount")
			currency: Currency = kwargs.get("currency", Currency.LPS)
		return wrapper

	@staticmethod
	def register_credit_card_payment(credit_card_payment):
		pass

	@staticmethod
	def register_credit_payment(credit_payment):
		pass

	@staticmethod
	def register_service_payment(service_payment):
		pass
