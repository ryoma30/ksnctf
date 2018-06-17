#! /usr/bin/env python
# coding: utf-8

import requests
import hashlib


# MD5の計算
def calcMD5(arg):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()

# nonceの取得
def getNonce(url):
    res = requests.get(url)
    return res.headers['WWW-Authenticate'].split(',')[1][8:-1]

# responceの設定
def genResponse(md5_A1, nonce, nc, cnonce, qop, md5_A2):
    return calcMD5( md5_A1 + ':' + 
                    nonce + ':' + 
                    nc + ':' + 
                    cnonce + ':' + 
                    qop + ':' +
                    md5_A2)

# A2のMD5を設定
def genMd5A2(httpMeth, uri):
    A2 = (httpMeth + ':' + uri)
    return calcMD5(A2)

# credentialsの設定
def genAuthCred(username, realm, nonce, uri, algorithm, response, qop, nc, cnonce):
    return  'username=\"' + username  + '\",' +\
            'realm=\"' + realm + '\",' +\
            'nonce=\"' + nonce + '\",' +\
            'uri=\"' + uri + '\",' +\
            'algorithm=\"' + algorithm + '\",' +\
            'response=\"' + response + '\",' +\
            'qop=\"' + qop + '\",' +\
            'nc=\"' + nc + '\",' +\
            'cnonce=\"' + cnonce +'\"'

# Authorizationヘッダの設定
def genAuthHeader(type, credentials):
    return {'Authorization': type + ' ' + credentials}

def main():

    httpMeth = 'GET'            # HTTPメソッド
    type = 'Digest'             # 認証の種類
    username = 'q9'             # ユーザ名
    realm = 'secret'            # ホスト名       
    uri = '/~q9/flag.html'      # URI
    md5_A1 = 'c627e19450db746b739f41b64097d449' # MD5(username:password)
    algorithm = 'MD5'           # ハッシュ計算アルゴリズム
    qop = 'auth'                # uality of protectionq
    nc = '00000001'             # リクエストごとにインクリメントされる値 
    cnonce='9691c249745d94fc'   # クライアントが生成するnonce
    url = 'http://ctfq.sweetduet.info:10080/~q9/flag.html' #URL


    nonce = getNonce(url)               # サーバから取得する値
    md5_A2 = genMd5A2(httpMeth, uri)    # MD5(HTTPメソッド:URI)
    response = genResponse(md5_A1, nonce, nc, cnonce, qop, md5_A2) # クライアントが計算する値  
    credentials = genAuthCred(username, realm, nonce, uri, algorithm, response, qop, nc, cnonce) # 認証情報 
    headers = genAuthHeader(type, credentials) # Authorizationヘッダ

    # GETリクエストの応答
    res = requests.get(url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    main()