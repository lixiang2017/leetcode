'''

You are here!
Your runtime beats 76.53 % of python submissions.
You are here!
Your memory usage beats 93.88 % of python submissions.
'''

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        return longUrl   

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))




class Codec:
    def __init__(self):
        self.cache = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        idx = self.cache.get(longUrl, len(self.cache))
        self.cache[idx] = longUrl
        return str(idx)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.cache[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



'''
You are here!
Your runtime beats 76.53 % of python submissions.
You are here!
Your memory usage beats 45.41 % of python submissions.
'''


import random
class Codec:
    STRING = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hashmap = {}
    BASE = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tag = self.gen_tag()
        self.hashmap[tag] = longUrl
        return self.BASE + tag

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.hashmap[shortUrl[-7:]]
        
    def gen_tag(self):
        tag = self.gen_random_str()
        while tag in self.hashmap:
            tag = self.gen_random_str()
        return tag

    def gen_random_str(self):
        rand_str = ""
        for i in range(7):
            rand_str += self.STRING[random.randint(0, 61)]
        return rand_str
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


