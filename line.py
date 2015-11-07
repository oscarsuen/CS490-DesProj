import pymysql.cursors
import matplotlib.pyplot as plt

def getdata(sql):
	co = pymysql.connect(host='localhost', user='root', db='econtest')
	try:
		with co.cursor() as cursor:
			cursor.execute(sql[0])
			result=cursor.fetchone()
			cursor.execute(sql[1])
			country = cursor.fetchone()
			cursor.execute(sql[2])
			stat = cursor.fetchone()
	finally:
		co.close()
		return [result, country, stat]

def sql(info):
	columns = ""
	for i in range(info[0],info[1]+1):
		columns = columns + "`" + str(i) + "`, "
	columns = columns[:-2]
	
	result = "SELECT "+columns+" FROM data WHERE `Country Code`='"+info[2]+"' AND `Indicator Code`='"+info[3]+"'"
	country = "SELECT `Short Name` FROM country WHERE `Country Code`='"+info[2]+"'"
	stat = "SELECT `Indicator Name` FROM series WHERE `Series Code`='"+info[3]+"'"
	return [result, country, stat]

def plot(info, result):
	plt.plot(range(info[0],info[1]),result[0][:-1])
	plt.xlim(info[0],info[1]-1)
	plt.xlabel('Year')
	plt.ylabel(result[2][0])
	plt.title(result[1][0]+" "+result[2][0])
	plt.show()

def run(info):
	plot(info, getdata(sql(info)))

info = [1960, 2014, "USA", "NY.GDP.MKTP.KD"]
run(info)