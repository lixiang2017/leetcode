'''
K -> M
O -> Q
E -> G

In [25]: import string # .ascii_lowercase

In [26]: string.ascii_lowercase
Out[26]: 'abcdefghijklmnopqrstuvwxyz'
'''

import string

hint = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

lower = list(string.ascii_lowercase)
low2 = {ch: lower[(i + 2) % 26] for i, ch in enumerate(lower)}

def decode_hint(hint):
    decode = ''
    for h in hint:
        if h in low2:
            decode += low2[h]
        else:
            decode += h 
    return decode

de = decode_hint(hint)
print(de)

'''
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
'''

'''
http://www.pythonchallenge.com/pc/def/map.html
'''

url = 'pc/def/map.html'
print(decode_hint(url))

'''
re/fgh/ocr.jvon


# wrong
http://www.pythonchallenge.com/re/fgh/ocr.jvon
# right
http://www.pythonchallenge.com/pc/def/ocr.html

recognize the characters. maybe they are in the book,
but MAYBE they are in the page source.

view-source:http://www.pythonchallenge.com/pc/def/ocr.html
F12 -> view page source



http://www.pythonchallenge.com/pc/def/equality.html


To see the solutions to the previous level, replace pc with pcc, i.e. go to: http://www.pythonchallenge.com/pcc/def/equality.html
Join us on IRC: irc.freenode.net #pythonchallenge 


'''




