#-*-encoding:utf-8-*-
import sqlite3
import setting
import requiredata as rd
import * from dataObject

insertResStr='''insert into %s (%s) values(%s)'''


def prepare_data():
    reload_db()
    allConductData=rd.queryAllResData(setting.resData,{'cpzt' : '02'})
    conn = sqlite3.connect(setting.dbName)
    cc=conn.cursor()
    abc=''
    for i in range(0,len(allConductData[0].values())):
        abc=abc+"?"
    abc=','.join(abc)
    key = setting.conductField.split(',')
    c = [ tuple(i[t] for t in key) for i in allConductData]
    cc.executemany(insertResStr%(setting.conductTable,setting.conductField,abc),c)
    conn.commit()