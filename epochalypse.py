#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

#############################################################################
##                                                                         ##
## Epochalypse.py --- Utility to convert epoch timestamps                  ##
##                                                                         ##
## Copyright 2018  Pasquale Stirparo, @pstirparo                           ##
## New License is: Apache 2.0                                              ##
##                                                                         ##
#############################################################################

__description__ = 'Epochalypse - time converter utility'
__author__ = 'Pasquale Stirparo, @pstirparo'
__version__ = '0.5'

import sys
import time
from datetime import datetime
import argparse

# The number of seconds between January 1, 1904 and Jan 1, 1970.
HFS_OFFSET = 2082844800

# The number of seconds between January 1, 1970 and January 1, 2001.
# Apple Safari also uses Cocoa timestamp
COCOA_OFFSET = 978307200

# The difference between Jan 1, 1601 and Jan 1, 1970 in micro seconds
# WebKit timestamp is used by Google Chrome and Opera
WEBKIT_OFFSET = 11644473600 * 1000000

# The difference between Jan 1, 1601 and Jan 1, 1970 in 100 nano seconds
NTFS_OFFSET = 11644473600 * 10000000

# The difference between Jan 1, 1980 and Jan 1, 1970 in seconds.
FAT_OFFSET = 315532800

# No offset calculation needed for APFS, as represent the number of nano
# second since January 1, 1970 (same as standard Unix epoch)

# No offset calculation needed for FireFox timestamp, as represent the number
# of microseconds since January 1, 1970 (same as standard Unix epoch)


def fromEpoch(epoch):
  print('Epoch Time input to be converted: %.6f' % epoch)
  try:
    print('Unix:    ' + datetime.utcfromtimestamp(epoch).isoformat(" ") + ' UTC')
  except:
    print('Unix:    -')
  try:
    print('COCOA:   ' + datetime.utcfromtimestamp(
        epoch + COCOA_OFFSET).isoformat(" ") + ' UTC')
  except:
    print('COCOA:   -')
  try:
    print('FAT:     ' + datetime.utcfromtimestamp(epoch + FAT_OFFSET).isoformat(
        " ") + ' UTC')
  except:
    print('FAT:     -')
  try:
    print('HFS+:    ' + datetime.utcfromtimestamp(epoch - HFS_OFFSET).isoformat(
        " ") + ' UTC')
  except:
    print('HFS+:    -')
  try:
    # Webkit timestamp calculation
    wk = datetime.utcfromtimestamp(float(epoch - WEBKIT_OFFSET) / 1000000)
    print('WebKit:  ' + wk.isoformat(" ") + ' UTC')
  except:
    print('WebKit:  -')
  try:
    # ntfs time calculation
    ntfs = datetime.utcfromtimestamp(float(epoch - NTFS_OFFSET) / 10000000)
    print('NTFS:    ' + ntfs.isoformat(" ") + ' UTC')
  except:
    print('NTFS:    -')
  try:
    # new APFS time calculation
    apfs = datetime.utcfromtimestamp(float(epoch) / 1000000000)
    print('APFS:    ' + apfs.isoformat(" ") + ' UTC')
  except:
    print('APFS:    -')
  try:
    # Firefox timestamp, number of microseconds since January 1, 1970 UTC
    ff = datetime.utcfromtimestamp(float(epoch) / 1000000)
    print('FireFox: ' + ff.isoformat(" ") + ' UTC')
  except:
    print('FireFox: -')


def fromHex(hextime):
    return(float.fromhex(hextime))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-e', '--epoch', dest="epoch_input", default=False,
      help='Epoch time to be converted',
      metavar='')
  parser.add_argument('-x', '--hex', dest="hexadecimal_input", default=False,
      help='Hexadecimal timemstamp value to be converted',
      metavar='')

  parser.add_argument("-r", "--revhex", action="store_true", default=False,
      help="Reverse hex bytes (for little endian input)")

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
    fromEpoch(float(args.epoch_input))
    print('')
  elif args.hexadecimal_input:
    hex_text = args.hexadecimal_input.replace(' ', '')
    if args.revhex:
      hex_text = hex_text.decode('hex')[::-1].encode('hex')
    epoch = fromHex(hex_text)
    fromEpoch(epoch)
    print('')

if __name__ == "__main__":
  main()
