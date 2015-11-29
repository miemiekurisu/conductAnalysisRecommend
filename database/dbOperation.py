#-*-encoding:utf-8-*-
'''
Created on 2015年11月25日

@author: chris
'''
from pymongo import MongoClient
from setting import dblink
from setting import dbname
#client = MongoClient(dblink+'/'+dbname)
#db=client[dbname]

#insert or update ConductInfo by cpid
def upsertConductInfo(conductInfo):
    pass
#upsert SalesRange
def upsertSalesRange():
    pass

def updateBankInfo(bankinfos):
    pass