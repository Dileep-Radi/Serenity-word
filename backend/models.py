from pydantic import BaseModel

class EmotionRequest(BaseModel):
    emotion_text: str
    language: str  # "en" or "te"

class VerseModel(BaseModel):
    emotion: str
    language: str
    verse: str
    reference: str
