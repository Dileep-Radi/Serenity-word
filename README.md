Serenity-Word  

**Serenity-Word** is a **Bible-based web application** that gives users Bible verses based on their **emotions** (e.g., fear, joy, sadness, love, hope).  
It uses **FastAPI** as backend, **MongoDB** for storing verses, and a simple **HTML/CSS/JS frontend**.  

---

Features  
- Search Bible verses based on **emotions**  
- Supports **multiple languages** (English & Telugu)  
- Stores and retrieves verses from **MongoDB**  
- Randomly returns a verse if multiple verses are available for an emotion  
- REST API built with **FastAPI**  
- Frontend with **HTML, CSS, and JavaScript**  
- API ready to integrate with **Bible API** (future upgrade for more verses)  

---

# Project Structure  

serenity-word/
│
├── backend/
│ ├── app.py # FastAPI main app
│ ├── models.py # Pydantic models
│ ├── database.py # MongoDB connection
│ ├── crud.py # DB operations (insert/query)
│ ├── requirements.txt # Python dependencies
│
├── frontend/
│ ├── index.html # Frontend UI
│ ├── style.css # Styling
│ ├── script.js # API calls


---

## ⚙️ Installation  

# Clone the repo  
git clone https://github.com/your-username/serenity-word.git
cd serenity-word

# Install Dependencies
pip install -r backend/requirements.txt

# Setup MongoDB

# Run FastAPI server 
cd backend
uvicorn app:app --reload



