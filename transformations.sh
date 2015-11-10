#! /bin/bash

#calculate the grid of lat lng points
python generateData.py

#run the transformations
ogr2ogr -f "ESRI Shapefile" -s_srs EPSG:4326 -t_srs "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +datum=OSGB36 +units=m +no_defs +towgs84=375,-111,431" -overwrite 3param.shp grid.vrt
ogr2ogr -f "ESRI Shapefile" -s_srs EPSG:4326 -t_srs "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +datum=OSGB36 +units=m +no_defs +towgs84=446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894" -overwrite 7param.shp grid.vrt
ogr2ogr -f "ESRI Shapefile" -t_srs "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +datum=OSGB36 +units=m +no_defs +nadgrids=/Users/jonnyhuck/Downloads/ostn02-ntv2-data/OSTN02_NTv2.gsb" -s_srs EPSG:4326 -overwrite ostn02.shp grid.vrt

# render using Mapnik (UK Example)
# nik2img.py OSNT02Blend.xml gb.png -s 27700 -d 700 1300 -e 0 0 700000 1300000 -w pgw

# render using Mapnik (Stornoway Example)
nik2img.py OSNT02Blend.xml gb.png -s 27700 -d 500 500 -e 142500 933000 142600 933100 -w pgw
