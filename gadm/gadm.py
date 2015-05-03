#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import urllib
import zipfile
from glob import glob

BASEDIR = './gadm'
FILEMAP = {
    'shp': [('skorea-shp.zip','http://biogeo.ucdavis.edu/data/gadm2/shp/KOR_adm.zip')],
    'kmz': [('skorea.kmz','http://biogeo.ucdavis.edu/data/gadm2/kmz/KOR_adm0.kmz'),
            ('skorea-provinces.kmz','http://biogeo.ucdavis.edu/data/gadm2/kmz/KOR_adm1.kmz'),
            ('skorea-municipalities.kmz','http://biogeo.ucdavis.edu/data/gadm2/kmz/KOR_adm2.kmz')],
    'r'  : [('skorea.RData','http://biogeo.ucdavis.edu/data/gadm2/R/KOR_adm0.RData'),
            ('skorea-provinces.RData','http://biogeo.ucdavis.edu/data/gadm2/R/KOR_adm1.RData'),
            ('skorea-municipalities.RData','http://biogeo.ucdavis.edu/data/gadm2/R/KOR_adm2.RData')]
    }
NAMEMAP = {
    'KOR_adm0': 'skorea',
    'KOR_adm1': 'skorea-provinces',
    'KOR_adm2': 'skorea-municipalities'
    }

def joinpath(pathlist):
    return os.path.sep.join(pathlist)

def download(f, path):
    if not os.path.exists(path):
        os.makedirs(path)

    url, zipped = f[1], joinpath([path, f[0]])
    print "Downloading '%s' to '%s'..." % (url, zipped)
    urllib.urlretrieve(url, zipped)

def extract(f, path):
    zipped = joinpath([path, f[0]])
    print "Extracting '%s'..." % zipped
    source = zipfile.ZipFile(zipped, 'r')
    for name in source.namelist():
        source.extract(name, path)
    source.close()
    os.remove(zipped)

def rename(path):
    for f in os.listdir(path):
        if f.startswith("KOR_adm"):
            name, ext = os.path.splitext(f)
            os.rename('/'.join([path, f]), '/'.join([path, NAMEMAP[name]+ext]))

if __name__=='__main__':
    for ext in FILEMAP:
        path = joinpath([BASEDIR, ext])
        for f in FILEMAP[ext]:
            download(f, path)
            if ext=='shp': extract(f, path)
            rename(path)
    print "Done."
