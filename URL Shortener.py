#URL Shortener with Python
import pyshorteners
s=pyshorteners.Shortener()
print(s.tinyurl.short('xxxx')) #link in the 'xxxx'
