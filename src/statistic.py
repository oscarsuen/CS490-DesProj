from database import getdata
#from tabulate import tabulate

def sql(stat):
	rt = "SELECT `Series Code`, `Topic`, `Indicator Name` FROM series WHERE `Indicator Name` LIKE '%"+stat+"%'"
	return [rt]

def searchstat(query):
	array = getdata(sql(query))
	#print(tabulate(array[0], headers=["Series Code", "Topic", "Indicator Name"]))
	return array[0]

#query = "GDP"