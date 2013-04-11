South Korea Maps
================

This repo hosts South Korea administrative division geodata in open formats that can be used to build static and interactive maps (e.g. with [D3](http://d3js.org)), and was inspired by [swiss-maps](https://github.com/interactivethings/swiss-maps).


## Data Description

### Formats
The following data are available:

<table>
<thead>
    <tr>
        <td>Format \ Source</td>
        <td><a href="http://kostat.go.kr">KOSTAT</a></td>
        <td><a href="http://www.gadm.org">GADM</a></td>
    </tr>
</thead>
<tbody>
    <tr>
        <td><a href="http://en.wikipedia.org/wiki/Shapefile">ESRI Shapefile</a></td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td><a href="http://en.wikipedia.org/wiki/Keyhole_Markup_Language">KML</a></td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td><a href="http://en.wikipedia.org/wiki/Scalable_Vector_Graphics">SVG</a></td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td><a href="http://geojson.org">GeoJSON</a></td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td><a href="http://github.com/mbostock/topojson">TopoJSON</a></td>
        <td>0</td>
        <td>0</td>
    </tr>
</tbody>
</table>

### Levels
South Korean administrative divisions are consisted of three levels:

- [Provinces (시도)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Provincial_level_divisions): Special City(특별시), Metropolitan City(광역시), Province(도), Special Self-governing Province(특별자치도), Special Self-governing City(특별자치시)
- [Municipalities (시군구)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Municipal_level_divisions): Si (시, city), Gun (군, county), Gu (구, district)
- [Submunicipalities (읍면동)](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Submunicipal_level_divisions): Eup (읍, town), Myeon (면, township), Dong (동, neighborhood), Ri (리, village)


## Development Notes

### KOSTAT
#### Shapefile
- Downloaded from [KOSTAT](http://www.gadm.org/country) (March, 2013).
- The [CRS](http://en.wikipedia.org/wiki/Coordinate_reference_system) is set to WGS84.
- Simplified shapefiles are generated with [MapShaper](http://mapshaper.com/test/MapShaper.swf), using the Special Visvalingam algorithm with 100% simplification.
- Projection files were provided [here](http://sgis.kostat.go.kr/contents/support/support_01_closeup.jsp?sgis_board_seq=344&code=N).

#### KML
- Created from shapefiles with `ogr2ogr -f kml [filename].kml [filename].shp`.

#### SVG
- SVGs are generated with QGIS's [SimpleSVG plugin](http://plugins.qgis.org/plugins/simplesvg/).

### GADM
#### Shapefile
- Downloaded from [GADM](http://gadm.org/country) (March 25, 2013).

## Data Sources
Data is acquired from the following sources:

- KOSTAT: [Administrative division geodata for Census (센서스용 행정구역경계), 2011](http://sgis.kostat.go.kr/statbd/statbd_03.vw)
- GADM: [Global administrative areas](http://www.gadm.org/country)


## Copyright and License

### Contributors
[Team POPONG](http://en.popong.com), [Justin Meyers](mailto:justinelliotmeyers@gmail.com)

### License
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a>
