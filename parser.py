import re
import os
import datetime


def parse_file(filepath, target_directory=''):
	file = open(filepath, 'r')

	first_line = True
	columns = None
	data = []
	for line in file:
		line = line.replace('\n', '').replace('\'', '')
		temp = []
		if first_line:
			first_line = False
			columns = line.lower().replace(' ', '_').replace('date', 'date_').split(',')
		else:
			line = re.findall(r'"([^"]*)"', line)
			for item in line:
				temp.append(item.replace(',', ''))
		if temp:
			data.append(temp)

	if target_directory != '':
		filename = filepath.split('/')[-1].split('.')
		now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
		filename[0] = filename[0] + now
		filename = '.'.join(filename)
		os.system('mv {} {}'.format(filepath, target_directory+filename))

	return columns, data