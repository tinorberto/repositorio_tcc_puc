##############
# Calculo de area das geoemtrias de um shape file
# autor: Tiago da Costa Norberto
# data  01/08/2018
###
from osgeo import ogr
from os import remove
from os.path import exists
in_file= "D:/repositorio_tcc_puc/dados/final/EDIFICACAO.EDIFICACAO.shp"
out_file = "D:/repositorio_tcc_puc/dados/final/EDIFICACAO.EDIFICACAO_REDUZIDA.shp"
in_ds = ogr.Open( in_file )
in_lyr = in_ds.GetLayerByIndex(0)
if exists(out_file):
    remove(out_file)

# criacao do driver para leitura e escrita
driver_name = "ESRI Shapefile"
drv = ogr.GetDriverByName( driver_name )
out_ds = drv.CreateDataSource( out_file )


out_lyr = out_ds.CreateLayer(out_file.split(".")[0],proj, ogr.wkbMultiPolygon )

lyr_def = in_lyr.GetLayerDefn ()
for i in range(lyr_def.GetFieldCount()):
    out_lyr.CreateField ( lyr_def.GetFieldDefn(i) )

# criar filtro no campo 
in_lyr.SetAttributeFilter("AREA > 28")

##Writing the features
for feature in in_lyr:
    out_lyr.CreateFeature(feature)
    
in_ds.Destroy()   
out_ds.Destroy()   
