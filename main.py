from db_connection import dbconnection
import parser
import os

transaction_file_directory = os.path.dirname(os.path.realpath(__file__))

db_directory = transaction_file_directory + '/database/'
transaction_file_target_directory = transaction_file_directory + '/parsed_files/'
transaction_file_directory += '/transaction_file/'
db_name = 'finances.db'
db_table = 'finances'
db_conn = dbconnection(db_directory, db_name)

for file in os.listdir(transaction_file_directory):
	if file == '.gitignore':
		continue
	elif file.split('.')[-1].lower() != 'csv':
		print('You must provide a CSV file')
	else:
		print('Processing: {}\n'.format(file))
		columns, data = parser.parse_csv_file(transaction_file_directory + file, transaction_file_target_directory)
		db_conn.insert_data(columns, data, db_table)

db_conn.close_connection()
