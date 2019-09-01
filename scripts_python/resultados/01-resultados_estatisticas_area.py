# calculo de Aea
import sys
from osgeo import ogr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daShapefile = 'D:/repositorio_tcc_puc/dados/final/EDIFICACAO.EDIFICACAO.shp'

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)


# Check to see if shapefile is found.
if dataSource is None:
	print ('Nao foi possi %s' % (daShapefile))
else:
	print ('Opened %s' % (daShapefile))
	layer = dataSource.GetLayer()
	featureCount = layer.GetFeatureCount()
	print ("Number of features in %s: " % (featureCount))
	
	arrayArea = []
	
	for feature in layer:
		arrayArea.append(feature.GetField("AREA"))
	
	df = pd.DataFrame(arrayArea)
	print (df.describe())
	