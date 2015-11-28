#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''
from math import ceil

from api.utils import post
from setting import baseUrl
from setting import pageUp


def getAll(cpzt='02'):
    param={}
    param['cpzt']=cpzt
    count,resData= getOnePage(cpzt)
    all_pg_num = int(ceil(count/pageUp))
    for i in range(2,all_pg_num+1):
        param['pagenum']=i
        count,pageData = getOnePage(param)
        resData.extend(pageData)
    return resData

def getOnePage(cpzt='02',pagenum=1):
    queryUrl = '%s/lccpAllProJzyServlet.go'%baseUrl
    param = {}
    param['cpzt']=cpzt
    if pagenum:
        param['pagenum']=pagenum
    data =  post(queryUrl, param)
    return data.get('Count'), data.get('List')