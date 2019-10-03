# ##############
# Analise dos dados gerados MDS
# autor: Tiago da Costa Norberto
# data  22/08/2018
###

import sys
from osgeo import ogr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daShapefile = 'D:/repositorio_tcc_puc/dados/final/edificacao/EDIFICACAO.EDIFICACAO.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)


# Check to see if shapefile is found.
if dataSource is None:
	print ('Nao foi possi %s' % (daShapefile))
else:
	print ('Opened %s' % (daShapefile))
	layer = dataSource.GetLayer()
	featureCount = layer.GetFeatureCount()
	print ("Number of features  %s: " % (featureCount))

	arrayEdif = []
	
	i = 0;
	
	for feature in layer:
		if ((feature.GetField("MODA_MDT")  is None) 
		or  (feature.GetField("MEDIA_MDT")  is None) 
		or (feature.GetField("COTA_MAX_T")  is None) 
		or (feature.GetField("COTA_MIN_T")  is None) 
		or (feature.GetField("DESVIO_MDT")  is None) ): 
			arrayEdif.append(feature.GetField("ID_EDIFICA"))

	
	df = pd.DataFrame(arrayEdif)
	print (df.describe())
	'''
	arrayDesvio = []
	arrayIndice = []
		

	for  x in range(0,100):
		print (x)
		count = 1;
		dataSource = driver.Open(daShapefile, 1)
		layer = dataSource.GetLayer()
		for feature in layer:
			if  ((feature.GetField("DESVIO_MDT")  is  not None )and   (feature.GetField("DESVIO_MDT") > x )  and  (feature.GetField("DESVIO_MDT") <= x+1 )):
				count = count +1
		arrayDesvio.append(count)
		arrayIndice.append(x)
		dataSource.Destroy()		
			
		
	
	print ((arrayDesvio))
	print ((arrayIndice))
	
	df = pd.DataFrame({'y':arrayDesvio, 'x' :arrayIndice})
	df.plot.bar(x='x', y='y', rot=0)
	#plt.show()
	print (df.describe())
