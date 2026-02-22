import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "ai_agent_db"
COLLECTION_NAME = "interactions"


def _get_collection():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        db = client[DB_NAME]
        return db[COLLECTION_NAME]
    except ConnectionFailure as e:
        print(f"[MEMORY] MongoDB connection failed: {e}")
        return None


def save_interaction(user_query: str, ai_response: str) -> dict:
    """Save a user-agent interaction to MongoDB."""
    print("[MEMORY] Saving interaction to MongoDB...")
    collection = _get_collection()

    if collection is None:
        return {"status": "error", "message": "Database connection failed."}

    document = {
        "user_query": user_query,
        "ai_response": ai_response,
        "timestamp": datetime.datetime.now().isoformat(),
    }
    result = collection.insert_one(document)
    print(f"[MEMORY] Interaction saved with ID: {result.inserted_id}")
    return {"status": "saved", "id": str(result.inserted_id), "timestamp": document["timestamp"]}


def get_last_interaction() -> dict:
    """Retrieve the most recent interaction from MongoDB."""
    print("[MEMORY] Retrieving last interaction from MongoDB...")
    collection = _get_collection()

    if collection is None:
        return {"status": "error", "message": "Database connection failed."}

    document = collection.find_one(sort=[("_id", -1)])

    if document:
        print("[MEMORY] Last interaction found.")
        return {
            "user_query": document["user_query"],
            "ai_response": document["ai_response"],
            "timestamp": document["timestamp"],
        }

    print("[MEMORY] No interactions found.")
    return {"user_query": None, "ai_response": None, "timestamp": None}


if __name__ == "__main__":
    save_interaction("What is AI?", "AI stands for Artificial Intelligence.")
    result = get_last_interaction()
    print(f"[MEMORY] Last interaction: {result}")
