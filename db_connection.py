import sqlite3


class dbconnection:
	def __init__(self, db_path, db_name):
		self.db_path = db_path
		self.db_name = db_name
		self.db_conn = sqlite3.connect(db_path + db_name)

	def close_connection(self):
		self.db_conn.close()

	def insert_data(self, columns, data, table_name):
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

