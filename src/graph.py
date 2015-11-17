from line import linegraph
from scatter import scatterplotyear
from scattercountry import scatterplotcountry
from scattertotal import scatterplottotal

def generate(gtype, data, figure):
	if gtype == "line":
		linegraph(data, figure)
	elif gtype == "scatteryear":
		scatterplotyear(data, figure)
	elif gtype == "scattercountry":
		scatterplotcountry(data, figure)
	elif gtype == "scattertotal":
		scatterplottotal(data, figure)