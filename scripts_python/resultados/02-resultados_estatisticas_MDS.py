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
	'''
	for feature in layer:
		if (feature.GetField("MODA_MDE")  is None) or  
		(feature.GetField("MEDIA_MDE")  is None) or 
		(feature.GetField("COTA_MAX_S")  is None) or 
		(feature.GetField("COTA_MIN_S")  is None) or 
		(feature.GetField("DESVIO_MDE")  or None) : 
			arrayEdif.append(feature.GetField("ID_EDIFICA"))
		
	
	for feature in layer:
		arrayEdif.append(feature.GetField("MODA_MDE"))
	
	print (len(arrayEdif))
	
	df = pd.DataFrame(arrayEdif)
	print (df.describe())
	'''
	arrayDesvio = []
	arrayIndice = []
	
	
	count = 0;
	x = 0
	for feature in layer:
		if  ((feature.GetField("DESVIO_MDE")  is  not None )and   (feature.GetField("DESVIO_MDE") > x )  and  (feature.GetField("DESVIO_MDE") <= x+1)):
			count = count +1
	arrayDesvio.append(count)
	
	'''
	for  x in range(0,):
		print (x)
		count = 1;
		dataSource = driver.Open(daShapefile, 1)
		layer = dataSource.GetLayer()
		for feature in layer:
			if  ((feature.GetField("DESVIO_MDE")  is  not None )and   (feature.GetField("DESVIO_MDE") > x )  and  (feature.GetField("DESVIO_MDE") <= x+1 )):
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
	'''
	print (len(arrayDesvio))
	print ((arrayDesvio))