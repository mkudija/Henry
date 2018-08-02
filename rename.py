#!/usr/bin/python
from PIL import Image
import sys
import time
from os import path
import os
import shutil
from optparse import OptionParser

def main():
        optParser = OptionParser("usage: %prog [options] images... ")
        optParser.add_option("-p","--prefix",help="New File Prefix Date Format",action="store",type="string",dest="dateFormat", default="%Y-%m-%d_")
        optParser.add_option("-d","--dry",help="Only show the rename, NO MOVE WILL BE PERFORMED",action="store_true",dest='dry')
        (options,args) = optParser.parse_args(sys.argv)
        dateFormat = options.dateFormat
        dry = options.dry

        for imagePath in args[1:]:
                try:
                        img = Image.open(imagePath)
                        exif_data = img._getexif()
                        strImageDate = exif_data[306]
                        imageDate = time.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
                        newFileName = time.strftime(dateFormat,imageDate)+path.basename(imagePath)
                        newPath = path.dirname(imagePath)+os.sep+newFileName
                        if dry:
                                print (imagePath +" -> "+newPath)
                        else:
                                shutil.move(imagePath,newPath)
                except IOError:
                        print("File " +imagePath + "not found")
                except TypeError:
                        print("No EXIF date Information found for file:"+imagePath)

if __name__=='__main__':
        main()