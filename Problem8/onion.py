#! /usr/bin/env python
# coding: utf-8

import base64
import sys


# Base64で書かれたファイルをオープン
file = open('b64encode.txt')

# ファイルの読み込み
ciph = file.read()
print(ciph)
# 後片付け
file.close()

# できる限りデコード
while True:
    try:
     plain = base64.b64decode(ciph)
     ciph = plain
     print(plain.decode('utf-8'))
    except:
        sys.exit()

