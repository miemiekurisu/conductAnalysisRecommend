#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''

import unittest
import api.ConductInfo as conduct
import api.BankInfo as bank
import api.SalesRange as sr

class apiUTest(unittest.TestCase):
    
    def test_one_page(self):
        count,pageData = conduct.getOnePage()
        print count, len(pageData)
        
    def test_all(self):
        data = conduct.getAll()
        print len(data)
        
    def test_bank_getBanks(self):
        data = bank.getBanks()
        print data[0]
    
    def test_sr_query_sales_range(self):
        data = sr.querySalesRange('943032')
        print data[1]
    
if __name__ == '__main__':
    unittest.main()