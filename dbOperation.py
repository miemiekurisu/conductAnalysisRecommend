#-*-encoding:utf-8-*-
import sqlite3
import setting

createStr='''create table  if not exists %s (%s)'''
dropStr=''
insertResStr='''insert into %s values(%s)'''
delStr=
selectStr=

import requiredata as rd
a=rd.queryAllResData(setting.resData,{'cpzt' : '02'})
conn = sqlite3.connect(setting.dbName)
c=conn.cursor()
abc=''
for i in range(1,len(a[0].values())+1):
     abc=abc+'?'
','.join(abc)
key = ConductInfo.sqlmeta.columns.keys()
c = [ tuple(i[t] for t in key) for i in a]
c.executemany('insert into conduct_info (%s) values(%s)'%(setting.conductField,abc),c)