from pymongo import MongoClient

# Replace <username> and <password> with your MongoDB credentials
client = MongoClient("mongodb+srv://<username>:<db_password>@cluster0.3orsxcg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["versefinder"]
emotions_collection = db["emotions"]
