# 535. Encode and Decode TinyURL
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


class Codec:
    from string import ascii_uppercase, ascii_letters, digits
    from random import choice

    def __init__(self):
        self.map = {}
        self.size = 6
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl):

        # if there is already a mapping return it
        if longUrl in self.map.keys():
            return self.map[longUrl]

        def generate_shortUrl():
            shortUrl = "".join(
                choice(ascii_uppercase + ascii_letters + digits) for _ in range(self.size))
            return shortUrl

        # while the generated short url isn't unique keep generating them
        shortUrl = generate_shortUrl()
        while shortUrl in self.map.values():
            shortUrl = generate_shortUrl()

        # we know its unique so add it to the map
        self.map[longUrl] = shortUrl

        return shortUrl

    def decode(self, shortUrl):
        if shortUrl in self.map.values():
            for k, v in self.map.items():
                if shortUrl == v:
                    return k

        return None
