from .database import emotions_collection

def get_verses_by_emotion(emotion, language):
    result = emotions_collection.find_one({"emotion": emotion})
    if not result:
        return []
    return result.get(language, [])

def add_verse(verse_data):
    emotions_collection.update_one(
        {"emotion": verse_data["emotion"]},
        {"$push": {verse_data["language"]: {"verse": verse_data["verse"], "reference": verse_data["reference"]}}},
        upsert=True
    )
    return {"message": "Verse added successfully!"}
