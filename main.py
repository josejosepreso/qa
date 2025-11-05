from core.driver_common import get_driver
from core.actions import Action
from core.transactions.transfers import Transfer
from core.transactions.credits import CreditPayment
from core.transactions.credit_cards import CreditCardPayment
from core.transactions.services import ServicePayment

transfers = [
	# cta destino,  cantidad   cta origen
	( "218030021032", 1 , "211040202570" ),
	( "211011242211", 2 , "213050019509" ),
	( "218030021032", 1 , None ),
]

try:
	Action.login()
	Transfer.ach()
	CreditCardPayment.ach()
	CreditCardPayment.third_party()
	CreditCardPayment.own()
	Transfer.own_account()
	"""
	for destination_account, amount, origin_account in transfers:
		Transfer.third_party(destination_account, amount, origin_account)
	"""
finally:
	input("Press Enter to close the browser...")
	get_driver().quit()
