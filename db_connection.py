import sqlite3
from datetime import datetime, date
from helpers import sqlite_reserved_words
import dateutil.parser as dateutil


class dbconnection:
	def __init__(self, db_path, db_name):
		self.db_path = db_path
		self.db_name = db_name
		self.db_conn = sqlite3.connect(db_path + db_name, detect_types=sqlite3.PARSE_DECLTYPES)
		self.db_curs = self.db_conn.cursor()

	def close_connection(self):
		self.db_conn.close()

	def get_table_info(self, table_name):
		execution_string = 'PRAGMA table_info({})'.format(table_name)
		data = self.db_curs.execute(execution_string)
		return data.fetchall()

	def get_columns_info(self, table_info, columns):
		# INFO --
		# the tuple that is process here will have the following structure:
		# (column id, name	, data type	, null		, default value	, primary key	)
		# (integer	, text	, text		, boolean	, any			, boolean		)
		column_info = {
			'name_dict': {},
			'index_dict': {}
		}
		for i in range(len(columns)):
			exists = False
			for tuple in table_info:
				if exists:
					pass
				if columns[i] in tuple:
					if columns[i] == tuple[1]:
						exists = True
						column_info['name_dict'][columns[i]] = {
							'db_index': tuple[0],
							'csv_index': i,
							'name': tuple[1],
							'data_type': tuple[2],
							'nullable': True if tuple[3] == 1 else False,
							'default_value': tuple[4],
							'primary_key': True if tuple[5] == 1 else False,

						}
						column_info['index_dict'][i] = column_info['name_dict'][columns[i]]
					elif columns[i].upper() in sqlite_reserved_words:
						if columns[i] == '{}'.format(columns[i] + '_'):
							columns[i] += '_'

			if not exists:
				print('Column header <{}> not found. ABORTING'.format(columns[i]))
				exit(1)
		return column_info

	def process_values(self, table_info, data, columns):
		# all this does right now is check dates to ensure they are in the correct format.
		# TODO(Gabriel): add more data sanitation
		column_info = self.get_columns_info(table_info, columns)
		for i in range(len(data)):
			for j in range(len(data[i])):
				if column_info['index_dict'][j]['data_type'] == 'date':
					data[i][j] = str(dateutil.parse(data[i][j]).date())
		return data

	def insert_data(self, columns, data, table_name):
		table_info = self.get_table_info(table_name)
		data = self.process_values(table_info, data, columns)
		execution_string = 'INSERT INTO {0} ({1}) values {2}'
		for i in range(len(columns)):
			columns[i] = "'{}'".format(columns[i])
		columns = ','.join(columns)

		for i in range(len(data)):
			for j in range(len(data[i])):
				data[i][j] = "'{}'".format(data[i][j].replace("'", ''))
			data[i] = ','.join(data[i])
			data[i] = '({})'.format(data[i])
		data = ',\n'.join(data)
		execution_string = execution_string.format(table_name, columns, data)
		self.db_conn.execute(execution_string)
		self.db_conn.commit()
