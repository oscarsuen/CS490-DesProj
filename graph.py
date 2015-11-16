from PIL import Image

from line import linegraph
from scatter import scatterplotyear
from scattercountry import scatterplotcountry
from scattertotal import scatterplottotal

def generate(gtype, data):
	if gtype == "line":
		linegraph(data)
	elif gtype == "scatteryear":
		scatterplotyear(data)
	elif gtype == "scattercountry":
		scatterplotcountry(data)
	elif gtype == "scattertotal":
		scatterplottotal(data)

	im = Image.open("graphs/image.png")
	im.save("graphs/imagetest.gif","GIF")