'''
Runtime: 32 ms, faster than 92.74% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 13.8 MB, less than 97.67% of Python3 online submissions for Encode and Decode TinyURL.
'''
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



'''
Runtime: 43 ms, faster than 59.79% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 13.9 MB, less than 28.27% of Python3 online submissions for Encode and Decode TinyURL.
'''
class Codec:
    def __init__(self) -> None:
        self.m = dict()
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = str(self.id) 
        self.m[short] = longUrl
        self.id += 1
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.m[shortUrl]        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



'''
Runtime: 56 ms, faster than 28.02% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 13.9 MB, less than 28.27% of Python3 online submissions for Encode and Decode TinyURL.
'''
from string import ascii_letters, digits
alphanum = ascii_letters + digits
SLOT = 8

class Codec:
    def __init__(self) -> None:
        # shortUrl -> longUrl
        # shortUrl is a string with length of SLOT
        self.short2long = dict()
    
    def _gen_random_str(self) -> str:
        tag = ''
        for _ in range(SLOT):
            ch = random.choice(alphanum)
            tag += ch 
        return tag

    def _gen_tag(self) -> str:
        tag = self._gen_random_str()
        while tag in self.short2long:
            tag = self._gen_random_str()
        return tag
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = self._gen_tag()
        self.short2long[short] = longUrl
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short2long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



'''
Runtime: 90 ms, faster than 5.19% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 13.9 MB, less than 69.91% of Python3 online submissions for Encode and Decode TinyURL.
'''
from string import ascii_letters, digits
alphanum = ascii_letters + digits
LEN = len(alphanum)
SLOT = 8

class Codec:
    def __init__(self) -> None:
        # shortUrl -> longUrl
        # shortUrl is a string with length of SLOT
        self.short2long = dict()
    
    def _gen_random_str(self) -> str:
        chs = []
        for _ in range(SLOT):
            # ch = random.choice(alphanum)
            idx = random.randint(0, LEN - 1)
            chs.append(alphanum[idx])
        return ''.join(chs)
    
    def _gen_tag(self) -> str:
        tag = self._gen_random_str()
        while tag in self.short2long:
            tag = self._gen_random_str()
        return tag
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = self._gen_tag()
        self.short2long[short] = longUrl
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short2long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



