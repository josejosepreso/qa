from config.enums import *

class History:
	_handlers = {
		TransactionType.TRANSFER: "register_transfer"
		, TransactionType.LOAN_PAYMENT: "register_loan_payment"
		, TransactionType.CREDIT_CARD_PAYMENT: "register_credit_card_payment"
		, TransactionType.SERVICE_PAYMENT: "register_service_payment"
	}

	@staticmethod
	def register_transaction(transaction_type: TransactionType):
		def decorator(transaction):
			def wrapper( *args, **kwargs ):
				result = transaction( *args, **kwargs )

				handler_name = History._handlers.get(transaction_type)
				if not handler_name:
					raise Exception

				handler = getattr(History, handler_name)
				handler(kwargs)

				return result
			return wrapper
		return decorator

	@staticmethod
	def register_transfer(transfer):
		origin_account: str = transfer.get("origin_account_number")
		origin_account_currency: Currency = transfer.get("origin_account_currency", Currency.LPS)
		destination_account: str = transfer.get("destination_account_number")
		destination_account_currency: Currency = transfer.get("destination_account_currency", Currency.LPS)
		amount: int = transfer.get("amount")
		currency: Currency = transfer.get("currency", Currency.LPS)
	    # TODO
	
	@staticmethod
	def register_credit_card_payment(payment):
	    # TODO
		pass
	
	@staticmethod
	def register_loan_payment(payment):
	    # TODO
		pass
	
	@staticmethod
	def register_service_payment(payment):
	    # TODO
		pass
