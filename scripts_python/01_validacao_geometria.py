##############
# Validação da geometria de um arquivo shaoe file
# autor: Tiago da Costa Norberto
# data  05/08/2018
###

import sys
from osgeo import ogr
daShapefile = 'D:/repositorio_tcc_puc/dados/EDIFICACAO (1)/EDIFICACAO.shp'

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)

# Check to see if shapefile is found.
if dataSource is None:
     print ('Nao foi possivel obter o data%s' % (daShapefile))
else:
    print ('Opened %s' % (daShapefile))
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print ("Numero de features encontrasdas : %d" % (featureCount))
 
    # percorrer todas as geometrias e fazer a validacao        
    for feature in layer:
        geom = feature.GetGeometryRef()
        if  geom.IsValid() != True:
            print (feature.GetField("ID_EDIFICAO")))


dataSource.Destroy()