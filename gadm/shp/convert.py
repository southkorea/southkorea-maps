#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
import csv
import glob

def sanitize(item):
    item = re.sub(r'<U\+(\w+)>', lambda m: unichr(int(m.group(1), 16)), item)
    item = item.replace(' ', '')

    if not isinstance(item, unicode):
        item = unicode(item.decode('utf-8'))

    return item

def read_data(infile):
    data = []
    with open(infile, 'r') as f:
        csvreader = csv.reader(f, delimiter=',', quotechar='"')
        for row in csvreader:
            data.append(sanitize(item) for item in row)

    return data

def write_data(data, outfile):
    with open(outfile, 'w') as f:
        for row in data:
            f.write(','.join(row).encode('utf-8'))
            f.write('\n')

if __name__=='__main__':

    infiles = glob.glob('*.csv')

    for infile in infiles:
        data = read_data(infile)
        outfile = infile.split('.')[0] + '-re.csv'
        write_data(data, outfile)
        print 'Data written to ' + outfile

    print 'Done.'
