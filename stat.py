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

def sql(stat):
	rt = "SELECT `Series Code`, `Topic`, `Indicator Name` FROM series WHERE `Indicator Name` LIKE '%"+stat+"%'"
	return rt


def run(query):
	print(tabulate(getdata(sql(query)), headers=["Series Code", "Topic", "Indicator Name"]))

query = "Foreign Direct Investment"
run(query)