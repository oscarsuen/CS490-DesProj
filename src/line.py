from database import getdata
import matplotlib
from textwrap import fill

def sql(info):
	columns = ""
	for i in range(info[0],info[1]+1):
		columns = columns + "`" + str(i) + "`, "
	columns = columns[:-2]
	
	result = "SELECT "+columns+" FROM data WHERE `Country Code`='"+info[2]+"' AND `Indicator Code`='"+info[3]+"'"
	country = "SELECT `Short Name` FROM country WHERE `Country Code`='"+info[2]+"'"
	stat = "SELECT `Indicator Name` FROM series WHERE `Series Code`='"+info[3]+"'"
	return [result, country, stat]

def plot(info, result, figure):
	figure.plot(range(info[0],info[1]),result[0][0][:-1])
	figure.set_xlim(info[0],info[1]-1)
	figure.set_xlabel(fill("Year",55).replace("$","\$"))
	figure.set_ylabel(fill(result[2][0][0],55).replace("$","\$"))
	figure.set_title(fill(result[1][0][0]+" "+result[2][0][0],55).replace("$","\$"))

def linegraph(info, figure):
	plot(info, getdata(sql(info)), figure)

#info = [1960, 2014, "USA", "NY.GDP.MKTP.KD"]