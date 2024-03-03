from pymongo import MongoClient
from pymongo.server_api import ServerApi

try:
    client = MongoClient(
        host=["localhost:27017"],
        username="user",
        password="pass",
    )
except pymongo.errors.ConnectionFailure as e:
    print("Connection error: ", e)
    exit


def print_result(result):
    print("-----Result-----")
    for el in result:
        print(el)
    print("----------------")


db = client.book
while True:
    print("1. Read")
    print("2. Update: age")
    print("3. Update: Add feature")
    print("4. Delete")
    print("5. Add cats")
    print("0. Exit")
    action = input("Select: ")  # Select mode
    if action == "0":  # Exit
        break
    elif action == "1":  # Read Mongo
        name = input("Enter Name: ")
        result = []
        try:
            if name:  # read by Name
                result = db.cats.find({"name": name})
            else:  # read all
                result = db.cats.find({})
            print_result(result)
        except Exception as e:
            print("An exception occurred ::", e)
    elif action == "2":  # update age
        name = input("Enter Name: ")
        if name:  # update by name, no name - no update
            age = input("New age: ")
            try:
                db.cats.update_one({"name": name}, {"$set": {"age": age}})
                result = db.cats.find_one({"name": name})
                print(result)
            except Exception as e:
                print("An exception occurred ::", e)
    elif action == "3":  # add feature by name
        name = input("Enter Name: ")
        if name:
            feature = input("New feature: ")
            try:
                db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
                result = db.cats.find_one({"name": name})
                print(result)
            except Exception as e:
                print("An exception occurred ::", e)
    elif action == "4":  # delete records
        name = input("Enter Name: ")
        try:
            if name:  # delete by name
                db.cats.delete_many({"name": name})
                result = db.cats.find({})
                print_result(result)
            else:  # delete all
                db.cats.delete_many({})
        except Exception as e:
            print("An exception occurred ::", e)
    elif action == "5":  # add demo record
        try:
            result_many = db.cats.insert_many(
                [
                    {
                        "name": "barsik",
                        "age": 3,
                        "features": ["ходить в капці", "дає себе гладити", "рудий"],
                    },
                    {
                        "name": "Lama",
                        "age": 2,
                        "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                    },
                    {
                        "name": "Liza",
                        "age": 4,
                        "features": ["ходить в лоток", "дає себе гладити", "білий"],
                    },
                ]
            )
        except Exception as e:
            print("An exception occurred ::", e)
        result = db.cats.find({})
        print_result(result)
    else:
        print("WRONG COMMAND. TRY AGAIN")
