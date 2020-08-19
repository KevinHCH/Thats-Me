
import db
# from db import db
from pprint import pprint

handler = db.get_db()
# pprint(handler)
query = '''select * 
					 	 from users 
						 where concat(mail_handle,'@',mail_server) = concat(%s,'@',%s)'''


handle = "admin"
mail = "gm.com"
handler.execute(query, [handle, mail])
data = handler.fetchall()

pprint(data)