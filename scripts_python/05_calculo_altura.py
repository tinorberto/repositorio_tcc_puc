##############
# Calculo das altura das edificacaoes
# autor: Tiago da Costa Norberto
# data  01/09/2018
###

import sys
from osgeo import ogr
daShapefile = 'D:/repositorio_tcc_puc/dados/edificacao_red\EDIFICACAO.shp'

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)

# Check to see if shapefile is found.
if dataSource is None:
    print ('Nao foi possivel obter o data%s' % (daShapefile))
else:
    print ('Opened %s' % (daShapefile))
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print ("Numero de features enconetradas %d" ,featureCount))
    # ciracao do campo de ALTURA_Moda
	new_field = ogr.FieldDefn("ALTURA_MODA", ogr.OFTReal)
    new_field.SetWidth(32)
    new_field.SetPrecision(2) #added line to set precision
    layer.CreateField(new_field)
	
	# criacao do campo de ALTURA_MEDIA
	new_field = ogr.FieldDefn("ALTURA_MEDIA", ogr.OFTReal)
    new_field.SetWidth(32)
    new_field.SetPrecision(2) #added line to set precision
    layer.CreateField(new_field)
       
    # percorrer todas as features e calcular a difernca das alturas   
    for feature in layer:
        feature.SetField("ALTURA_MODA", ()feature.GetField("MODA_MDS") - feature.GetField("MODA_MDT"))
		feature.SetField("ALTURA_MEDIA", ()feature.GetField("MEDIA_MDS") - feature.GetField("MEDIA_MDT"))
        layer.SetFeature(feature)
  

dataSource.Destroy()