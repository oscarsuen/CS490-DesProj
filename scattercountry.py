from database import getdata
import matplotlib.pyplot as plt

def sql(info):
	result1 = "SELECT * FROM data WHERE `Country Code`='"+info[0]+"' AND `Indicator Code`='"+info[1]+"'"
	result2 = "SELECT * FROM data WHERE `Country Code`='"+info[0]+"' AND `Indicator Code`='"+info[2]+"'"
	return [result1, result2]

def points(array):
	p = []
	for i in range(4, 60):
		t1 = array[0][0][i]
		t2 = array[1][0][i]
		if t1 != 0 and t2 != 0:
			p.append([t1,t2])
	return p

def plot(country, stat1, stat2, points):
	plt.scatter([i[0] for i in points],[i[1] for i in points])
	plt.xlabel(stat1)
	plt.ylabel(stat2)
	plt.title(stat1+" vs. "+stat2+" in "+country)
	#plt.savefig("graphs/"+stat1+"-"+stat2+"-"+country+".png")
	plt.savefig("graphs/image.png")
	#plt.show()

def scatterplotcountry(info):
	sequel = sql(info)
	data = getdata(sequel)
	p = points(data)
	plot(info[0], data[0][0][2], data[1][0][2], p)

#info = ["USA", "SL.UEM.TOTL.ZS", "FP.CPI.TOTL.ZG"]