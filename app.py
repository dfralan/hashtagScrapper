import re
import urllib.parse
import urllib.request

keyHashtag = INSERT_KEYWORD #put the keyword u want
pattern = r'\B(\#[a-zA-Z]+\b)(?!;)'
url = str('https://best-hashtags.com/hashtag/'+ keyHashtag) #or you can put what url u want that contains the hashtags and delete the keyHashtag variable
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = str(response.read())
   hashtags = re.findall(pattern, the_page)
   separator = " "
   hashtagsready = str(separator.join(hashtags[:30]))
