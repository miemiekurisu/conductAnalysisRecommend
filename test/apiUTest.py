#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''

import unittest
import api.ConductInfo as conduct

class apiUTest(unittest.TestCase):
    
    def test_one_page(self):
        count,pageData = conduct.getOnePage()
        print count, len(pageData)
        
    def test_all(self):
        data = conduct.getAll()
        print len(data)

if __name__ == '__main__':
    unittest.main()