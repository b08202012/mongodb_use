import sqlite3
import pymongo
from bson import ObjectId
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
mydb = myclient["runoobdb"]
#可更改集合名稱
mycol = mydb["user"]
con = sqlite3.connect("pyqum.sqlite")
cur = con.cursor()
#可更改集合名稱
cur.execute("SELECT * FROM user")
col_name_list = [tuple[0] for tuple in cur.description]
data = cur.fetchall()
"""
for i in range(len(data)):
    dic = {}
    for j in range(len(col_name_list)):
        dic[col_name_list[j]] = data[i][j]
    dic["DR"] = 4
    mycol.insert_one(dic)
"""
def id_to_data(a):
    x = mycol.find_one({"_id":ObjectId(a)})
    return x
#print(id_to_data('651132eca3544f5045e1c7fe'))

def condition_to_id(a):
    mybec = mycol.find(a,{"_id":1})
    id_list = []
    for x in mybec:
        id_list.append(x["_id"])
    return id_list
#print(condition_to_id({"instrument":"3"}))
#print(size)
con.close()