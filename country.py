import pymysql.cursors
from tabulate import tabulate

def getdata(sql):
	co = pymysql.connect(host='localhost', user='root', db='econtest')
	try:
		with co.cursor() as cursor:
			cursor.execute(sql)
			rt = cursor.fetchall()
	finally:
		co.close()
		return rt

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