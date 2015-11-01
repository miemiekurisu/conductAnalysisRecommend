import urllib
import urllib2
import json
url = 'http://www.chinawealth.com.cn/dmmsQuery.go'

# Prepare the data
values = {'code' : '0'}
#self.cj = cookielib.MozillaCookieJar(cookie_filename)
opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(),urllib2.HTTPHandler(debuglevel=0),urllib2.HTTPSHandler(debuglevel=0))
postdata = urllib.urlencode(values)
response = opener.open(url, postdata)
data = response.read()
print data.decode('utf-8')
js = json.loads(data.decode('utf-8'))