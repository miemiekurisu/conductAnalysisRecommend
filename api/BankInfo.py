#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''
from api.utils import post
from setting import baseUrl

def getBanks(code='0'):
    queryUrl = '%s/dmmsQuery.go'%baseUrl
    param = {}
    param['code']=code
    data =  post(queryUrl, param)
    return  data