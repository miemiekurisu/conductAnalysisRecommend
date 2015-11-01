import urllib
import urllib2
import json
import math

url = 'http://www.chinawealth.com.cn/lccpAllProJzyServlet.go'
pages_up = 500.0
# Prepare the data
values = {'cpzt' : '02','pagenum':'1'}
opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(),urllib2.HTTPHandler(debuglevel=0),urllib2.HTTPSHandler(debuglevel=0))
postdata = urllib.urlencode(values)
response = opener.open(url, postdata)
data = response.read()
js = json.loads(data.decode('utf-8'))
count = js.get('Count')
all_pg_num = int(math.ceil(count/pages_up))
print '%s,%s'%(count,all_pg_num)