#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

#############################################################################
##                                                                         ##
## Epochalypse.py --- Utility to convert epoch timestamps                  ##
##                                                                         ##
## Copyright 2016  Pasquale Stirparo, @pstirparo                           ##
## New License is: Apache 2.0                                              ##
##                                                                         ##
#############################################################################

__description__ = 'Epochalypse - time converter utility'
__author__ = 'Pasquale Stirparo, @pstirparo'
__version__ = '0.2'

import sys
import time
from datetime import datetime
import argparse

# The number of seconds between January 1, 1904 and Jan 1, 1970.
HFS_OFFSET = 2082844800

# The number of seconds between January 1, 1970 and January 1, 2001.
COCOA_OFFSET = 978307200

# The difference between Jan 1, 1601 and Jan 1, 1970 in micro seconds
WEBKIT_OFFSET = 11644473600 * 1000000

# The difference between Jan 1, 1601 and Jan 1, 1970 in 100 nano seconds
NTFS_OFFSET = 11644473600 * 10000000

# The difference between Jan 1, 1980 and Jan 1, 1970 in seconds.
FAT_OFFSET = 315532800

# No offset calculation needed for APFS, as represent the number of nano second elapsed since January 1, 1970
# same as standard Unix epoch


def fromEpoch(epoch):
    print('Epoch Time input to be converted: ', epoch)
    try:
        print('Unix:   ' + time.strftime('%Y-%m-%d %H:%M:%S',
            time.gmtime(epoch)) + ' UTC')
    except:
        print('Unix:   -')

    try:
        print('COCOA:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
            time.gmtime(epoch + COCOA_OFFSET)) + ' UTC')
    except:
        print('COCOA:  -')

    try:
        print('FAT:    ' + time.strftime("%Y-%m-%d %H:%M:%S",
            time.gmtime(epoch + FAT_OFFSET)) + ' UTC')
    except:
        print('FAT:    -')

    try:
        print('HFS+:   ' + time.strftime("%Y-%m-%d %H:%M:%S",
            time.gmtime(epoch - HFS_OFFSET)) + ' UTC')
    except:
        print('HFS+:   -')

    try:
        # Webkit timestamp calculation
        wk = datetime.utcfromtimestamp(float(epoch - WEBKIT_OFFSET) / 1000000)
        print('WebKit: ' + wk.isoformat(" ").split(".")[0] + ' UTC')
    except:
        print('WebKit: -')
    try:
        # ntfs time calculation
        ntfs = datetime.utcfromtimestamp(float(epoch - NTFS_OFFSET) / 10000000)
        print('NTFS:   ' + ntfs.isoformat(" ").split(".")[0] + ' UTC')
    except:
        print('NTFS:   -')
    try:
        # new APFS time calculation
        apfs_t = datetime.utcfromtimestamp(float(epoch) / 1000000000)
        print('APFS:   ' + apfs_t.isoformat(" ").split(".")[0] + ' UTC')
    except:
        print('APFS:   -')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--epoch', dest="epoch_input", default=False, help='Epoch time to be converted',
                        metavar='')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    print('\n##########################################################')
    print('#                                                        #')
    print('#    Epochalypse - Epoch timestamp converter utility     #')
    print('#            by Pasquale Stirparo, @pstirparo            #')
    print('#                                                        #')
    print('##########################################################\n')

    if args.epoch_input:
        fromEpoch(int(args.epoch_input))
        print('')

if __name__ == "__main__":
    main()
