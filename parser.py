import re


def parse_file(filepath):
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
	return columns, data