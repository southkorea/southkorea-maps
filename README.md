South Korea Maps
================

This repo hosts South Korea administrative division geodata in open formats that can be used to build static and interactive maps (e.g. with [D3](http://d3js.org)), and was inspired by [swiss-maps](https://github.com/interactivethings/swiss-maps).

> Maps of Other Countries
- [Swiss](https://github.com/interactivethings/swiss-maps)
- ...

The following formats are available:

- [ESRI Shapefile](http://en.wikipedia.org/wiki/Shapefile)
- [GeoJSON](http://geojson.org) (In preparation)
- [TopoJSON](http://github.com/mbostock/topojson) (In preparation)

## Description

South Korean administrative divisions are consisted of three levels:
- [Provincial level](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Provincial_level_divisions): Special City(특별시), Metropolitan City(광역시), Province(도), Special Self-governing Province(특별자치도), Special Self-governing City(특별자치시)
- [Municipal level](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Municipal_level_divisions): Si (시, city), Gun (군, county), Gu (구, district)
- [Submunicipal level](http://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea#Submunicipal_level_divisions): Eup (읍, town), Myeon (면, township), Dong (동, neighborhood), Ri (리, village)

## Development Notes


### ESRI Shapefile
The ESRI Shapefiles are generated with [QGIS](http://www.qgis.org/).
The [CRS](http://en.wikipedia.org/wiki/Coordinate_reference_system) is set to WGS84.
The simplified shapefiles are generated with [MapShaper](http://mapshaper.com/test/MapShaper.swf), using the Special Visvalingam algorithm with 100% simplification.

### GeoJSON
TBD

### TopoJSON
TBD


## Examples
TBD

## Copyright and License

### Author
[Lucy Park](mailto:lucypark@popong.com), [team POPONG](http://en.popong.com)

### Data Source
Data source for the raw Shapefiles is the [Administrative division geodata for Census (센서스용 행정구역경계), 2011](http://sgis.kostat.go.kr/statbd/statbd_03.vw) provided by [KOSTAT (Statistics Korea)](http://kostat.go.kr).

### License
No license specified by KOSTAT for the raw Shapefiles.
