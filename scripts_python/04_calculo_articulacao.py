##############
# Calculo da relaçao a 
# autor: Tiago da Costa Norberto
# data  01/08/2018
###

import sys
from osgeo import ogr
daShapefile = 'D:/repositorio_tcc_puc/dados/final/articulacao/IMAGEM_BH.ARTICUL2.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(daShapefile, 1)

daShapefileArticulacao = 'D:/repositorio_tcc_puc/dados/final/edificacao/EDIFICACAO.EDIFICACAO.shp'
driverReg = ogr.GetDriverByName("ESRI Shapefile")
dataSourceArticulacao = driverReg.Open(daShapefileArticulacao, 1)

# Check to see if shapefile is found.
if dataSource is None:
    print ('Could not open %s' % (daShapefile))
else:
    dataSourceEdificacao = dataSource.GetLayer()
    featureCount = dataSourceEdificacao.GetFeatureCount()
    print (featureCount)
    
    layerArticulacao = dataSourceArticulacao.GetLayer()
    featureCountRegional = layerArticulacao.GetFeatureCount()
    print (featureCountRegional) 
    
    # adicionar um novo campo para setar o valor da regional
    new_field = ogr.FieldDefn("ARTICULACA", ogr.OFTString)
    new_field.SetWidth(200)
    dataSourceEdificacao.CreateField(new_field)
    
    # percorrer todas as edificacaoes
    for featureArticulacao in dataSourceEdificacao:
        geom = featureArticulacao.GetGeometryRef()
        
        # fazer o filtro espacial da edificao com a regional
        layerArticulacao.SetSpatialFilter(geom)
        
        nomeArticulacao = ""
        for feature in layerArticulacao:
            nomeArticulacao = nomeArticulacao+";"+str(feature.GetField("ARTICULACACAO"))
            featureArticulacao.SetField("ARTICULACACAO", nomeArticulacao)
           
dataSource.Destroy()
dataSourceArticulacao.Destroy()