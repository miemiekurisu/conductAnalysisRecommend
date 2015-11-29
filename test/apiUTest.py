#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''

import unittest
from api.ConductInfo import ConductInfo
from api.BankInfo import BankInfo
from api.SalesRange import SalesRange

class apiUTest(unittest.TestCase):
    
    def test_one_page(self):
        c1 = ConductInfo()
        count,pageData = c1.getOnePage(cpzt='02')
        print "test_one_page:",count, len(pageData)
        print "test_one_page,content",pageData[0].get("cpztms")
        c2 = ConductInfo()
        ct,pd = c2.getOnePage(cpid='917088')
        print "one_record:",ct
        print "one_record,pd",pd
        
    def test_all(self):
        conduct = ConductInfo()
        data = conduct.getAll(cpzt='02')
        print 'test_all:',len(data)
        
    def test_bank_getBanks(self):
        bank = BankInfo()
        data = bank.getBanks()
        print data[0]
    
    def test_sr_query_sales_range(self):
        sr = SalesRange()
        data = sr.querySalesRange('943032')
        print data[1]
    
if __name__ == '__main__':
    unittest.main()