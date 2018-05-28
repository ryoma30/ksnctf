#! /usr/bin/env python
# coding: UTF-8


def caesar(ciph, key):
    plain = ''
    for c in list(ciph):
        if 'A' <= c <= 'Z':
            # key文字分シフト
            plain += (chr((ord(c) + key - ord('A')) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            # key文字分シフト
            plain += (chr((ord(c) + key - ord('a')) % 26 + ord('a')))
        else:
            # そのまま
            plain += c
    
    return plain

def test_caesar(ciph):
    # 0-25文字文シフトを試す
    for i in range(26):
        print (str(i) + ' ' +caesar(ciph, i))

def main():
    # str = 'EBG KVVV SYNT'
    # test_caesar(str)
    str = 'EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.'
    print(caesar(str, 13))

if __name__ == '__main__':
    main()