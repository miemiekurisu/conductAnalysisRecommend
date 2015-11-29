#-*-encoding:utf-8-*-
'''
Created on 2015年11月29日

@author: chris
'''
import unittest
from pymongo import MongoClient
from setting import dblink
from setting import dbname
from api.ConductInfo import ConductInfo
from database.DiffLog import DiffLog
class funcUTest(unittest.TestCase):
    
    def test_compare(self):
        ci = ConductInfo()
        df = DiffLog()
        client = MongoClient(dblink+'/'+dbname)
        database=client[dbname]
        collection = database['ConductInfo']
        dbc = collection.find()
        netc = ci.getAll();
        rm,ins = df.compare(dbc, netc)
        print rm,'|',ins
        print df.diffInsert(rm, ins)
        client.close()
        
        
if __name__ == '__main__':
    unittest.main()