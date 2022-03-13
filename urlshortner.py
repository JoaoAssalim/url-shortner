import clipboard as c
import pyshorteners

def short_url(url):
    s = pyshorteners.Shortener()
    c.copy(s.tinyurl.short(url))

url = input('Enter url to short: ')
short_url(url)
print('URL copied to clipboard! ')
