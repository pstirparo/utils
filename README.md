# utils
DFIR utilities

## ACH_template-v0.4.xlsx
I have moved all CTI related material under https://github.com/pstirparo/threatintel-resources, check that out!

## Epochalypse
There is the standard, official Epoch time (the Unix/POSIX one, seconds elapsed since 1 Jan 1970), and there are "other epoch" type of time (because, why not?). Epochalypse is a python script that receives a generic timestamp as input and converts it in several known common formats. In the latest version it supports also timestamps in hexadecimal value as input.
Sample output and currently supported formats below:
```
$ python3 epochalypse.py --help
usage: epochalypse.py [-h] [-e timestamp] [-r] [-x hex_timestamp] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -e timestamp, --epoch timestamp
                        Epoch time to be converted.
  -r, --revhex          Reverse hex bytes (for little endian input), use it together with -x.
  -x hex_timestamp, --hex hex_timestamp
                        Hexadecimal timemstamp value to be converted.
  -v, --version         show program's version number and exit


$ python3 epochalypse.py -e 547120509.243697

Epoch Time input to be converted: 547120509.243697
Unix:    1987-05-04 09:55:09.243697 UTC
COCOA:   2018-05-04 09:55:09.243697 UTC
FAT:     1997-05-03 09:55:09.243697 UTC
HFS+:    1921-05-03 09:55:09.243697 UTC
WebKit:  1601-01-01 00:09:07.120510 UTC
NTFS:    1601-01-01 00:00:54.712051 UTC
APFS:    1970-01-01 00:00:00.547121 UTC
FireFox: 1970-01-01 00:09:07.120509 UTC
```
