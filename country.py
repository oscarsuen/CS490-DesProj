from database import getdata
from tabulate import tabulate

def sql(country):
	rt = "SELECT `Country Code`, `Table Name`, `Long Name` FROM country WHERE "
	rt = rt + "`Long Name` LIKE '%"+country+"%' OR "
	rt = rt + "`Table Name` LIKE '%"+country+"%' OR "
	rt = rt + "`Short Name` LIKE '%"+country+"%' OR "
	rt = rt + "`Country Code` LIKE '%"+country+"%'"
	return rt

def country(query):
	array = getdata(sql(query))
	print(tabulate(array, headers=["Country Code", "Table Name", "Long Name"]))
	print('\n')
	return array

#query = "U.S."