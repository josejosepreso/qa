from core.driver_common import get_driver
from core.actions import Action
from core.transactions.transfers import Transfer
from core.transactions.loans import LoanPayment
from core.transactions.credit_cards import CreditCardPayment
from core.transactions.services import ServicePayment
from config.const import Configuration

transfers = [
	# cta destino,  cantidad   cta origen
	( "218030021032", 1 , "211040202570" ),
	( "211011242211", 2 , "213050019509" ),
	( "218030021032", 1 , None ),
]

try:
	Action.login()

	Transfer.ach(
			Configuration.ACH_ACCOUNT_NUMBER,
			Configuration.ACH_ACCOUNT_BANK,
			Configuration.ACH_ACCOUNT_TYPE,
			Configuration.DEFAULT_AMOUNT,
			"213050019509"
	)

	CreditCardPayment.ach()

	CreditCardPayment.third_party()

	for destination_account, amount, origin_account in transfers:
		Transfer.third_party(destination_account, amount, origin_account)

	Transfer.own_account()

	CreditCardPayment.own()

	LoanPayment.third_party()
finally:
	input("Press Enter to close the browser...")
	get_driver().quit()
