from db_connection import dbconnection
import parser
import os

transaction_file_directory = os.path.dirname(os.path.realpath(__file__))
db_directory = transaction_file_directory + '/database/'
transaction_file_directory += '/transaction_file/'
db_name = 'finances.db'
db_table = 'finances'
db_conn = dbconnection(db_directory, db_name)

for file in os.listdir(transaction_file_directory):
	if file == '.gitignore':
		continue
	else:
		columns, data = parser.parse_file(transaction_file_directory + file)
		db_conn.insert_data(columns, data, db_table)

db_conn.close_connection()
