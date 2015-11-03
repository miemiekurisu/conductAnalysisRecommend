#-*-encoding:utf-8-*-
from sqlobject import *
import setting
import os

class BankInfo(SQLObject):
    dm = StringCol(length=100)
    ms = StringCol(length=100)

class ConductInfo(SQLObject):
    bqjz=StringCol(length=500)
    cpdjbm=StringCol(length=500)
    cpdm=StringCol(length=500)
    cpfxdj=StringCol(length=500)
    cpid=StringCol(length=500)
    cpjz=StringCol(length=500)
    cplx=StringCol(length=500)
    cplxms=StringCol(length=500)
    cpms=StringCol(length=500)
    cpqsrq=StringCol(length=500)#date
    cpqx=IntCol()#int
    cpsylx=StringCol(length=500)
    cpsylxms=StringCol(length=500)
    cpxsqy=StringCol(length=500)
    cpyjzzrq=StringCol(length=500)#date
    cpztms=StringCol(length=500)
    csjz=StringCol(length=500)
    dqsjsyl=StringCol(length=500)
    fxdjms=StringCol(length=500)
    fxjgdm=StringCol(length=500)
    fxjgms=StringCol(length=500)
    kfzqjsr=StringCol(length=500)
    kfzqqsr=StringCol(length=500)
    mjbz=StringCol(length=500)
    mjjsrq=StringCol(length=500)#date
    mjqsrq=StringCol(length=500)#date
    orderby=StringCol(length=500)
    qdxsje=DecimalCol(size=50,precision=20)#int
    qxms=StringCol(length=500)
    xsqy=StringCol(length=500)
    yjkhzdnsyl=DecimalCol(size=50,precision=20)#double
    yjkhzgnsyl=DecimalCol(size=50,precision=20)#double

class SalesRange(SQLObject):
    cpxsqy = StringCol(length=500)
    cpid = StringCol(length=500)
    
def reload_db():
    db_filename = os.path.abspath(setting.dbName)
    print db_filename
    if os.path.exists(db_filename):
        os.unlink(db_filename)
    connection_string = 'sqlite:' + db_filename
    connection=connectionForURI(connection_string)
    sqlhub.processConnection = connection
    BankInfo.createTable()
    ConductInfo.createTable()
    SalesRange.createTable()
    connection.close()