# -*-encoding:utf-8-*-
'''
Created on 2015年11月29日

@author: chris
'''
from datetime import datetime as dtt
from pymongo import MongoClient
from setting import dblink
from setting import dbname

class DiffLog():
    def compare(self,dbrecords, netreocrds):
        dbcps = set([i.get('cpid') for i in dbrecords])
        netcps = set([j.get('cpid') for j in netreocrds])
        eq = dbcps.intersection(netcps)
        forrm = dbcps.difference_update(eq)
        foradd = netcps.difference(eq)
        return forrm, foradd
    
    def diffInsert(self,rmlist, inslist):
        client = MongoClient(dblink + '/' + dbname)
        database = client[dbname]
        collection = database['DiffRecord']
        insertRecords = []
        if rmlist:
            insertRecords.extend([{"cpid":r, 'operation':'rm', 'date':dtt.now().strftime('%Y-%m-%d %H:%M:%S')} for r in rmlist])
        if inslist:
            insertRecords.extend([{"cpid":r, 'operation':'insert', 'date':dtt.now().strftime('%Y-%m-%d %H:%M:%S')} for r in inslist])
        collection.insert_many(insertRecords)
        client.close()
    #     collection.remove({cpid:{$in:["917088","942381"]}}'')
