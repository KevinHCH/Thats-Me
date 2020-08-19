import psycopg2, psycopg2.extras
# import config.config as config #script shell
from .config import config #Flask app

def get_db():
	try:
		connection = psycopg2.connect(user=config.DB_USER,
																	password=config.DB_PASSWORD,
																	host=config.DB_HOST,
																	port=config.DB_PORT,
																	database=config.DB_NAME
																 )
		# This line just returns the data as tuple and you can access to the data like a Dict, but don't show the data as dict
		# cursor = connection.cursor(cursor_factory= psycopg2.extras.DictCursor)
		# This line enables the Data as DICT (Like PHP)
		cursor = connection.cursor(cursor_factory= psycopg2.extras.RealDictCursor)
		return cursor
	except (Exception, psycopg2.Error) as error:
		print(f"Connection Error: {error}")

