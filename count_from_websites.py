#! /usr/bin/python
# TODO
import requests

US_URL = 'https://leetcode.com/838255715/'
CN_URL = 'https://leetcode-cn.com/u/xiang-lee/'

res = requests.get(US_URL)
print res
print res.content
