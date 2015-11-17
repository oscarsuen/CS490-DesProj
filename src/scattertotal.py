from database import getdata
import matplotlib

def sql(info):
	result1 = "SELECT * FROM data WHERE `Indicator Code`='"+info[0]+"'"
	result2 = "SELECT * FROM data WHERE `Indicator Code`='"+info[1]+"'"
	return [result1, result2]

def points(array):
	p = []
	for i in range(249):
		for j in range(4, 60):
			t1 = array[0][i][j]
			t2 = array[1][i][j]
			if t1 != 0 and t2 != 0:
				p.append([t1,t2])
	return p

def plot(stat1, stat2, points, figure):
	figure.scatter([i[0] for i in points],[i[1] for i in points])
	figure.set_xlabel(stat1)
	figure.set_ylabel(stat2)
	figure.set_title(stat1+" vs. "+stat2)

def scatterplottotal(info, figure):
	sequel = sql(info)
	data = getdata(sequel)
	p = points(data)
	plot(data[0][0][2], data[1][0][2], p, figure)

#info = ["SL.UEM.TOTL.ZS", "FP.CPI.TOTL.ZG"]