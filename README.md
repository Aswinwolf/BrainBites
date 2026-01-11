# AI Wiki Quiz Generator

An AI-powered web application that generates interactive quizzes from Wikipedia articles using web scraping and Large Language Models.

This project was built as part of the assignment for **DeepKlarity Technologies**.

---

## 🚀 Project Overview

AI Wiki Quiz Generator allows users to:
- Paste a Wikipedia article URL  
- Automatically generate quiz questions using AI  
- Take quizzes with instant scoring  
- View correct answers and explanations  
- Track quiz history  

The system works end-to-end with a **FastAPI backend**, **PostgreSQL database**, and a **React frontend**.

---

## 🛠 Tech Stack

### Frontend
- React  
- Axios  
- CSS  

### Backend
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- BeautifulSoup (for scraping)  
- LangChain  
- Gemini API  

---

## ✨ Features

- Wikipedia article scraping (no Wikipedia API used)  
- AI-based quiz generation  
- Multiple-choice questions  
- Take quiz mode & view answers mode  
- Auto scoring and result summary  
- Quiz history tracking  
- Error handling and loading states  

---

## 📁 Folder Structure

ai-wiki-quiz-generator/
├── backend/
│ ├── app/
│ ├── main.py
│ ├── requirements.txt
├── frontend/
│ ├── src/
│ ├── package.json
├── sample_data/
│ ├── urls.txt
│ ├── artificial_intelligence.json
│ ├── mern_stack.json
│ ├── react.json
├── README.md



---

## ⚙️ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000


cd frontend
npm install
npm start

Frontend runs at:

http://localhost:3000

🔑 Environment Variables

Create a .env file inside the backend folder.

DATABASE_URL=postgresql://username:password@host:port/dbname
GEMINI_API_KEY=your_gemini_api_key_here

🔌 API Endpoints
Method	Endpoint	Description
POST	/generate-quiz	Generate quiz from Wikipedia URL
GET	/history	Get all previously generated quizzes
GET	/quiz/{id}	Get quiz details by ID
▶️ How to Run Locally

Start the backend server

Start the frontend server

Open the app in your browser:

http://localhost:3000


Paste a Wikipedia URL and generate your quiz.

🧪 How to Test
Backend
curl http://127.0.0.1:8000/history
curl http://127.0.0.1:8000/quiz/1

Frontend

Generate a quiz

Attempt the quiz

Submit answers

Check score

Open history tab and view quiz details

🚀 Deployment
Backend → Render

FastAPI app deployed on Render

PostgreSQL database hosted on Render

Environment variables configured in Render dashboard

Frontend → Vercel

React app deployed on Vercel

Backend API base URL configured as environment variable

📸 Screenshots

Add the following screenshots here:

Generate Quiz page (before submit)

Generate Quiz page (after result)

History tab

Quiz details modal

Deployed frontend

Deployed backend API test

🎥 Demo Video

A short screen recording demonstrating:

Quiz generation

Taking the quiz

Viewing history

Deployed application

✅ Final Status

This project is fully functional with:

Working backend

Working frontend

Database integration

AI-powered quiz generation

Deployment completed