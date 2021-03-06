#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''
from api.utils import post
from setting import baseUrl

class SalesRange():
    
    salesDict = {'cpid':'产品ID','cpxsqy':'产品销售区域'}
    
    def querySalesRange(self,cpid=None,pagenum=1):
        assert cpid != None
        param = {}
        param['cpid'] = cpid
        if pagenum:
            param['pagenum']=pagenum
        queryUrl = '%s/cpxsqyQuery.go'%baseUrl
        data = post(queryUrl,param)
        rangeList = data.get('List')
        if rangeList[0]!=None:
            return [{'cpid':cpid,'cpxsqy':i.get('cpxsqy')} for i in rangeList]
        else:
            return None