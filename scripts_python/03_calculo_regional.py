##############
# Calculo da Regional que a edificacao esta localizda
# autor: Tiago da Costa Norberto
# data  01/08/2018
###

import sys
from osgeo import ogr
daShapefile = 'D:/repositorio_tcc_puc/dados/edificacao_red\EDIFICACAO.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)

daShapefileRegional = 'D:/repositorio_tcc_puc/dados/final/CADASTRO_TECNICO.REGIONAL_area.shp'
driverReg = ogr.GetDriverByName("ESRI Shapefile")
dataSourceRegional = driverReg.Open(daShapefileRegional, 1)

# Check to see if shapefile is found.
if dataSource is None:
    print ('Could not open %s' % (daShapefile))
else:
    layerEdificacao = dataSource.GetLayer()
    featureCount = layerEdificacao.GetFeatureCount()
    print (featureCount)
    
    layerRegional = dataSourceRegional.GetLayer()
    featureCountRegional = layerRegional.GetFeatureCount()
    print (featureCountRegional) 
    
    # adicionar um novo campo para setar o valor da regional
    new_field = ogr.FieldDefn("REGIONAL", ogr.OFTString)
    new_field.SetWidth(50)
    layerEdificacao.CreateField(new_field)
    
    # percorrer todas as edicacaoes
    for featureEdif in layerEdificacao:
        geom = feature.GetGeometryRef()
        
        # fazer o filtro espacial da edificao com a regional
        layerRegional.SetSpatialFilter(geom)
        
        for feature in layerRegional:
            featureEdif.SetField("REGIONAL", feature.GetField("NOME_REGIONAL"))
        

dataSource.Destroy()
dataSourceRegional.Destroy()