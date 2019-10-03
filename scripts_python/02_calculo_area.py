##############
# Calculo de area das geometrias de um shape file
# autor: Tiago da Costa Norberto
# data  01/08/2018
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
    new_field = ogr.FieldDefn("AREA", ogr.OFTReal)
    new_field.SetWidth(32)
    new_field.SetPrecision(2) #added line to set precision
    layer.CreateField(new_field)
       
       
    for feature in layer:
        geom = feature.GetGeometryRef()
        area = geom.GetArea()
        feature.SetField("AREA", area)
        layer.SetFeature(feature)
   

dataSource.Destroy()