from database import getdata
import matplotlib.pyplot as plt

def sql(info):
	result1 = "SELECT `Country Code`,`"+str(info[0])+"` FROM data WHERE `Indicator Code`='"+info[1]+"'"
	result2 = "SELECT `Country Code`,`"+str(info[0])+"` FROM data WHERE `Indicator Code`='"+info[2]+"'"
	stat1 = "SELECT `Indicator Name` FROM series WHERE `Series Code`='"+info[1]+"'"
	stat2 = "SELECT `Indicator Name` FROM series WHERE `Series Code`='"+info[2]+"'"
	return [result1, result2, stat1, stat2]

def points(array):
	p = []
	for i in range(249):
		t1 = array[0][i][1]
		t2 = array[1][i][1]
		if t1 != 0 and t2 != 0:
			p.append([t1,t2])
	return p

def plot(year, stat1, stat2, points):
	plt.scatter([i[0] for i in points],[i[1] for i in points])
	plt.xlabel(stat1)
	plt.ylabel(stat2)
	plt.title(stat1+" vs. "+stat2+" in "+str(year))
	plt.savefig("graphs/"+stat1+"-"+stat2+"-"+str(year)+".png")
	plt.show()

def scatter(info):
	sequel = sql(info)
	data = getdata(sequel)
	p = points(data)
	plot(info[0], data[2][0][0], data[3][0][0], p)

#info = [2014, "NY.GDP.PCAP.KD", "FP.CPI.TOTL.ZG"]