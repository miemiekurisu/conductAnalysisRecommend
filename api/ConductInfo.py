#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''
from math import ceil

from api.utils import post
from setting import baseUrl
from setting import pageUp

class ConductInfo():
    convdict = {
        "yjkhzgnsyl":"预期最高收益",
        "cplx":"", 
        "bqjz":"",
        "mjbz":"募集币种",
        "csjz":"初始净值",
        "kfzqjsr":"最近开放周期结束日",
        "cpqsrq":"产品起始日期",
        "cpjz":"产品净值",
        "yjkhzdnsyl":"预期最低收益",
        "cpfxdj":"风险等级",#01,02,03,04,05
        "qxms":"期限类型",
        "mjqsrq":"募集起始日期",
        "cpztms":"产品状态", #05终止
        "cpyjzzrq":"产品终止日期",
        "cpms":"产品名称",
        "cpid":"产品ID",
        "fxjgms":"发行机构",
        "cpxsqy":"产品销售区域",
        "fxjgdm":"",
        "fxdjms":"风险等级",
        "xsqy":"销售区域",
        "dqsjsyl":"到期实际收益率",
        "orderby":"",
        "kfzqqsr":"最近开放周期起始日",
        "cpsylx":"",
        "cpdm":"",
        "cplxms":"运作模式",
        "cpqx":"实际天数",
        "cpdjbm":"登记编码",
        "mjjsrq":"募集结束日期",
        "qdxsje":"起点销售金额",
        "cpsylxms":"收益类型"
    }
    
    def getAll(self,cpzt='02'):
        count,resData= self.getOnePage(cpzt=cpzt)
        all_pg_num = int(ceil(count/pageUp))
        for i in range(2,all_pg_num+1):
            count,pageData = self.getOnePage(cpzt=cpzt,pagenum=i)
            resData.extend(pageData)
        return resData
    
    def getOnePage(self,cpid = None,cpzt='02',pagenum=1):
        queryUrl = '%s/lccpAllProJzyServlet.go'%baseUrl
        param = {}
        param['cpzt']=cpzt
        if cpid:
            param.clear()
            param['cpid']=cpid
        if pagenum:
            param['pagenum']=pagenum
        data =  post(queryUrl, param)
        return data.get('Count'), data.get('List')