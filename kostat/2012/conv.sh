#!/bin/bash

TYPES=( provinces municipalities submunicipalities )

KML_SIMPLIFY=0.01
GEOJSON_DECIMALS=3
TOPOJSON_QUANTIFY=100000
TOPOJSON_SIMPLIFY=0.03

for t in "${TYPES[@]}"
do
    echo "[$t]"

    echo "* Generate KML" # for Google Maps
    ogr2ogr -f kml kml/$t.kml shp/$t.shp # however, too dense to upload to Google
    ogr2ogr -f kml -simplify $KML_SIMPLIFY kml/$t-simple.kml shp/$t.shp # creates topology errors

    echo "* Generate GeoJSON"
    rm -f json/$t-geo.json # ERROR 6: The GeoJSON driver does not overwrite existing files
    ogr2ogr -f geojson json/$t-geo.json shp/$t.shp -lco COORDINATE_PRECISION=$GEOJSON_DECIMALS

    echo "* Generate TopoJSON"
    topojson -p -o json/$t-topo.json -- json/$t-geo.json 
    topojson -p -q $TOPOJSON_QUANTIFY --simplify-proportion $TOPOJSON_SIMPLIFY -o json/$t-topo-simple.json -- shp/$t.shp

    echo ""
done

echo "[All]"
echo "* Generate TopoJSON"
topojson -p --shapefile-encoding UTF8 -o json/skorea-topo.json -- shp/provinces.shp shp/municipalities.shp shp/submunicipalities.shp
