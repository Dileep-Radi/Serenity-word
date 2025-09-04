from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import random

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb+srv://Dileep:jesussaves@cluster0.3orsxcg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["versefinder"]
emotions_collection = db["emotions"]

# Request model
class EmotionRequest(BaseModel):
    emotion_text: str
    language: str  # "en" or "te"

# Emotion keywords mapping
emotion_map = {
    "sad": "sadness",
    "lonely": "sadness",
    "fear": "fear",
    "happy": "joy",
    "love": "love",
    "hope": "hope",
}

@app.post("/getverse")
def get_verse(req: EmotionRequest):
    # Detect emotion from text
    emotion = "hope"  # default
    for key, value in emotion_map.items():
        if key in req.emotion_text.lower():
            emotion = value
            break

    # Fetch all verses for the detected emotion & language
    verses_cursor = emotions_collection.find({"emotion": emotion})
    verses_list = []
    for doc in verses_cursor:
        if req.language in doc:
            verses_list.append({
                "verse": doc[req.language]["verse"],
                "reference": doc[req.language]["reference"]
            })

    if not verses_list:
        return {"error": "No verses found for this emotion/language"}

    # Pick a random verse
    selected = random.choice(verses_list)
    return {
        "emotion": emotion,
        "verse": selected["verse"],
        "reference": selected["reference"]
    }
