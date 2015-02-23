#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import dbf

def codeconv(filename, encoding='utf8'):
    t = dbf.Table(filename)
    print t.codepage
    if not str(t.codepage).startswith(encoding):
        t.open()
        t.codepage = dbf.CodePage(encoding)
        t.close()
        print 'Encoding updated to', t.codepage
    else:
        print 'Encoding not updated'


filenames = ['shp/skorea-provinces-2012.dbf',
             'shp/skorea-municipalities-2012.dbf',
             'shp/skorea-submunicipalities-2012.dbf']

for filename in filenames:
    print filename
    codeconv(filename, 'utf8')
