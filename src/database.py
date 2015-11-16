import pymysql.cursors

def getdata(sql):
	co = pymysql.connect(host='localhost', user='root', db='econtest')
	rt = []
	try:
		with co.cursor() as cursor:
			for i in sql:
				cursor.execute(i)
				rt.append(cursor.fetchall())
	finally:
		co.close()
		return rt