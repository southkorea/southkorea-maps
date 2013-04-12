#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import urllib
import zipfile
from glob import glob

BASEURL = 'http://www.filefactory.com/file'
BASEPATH = './gadm'
FILEMAP = {
    'png': [('skorea.png','/hfyvqc8b5fh/n/KOR_adm_png')],
    'shp': [('skorea-shp.zip','/2nb1ulzzb92l/n/KOR_adm_zip')],
    'kmz': [('skorea.kmz','/29hktwve5h3r/n/KOR_adm0_kmz'),
            ('skorea-provinces.kmz','/1ugqc403utmn/n/KOR_adm1_kmz'),
            ('skorea-municipalities.kmz','/3o3nktmlobzb/n/KOR_adm2_kmz')],
    'r'  : [('skorea.RData','/3zwuqmw62v2f/n/KOR_adm0_RData'),
            ('skorea-provinces.RData','/181g2vdo0a0f/n/KOR_adm1_RData'),
            ('skorea-municipalities.RData','/vubfyio3upz/n/KOR_adm2_RData')]
    }
NAMEMAP = {
    'KOR_adm0': 'skorea',
    'KOR_adm1': 'skorea-provinces',
    'KOR_adm2': 'skorea-municipalities'
    }

def download(f, opt):
    path = "%s/%s/" % (BASEPATH, opt)
    if not os.path.exists(path):
        os.makedirs(path)

    print "Downloading '%s'..." % f[0]
    urllib.urlretrieve(BASEURL+f[1], path+f[0])

def extract(opt):
    path = '%s/%s/' % (BASEPATH, opt)

    for z in glob(path+'*.zip'):
        print "Extracting '%s'..." % z
        source = zipfile.ZipFile(z, 'r')
        for name in source.namelist():
            source.extract(name, path)
        source.close()
        os.remove(z)

def rename(opt):
    path = '%s/%s/' % (BASEPATH, opt)
    for f in os.listdir(path):
        if f.startswith("KOR_adm"):
            name, ext = os.path.splitext(f)
            os.rename(path+f, path+NAMEMAP[name]+ext)

if __name__=='__main__':
    for opt in FILEMAP:
        for f in FILEMAP[opt]:
            download(f, opt)
            extract(opt)
            rename(opt)
    print "Done."
