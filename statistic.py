from database import getdata
from tabulate import tabulate

def sql(stat):
	rt = "SELECT `Series Code`, `Topic`, `Indicator Name` FROM series WHERE `Indicator Name` LIKE '%"+stat+"%'"
	return rt


def stat(query):
	array = getdata(sql(query))
	print(tabulate(array, headers=["Series Code", "Topic", "Indicator Name"]))
	print('\n')
	return array

#query = "GDP"