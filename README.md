South Korea Maps
================

This repo hosts South Korea administrative division geodata in open formats that can be used to build static and interactive maps (e.g. with [D3](http://d3js.org)), and was inspired by [swiss-maps](https://github.com/interactivethings/swiss-maps).


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

- [KOSTAT](http://kostat.go.kr): [Administrative division geodata for Census (센서스용 행정구역경계), 2011](http://sgis.kostat.go.kr/statbd/statbd_03.vw)
- [GADM](http://www.gadm.org): [Global administrative areas](http://www.gadm.org/country)

### Levels
South Korean administrative divisions are consisted of three levels:

- [Provinces (시도)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Provincial_level_divisions): Special City(특별시), Metropolitan City(광역시), Province(도), Special Self-governing Province(특별자치도), Special Self-governing City(특별자치시)
- [Municipalities (시군구)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Municipal_level_divisions): Si (시, city), Gun (군, county), Gu (구, district)
- [Submunicipalities (읍면동)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Submunicipal_level_divisions): Eup (읍, town), Myeon (면, township), Dong (동, neighborhood), Ri (리, village)

### Data
The following data are available.<br>
Numbers are data sizes in MB, in the following order: All, Provinces, Municipalities, Submunicipalities:

<table>
<thead>
    <tr>
        <td>Format \ Source</td>
        <td>KOSTAT</td>
        <td>GADM</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>ESRI Shapefile</td>
        <td>0, 9.7, 19.4, 47.6</td>
        <td>5.5, 5.5, 5.8, 0</td>
    </tr>
    <tr>
        <td>KML/KMZ</td>
        <td>0, 23.7, 47.4, 116.9</td>
        <td>1.5, 1.5, 1.7, 0</td>
    </tr>
    <tr>
        <td>SVG</td>
        <td>0, 0.3, 0.5, 1.5</td>
        <td>0</td>
    </tr>
    <tr>
        <td>GeoJSON</td>
        <td>0</td>
        <td>15.2, 15.4, 16.1, 0</td>
    </tr>
    <tr>
        <td>TopoJSON</td>
        <td>0</td>
        <td>1.5, 1.5, 1.6, 0</td>
    </tr>
    <tr>
        <td>RData</td>
        <td>0</td>
        <td>1.0, 1.0, 1.2, 0</td>
    </tr>
</tbody>
</table>

## Development Notes
### KOSTAT
#### Shapefile
- Downloaded on March, 2013.
- The [CRS](http://en.wikipedia.org/wiki/Coordinate_reference_system) is set to WGS84.
- Projection files were provided [here](http://sgis.kostat.go.kr/contents/support/support_01_closeup.jsp?sgis_board_seq=344&code=N).

#### KML
Created from shapefiles with `ogr2ogr -f kml [filename].kml [filename].shp`.

#### SVG
SVGs are generated with QGIS's [SimpleSVG plugin](http://plugins.qgis.org/plugins/simplesvg/).


### GADM
#### Shapefile, KMZ, RData
To download data files, run:

    make get_gadm

#### GeoJSON
Created from shapefiles with `ogr2ogr -f geojson [filename]-geo.json [filename].shp`.

#### TopoJSON
Created from GeoJSON files with `topojson [filename]-geo.json -o [filename]-topo.json --properties`.


## Copyright and License
### Contributors
[Team POPONG](http://en.popong.com), [Justin Meyers](mailto:justinelliotmeyers@gmail.com)

### License
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a>

- KOSTAT: Free to share or remix.
- GADM:  For non-commercial purposes only. Redistribution not allowed.
