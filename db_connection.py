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
		columns = ','.join(columns).replace('"', "'")

		for j in range(len(data)):
			row = data[j]
			for i in range(len(row)):
				if i == 0:
					month, day, year = row[i].split('/')
					if len(day) == 1:
						day = '0' + day
					if len(month) == 1:
						month = '0' + month
					row[i] = "'{0}-{1}-{2}".format(year, month, day)
			temp = "','".join(row)[:-1]
			temp += "''"
			data[j] = '({}),\n'.format(temp)
		data = ''.join(data)
		execution_string = execution_string.format(table_name, columns, data[:-1])[:-1]
		self.db_conn.execute(execution_string)
		self.db_conn.commit()

