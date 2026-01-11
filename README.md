BrainBites
📌 Project Overview

BrainBites is a full-stack web application that takes a Wikipedia article URL as input, scrapes the content, and automatically generates a quiz using a Large Language Model (LLM).
The system stores all generated quizzes in a database and allows users to view previous quizzes through a clean, tab-based interface.

This project is built as part of the DeepKlarity Technologies technical assignment.

🌐 Live Application Links

Frontend (Vercel):
👉 https://brain-bites-three.vercel.app/

Backend (Render):
👉 https://brainbites.onrender.com/

🛠 Tech Stack
Backend

Python – FastAPI

Database – PostgreSQL

Scraping – BeautifulSoup

LLM Integration – LangChain + Gemini (Free Tier)

Frontend

React.js

CSS (clean, minimal UI)

Deployment

Backend – Render

Frontend – Vercel

✨ Features

Accepts any valid Wikipedia article URL

Scrapes:

Title

Summary

Key sections

Generates:

5–10 quiz questions

4 options per question

Correct answer

Difficulty level

Short explanation

Related Wikipedia topics

Stores all data in PostgreSQL

Two-tab UI:

Generate Quiz

Past Quizzes (History)

Modal view for quiz details

Error handling for:

Invalid URLs

Network failures

Missing content

📂 Folder Structure
ai-wiki-quiz-generator/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── database.py
│   ├── models.py
│   ├── services/
│   │   ├── scraper.py
│   │   └── llm_service.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│
├── sample_data/
│   ├── urls.txt
│   ├── alan_turing.json
│   └── artificial_intelligence.json
│
├── README.md
└── .gitignore

⚙️ Backend Setup
1. Create virtual environment
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Environment variables

Create a .env file in backend/:

DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db
GEMINI_API_KEY=your_gemini_api_key_here

4. Run backend
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

⚛️ Frontend Setup
1. Install dependencies
cd frontend
npm install

2. Configure API base URL

Create .env in frontend/:

VITE_API_BASE_URL=http://127.0.0.1:8000

3. Run frontend
npm run dev


Frontend runs at:

http://localhost:5173

🔌 API Endpoints
1. Generate Quiz

POST /generate-quiz

Request:

{
  "url": "https://en.wikipedia.org/wiki/Alan_Turing",
  "num_questions": 5
}


Response:

{
  "quiz_id": 1,
  "quiz_title": "Alan Turing Quiz",
  "questions": [...]
}

2. Get History

GET /history

Response:

[
  {
    "quiz_id": 1,
    "quiz_title": "Alan Turing Quiz",
    "article_title": "Alan Turing"
  }
]

3. Get Quiz by ID

GET /quiz/{id}

Response:

{
  "quiz_id": 1,
  "quiz_title": "Alan Turing Quiz",
  "questions": [...]
}

🧪 How to Test (Using Live App)

Open the frontend:
👉 https://brain-bites-three.vercel.app/

Go to Generate Quiz tab

Enter a Wikipedia URL (example):

https://en.wikipedia.org/wiki/Artificial_intelligence


Click Generate Quiz

View quiz results

Go to Past Quizzes tab

Click Details to view saved quizzes


🚀 Deployment
Backend → Render

Push backend to GitHub

Create new Web Service in Render

Connect repository

Set:

Build command: pip install -r requirements.txt

Start command:

uvicorn main:app --host 0.0.0.0 --port 10000


Add environment variables:

DATABASE_URL

GEMINI_API_KEY

Deploy and test:

https://brainbites.onrender.com/docs

Frontend → Vercel

Push frontend to GitHub

Import project in Vercel

Add environment variable:

VITE_API_BASE_URL=https://brainbites.onrender.com


Deploy and test:

https://brain-bites-three.vercel.app/

🧠 LangChain Prompt Templates
Quiz Generation Prompt
You are an expert quiz generator.
Using the given Wikipedia article content, create 5–10 quiz questions.

Each question must include:
- question text
- 4 options
- correct answer
- difficulty (easy/medium/hard)
- short explanation
- related topics

Return ONLY valid JSON.
Do not include any extra text.

Related Topics Prompt
From the article content, suggest 5 related Wikipedia topics
for further reading.

Return as a JSON array of strings only.

📋 Final Submission Checklist

 Backend working locally

 Frontend working locally

 Database connected

 sample_data folder added

 README completed

 Screenshots captured

 Screen recording done

 GitHub repo updated

 Deployed links tested

 Final links submitted

👨‍💻 Author

Aswin Siva
BrainBites – DeepKlarity Technologies Assignment
