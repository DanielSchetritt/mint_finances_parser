import os
import csv
import datetime


def parse_csv_file(file_path, target_directory=''):
	file = open(file_path, 'r')
	row_reader = csv.reader(file, delimiter=',')
	first_line = True
	columns = None
	data = []
	for line in row_reader:
		if first_line:
			first_line = False
			# line[0] = 'date_'
			columns = line
		else:
			data.append(line)

	if target_directory != '':
		filename = file_path.split('/')[-1].split('.')
		now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
		filename[0] = filename[0] + '_' + now
		filename = '.'.join(filename)
		# os.system('mv {} {}'.format(file_path, target_directory+filename))

	return columns, data
