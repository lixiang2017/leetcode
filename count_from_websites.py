#! /usr/bin/python
# TODO
import requests

# US_URL = 'https://leetcode.com/838255715/'
US_URL = 'https://leetcode.com/xiang2022/'
CN_URL = 'https://leetcode-cn.com/u/xiang-lee/'

response = requests.get(US_URL)
print(response)
print(response.content)
