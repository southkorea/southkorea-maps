South Korea Maps
================

This repo hosts South Korea administrative division geodata in open formats that can be used to build static and interactive maps (e.g. with [D3](http://d3js.org)), and was inspired by [swiss-maps](https://github.com/interactivethings/swiss-maps).

To see maps for Seoul, go to https://github.com/southkorea/seoul-maps

## Description
### Formats
The following formats are available: 
[`shp`](http://en.wikipedia.org/wiki/Shapefile),
[`kml/kmz`](http://en.wikipedia.org/wiki/Keyhole_Markup_Language),
[`svg`](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics), 
[`GeoJSON`](http://geojson.org),
[`TopoJSON`](http://github.com/mbostock/topojson), 
and `RData`.

### Sources 
Data is acquired from the following sources:

- [KOSTAT](http://kostat.go.kr): [Administrative division geodata for Census (센서스용 행정구역경계), 2011|2012](http://sgis.kostat.go.kr/statbd/statbd_03.vw)
- [GADM](http://www.gadm.org): [Global administrative areas](http://www.gadm.org/country)
- [POPONG](http://popong.com): Hand-traced (for production)
- [Wikimedia](http://wikimedia.org): [Administrative divisions map of South Korea](http://commons.wikimedia.org/wiki/File:Administrative_divisions_map_of_South_Korea.svg)

### Levels
South Korean administrative divisions are consisted of three levels:

- [Provinces (시도)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Provincial_level_divisions): Special City(특별시), Metropolitan City(광역시), Province(도), Special Self-governing Province(특별자치도), Special Self-governing City(특별자치시)
- [Municipalities (시군구)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Municipal_level_divisions): Si (시, city), Gun (군, county), Gu (구, district)
- [Submunicipalities (읍면동)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Submunicipal_level_divisions): Eup (읍, town), Myeon (면, township), Dong (동, neighborhood), Ri (리, village)
- Precinct (선거구): TBA

### Data
The following data are available.<br>
Numbers are data sizes in Megabytes in the following order: Country border, Provinces, Municipalities, Submunicipalities.
Numbers in parentheses are simplified versions of each format.

<table>
<thead>
    <tr>
        <th>Format \ Source</th>
        <th>KOSTAT (2012)</th>
        <th>GADM</th>
        <th>POPONG</th>
        <th>Wikimedia</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>ESRI Shapefile</td>
        <td>0, 9.3, 19, 45</td>
        <td>5.5, 5.5, 5.8, 0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>KML/KMZ</td>
        <td>0, 23, 45, 112</td>
        <td>1.5, 1.5, 1.7, 0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>SVG</td>
        <td>0</td>
        <td>0</td>
        <td>0, 0.014, 0, 0</td>
        <td>0, 0, 0.100, 0</td>
    </tr>
    <tr>
        <td>GeoJSON</td>
        <td>0, 12, 24, 79<br>(0, 0.28, 0.62, 0, 0)</td>
        <td>15, 15, 16, 0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>TopoJSON</td>
        <td>0, 0.9, 1.5, 4.9<br>(0, 0.06, 0.14, 0, 0)</td>
        <td>1.5, 1.5, 1.6, 0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>RData</td>
        <td>0</td>
        <td>1.0, 1.0, 1.2, 0</td>
        <td>0</td>
        <td>0</td>
    </tr>
</tbody>
</table>


## Development Notes

### Requirements

    brew install gdal
    npm install -g topojson

### KOSTAT (2012)
1. [Download Shapefiles](http://sgis.kostat.go.kr/statbd/statbd_03.vw)
    - Projection files are provided [here](http://sgis.kostat.go.kr/contents/support/support_01_closeup.jsp?sgis_board_seq=344&code=N). Otherwise, copy the snippet below and save to a separate `prj` file having the same name as the `shp` file.

            PROJCS["Bessel_1841_Transverse_Mercator",GEOGCS["GCS_Bessel_1841",DATUM["D_Bessel_1841",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",200000.0],PARAMETER["False_Northing",500000.0],PARAMETER["Central_Meridian",127.0028902777778],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",38.0],UNIT["Meter",1.0]]
        - CRS: Korean 1985 / Modified Central, EPSG:5174
        - Data encoding: EUC-KR
    - Downloaded dates

        - 2011 version: Downloaded on Mar 2013.
        - 2012 version: Downloaded on Feb 2015.
1. Download and install [QGIS](http://qgis.org). With QGIS, 1) Change layer encoding from UTF-8 to EUC-KR, then 2) load each `shp` file and `save as`, in order to convert CRS and data encoding as shown in the image below.

    <img src="static/saveas.png" width="300px">

    - Change [CRS](http://en.wikipedia.org/wiki/Coordinate_reference_system) from [Korean 1985 / Modified Central, EPSG:5174](http://epsg.io/5174) to [WGS84, EPSG:4326](http://epsg.io/4326)
    - Change data encoding from System to UTF8

1. Change `dbf` codebooks (encodings)

        cd kostat/2012
        ./conv.py

1. Convert `shp` to KML, GeoJSON, TopoJSON

        cd kostat/2012
        ./conv.sh

1. Simplify `GeoJSON`s with http://mapshaper.org/ (with Visvalingam / weighted area, 1% simplification)


### GADM
#### Shapefile, KMZ, RData
To download data files, run:

    make get_gadm

#### GeoJSON
Created from shapefiles with `ogr2ogr -f geojson [filename]-geo.json [filename].shp`.

#### TopoJSON
Created from GeoJSON files with `topojson [filename]-geo.json -o [filename]-topo.json --properties`.

### Wikimedia
#### SVG
To download file, run:

    wget http://upload.wikimedia.org/wikipedia/commons/7/77/Administrative_divisions_map_of_South_Korea.svg

## Examples
- [우리나라 시군구별 인구밀도 시각화 (KOSTAT TopoJSON, 2012)](http://bl.ocks.org/e9t/55699e9fa8c3eb7fe40c)<br><img src="static/choropleth.png" width="200px">
- [우리나라 도시별 인구수 시각화 (KOSTAT TopoJSON, 2012)](http://bl.ocks.org/e9t/826b20ae75b331f56b4e)<br><img src="static/bubble.png" width="200px">
- [시도 시각화 (POPONG SVG)](http://bl.ocks.org/e9t/5712545)
- [시도 시각화 (GADM TopoJSON)](http://bl.ocks.org/e9t/5409484)
- [시군구 시각화 (GADM TopoJSON)](http://bl.ocks.org/e9t/5409518)
- ...add yours to this list!

## Copyright and License
### Contributors
- Lucy Park ([Team POPONG](/teampopong))
- [Justin Meyers](mailto:justinelliotmeyers@gmail.com)

### License
- KOSTAT: Free to share or remix.
- GADM:  For non-commercial purposes only. Redistribution not allowed.
- POPONG: <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/80x15.png" /></a>
- Wikimedia: [GNU 1.2+](http://commons.wikimedia.org/wiki/File:Administrative_divisions_map_of_South_Korea.svg#Licensing)

