from pymongo import MongoClient
uri = "mongodb+srv://manishgrewal018_db_user:Manish018@cluster0.t1cieij.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)