import pymysql.cursors
import matplotlib.pyplot as plt

co = pymysql.connect(host='localhost',
	user='root', db='econtest')

columns = ""
for i in range(1960,2016):
	columns = columns + "`" + str(i) + "`, "
columns = columns[:-2]

try:
	with co.cursor() as cursor:
		sql = "SELECT "+columns+" FROM data WHERE `Country Code`='USA' AND `Indicator Code`='NY.GDP.MKTP.KD'"
		cursor.execute(sql)
		result=cursor.fetchone()
		print(result)
finally:
	co.close()

plt.plot(range(1960,2015),result[:-1])
plt.xlabel('Year')
plt.ylabel('GDP (2005$)')
plt.title('US GDP')
plt.show()