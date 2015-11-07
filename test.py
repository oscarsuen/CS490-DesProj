from line import line
from scatter import scatter
from country import country
from statistic import stat

stat1 = stat("Inflation")
stat2 = stat("Unemployment, total")

scatter([2012, stat1[0][0], stat2[0][0]])