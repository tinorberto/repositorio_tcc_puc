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
dataSource = driver.Open(daShapefile, 0)


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

	arrayDesvioMDE = []
		
	count = 0;
	x = 0
	for feature in layer:
		if  ((feature.GetField("DESVIO_MDE")  is  not None )and   (feature.GetField("DESVIO_MDE") > x ) ):
			count = count +1
			array = []
			array.append(feature.GetField("DESVIO_MDE"))
			array.append(feature.GetField("DESVIO_MDT"))
			array.append(feature.GetField("AREA"))
			arrayDesvioMDE.append(array)
			#if count > 1000:
			#	break
			
			
	print ('------------- COVARIANCIA ---------------	')
	pd = (pd.DataFrame(arrayDesvioMDE, columns=["DESVIO MDS","DESVIO MDT", "AREA"]))	
	print (pd.cov())
	print ('')
	print ('------------- CORRELACAO ---------------	')
	print (pd.corr())		
	
