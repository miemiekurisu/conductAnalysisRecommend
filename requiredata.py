#-*-encoding:utf-8-*-
import urllib
import urllib2
import json
import math
import setting
import aspect

def queryBankInfo(queryUrl,param):
    return dataReq(queryUrl,param)
    
    
#{'cpzt' : '02','pagenum':'1'}
def queryAllResData(queryUrl,param):
    param['pagenum']=1
    firstpage = dataReq(queryUrl,param)
    resData = firstpage.get('List')
    count = firstpage.get('Count')
    all_pg_num = int(math.ceil(count/setting.pageUp))
    print "page number:",all_pg_num
    for i in range(2,all_pg_num+1):
        pageData = queryResDataPage(queryUrl,param,i)
        resData.extend(pageData.get('List'))
    return resData

def queryResDataPage(queryUrl,param,pageNumber):
    param['pagenum']=pageNumber
    return dataReq(queryUrl,param)

def querySalesRange(cpid):
    rangeList = dataReq(setting.saleRange,{'cpid':cpid}).get('List')
    if rangeList[0]!=None:
        resList = []
        for i in rangeList:
            resList.append((cpid,i.get('cpxsqy')))
        return resList
    else:
        return None

def dataReq(queryUrl,param):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(),urllib2.HTTPHandler(debuglevel=0),urllib2.HTTPSHandler(debuglevel=0))
    postdata = urllib.urlencode(param)
    response = opener.open(queryUrl, postdata)
    data = response.read()
    opener.close()
    return json.loads(data.decode('utf-8'))