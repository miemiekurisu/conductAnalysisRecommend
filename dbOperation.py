#-*-encoding:utf-8-*-
import sqlite3
import setting
import requiredata as rd
from dataObject import * 
from multiprocessing.dummy import Pool as ThreadPool 
insertResStr='''insert into %s (%s) values(%s)'''


def prepare_data():
    reload_db()
    allConductData=rd.queryAllResData(setting.resData,{'cpzt' : '02'})
    conn = sqlite3.connect(setting.dbName)
    cc=conn.cursor()
    magicq=''
    for i in range(0,len(allConductData[0].values())):
        magicq=magicq+"?"
    magicq=','.join(magicq)
    key = setting.conductField.split(',')
    c = [ tuple(i[t] for t in key) for i in allConductData]
    cc.executemany(insertResStr%(setting.conductTable,setting.conductField,magicq),c)
    conn.commit()
    sales_ranges = query_sales_range(query_cpids())
    cc.executemany(insertResStr%(setting.salesRangeTable,setting.salesRangeField,'?,?'),sales_ranges)
    conn.commit()
    conn.close()

def query_cpids():
    conn = sqlite3.connect(setting.dbName)
    cc=conn.cursor()
    cc.execute('select cpid from conduct_info')
    cpids = [i[0] for i in cc.fetchall()]
    conn.close()
    return cpids
    
def query_sales_range(cpid_list):
    pool = ThreadPool(40)
    try:
        rt = pool.map(rd.querySalesRange,cpid_list)
        rt_list = []
        for i in rt:
            rt_list.extend(i)
        return rt_list
    finally:
        pool.close()
