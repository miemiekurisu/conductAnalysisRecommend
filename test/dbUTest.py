#-*-encoding:utf-8-*-
'''
Created on 2015年11月26日

@author: chris
'''
import unittest
import api.SalesRange as sr
from pymongo import MongoClient
from setting import dblink
from setting import dbname

class dbUtest(unittest.TestCase):
    
    def test_mongo_basic(self):
        data = sr.querySalesRange('943032')
        client = MongoClient(dblink+'/'+dbname)
        database=client[dbname]
        collection = database['SalesRanges']
        collection.insert_many(data)
        print collection.count()
        print collection.find_one()
        client.close()
        
if __name__ == '__main__':
    unittest.main()