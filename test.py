from line import linegraph
from scatter import scatterplotyear
from scattercountry import scatterplotcountry
from scattertotal import scatterplottotal
from country import searchcountry
from statistic import searchstat

s1 = searchstat("Unemployment, total")
s2 = searchstat("GDP per capita")
scatterplottotal(["SL.UEM.TOTL.ZS", "NY.GDP.PCAP.CD"])