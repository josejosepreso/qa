import psycopg2
from config.const import Configuration
from core.exceptions import TimeoutException
from dotenv import load_dotenv
import os

load_dotenv()

DB_OTP_SERVICES = os.getenv("DB_OTP_SERVICES")

class DBRequest:
	@staticmethod
	def get_most_recent_OTP(client_identifier: str) -> str:
		try:
			conn = psycopg2.connect(DB_OTP_SERVICES)
			cur = conn.cursor()
			
			query = f"""
				select otp
				from otp_configuration.otp_verification
				-- where identifier = '{ client_identifier }'
				order by issued_date desc
				limit 1;
			"""

			rows = []
			retries = 0

			while not rows:
				if retries > Configuration.RETRIES_LIMIT:
					raise TimeoutException("Couldn't get otp")

				cur.execute( query )
				rows = cur.fetchall()

			assert len(rows) == 1 and rows[0][0]
			
			return rows[0][0]
		except Exception:
			raise
