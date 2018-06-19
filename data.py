from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://pqwe:pqe123@ds018238.mlab.com:18238/avidb')
db = client['avidb']
collection = db.userdb

# single_post = {"name":"Satyam","text":"My first document","tags":["mongodb","python","pymongo"]}
multiple_post = [{"user":"abc","password":"123"},{"user":"Avi","password":"7895"},{"user":"zxc","password":"4563"}]

# name = input('Enter Username : ')
# password = input('Enter Password : ')
# l = []
# d = {'user_name':name,'password':password}
# l.append(d)



def insert_single():
    post_id = collection.insert_one(single_post).inserted_id
def insert_multiple():
    post_id = collection.insert_many(multiple_post).inserted_id
def print_previous():
    pprint(collection.find_one())
def fetch_all():
    for post in collection.find():
        pprint(post)
def find_element():
    pprint(collection.find_one({"user":"Avi"}))
try:
#    insert_single()
    #  insert_multiple()
#    print_previous()
#  find_element()
    fetch_all()
except Exception as e:
    print(e)
finally:
    client.close()