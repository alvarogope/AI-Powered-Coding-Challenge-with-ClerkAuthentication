# AI Coding Challenge Platform
 
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![Clerk](https://img.shields.io/badge/Clerk-6C47FF?style=flat&logo=clerk&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
 
A full-stack AI-powered coding challenge platform. Users log in, select a difficulty, and receive a dynamically generated multiple-choice coding challenge — no static database required. Every challenge is unique, produced in real time by an OpenAI pipeline. User sessions, challenge history, and daily quotas are all persisted and tracked.
 
---

## ✨ Features
 
- 🤖 **AI-Generated Challenges** — GPT produces unique coding questions on every request, eliminating the need for a static challenge database
- 🔐 **Clerk Authentication** — Full sign-in/sign-up flow with session management split across frontend and backend
- 📊 **Challenge History** — Each user's past attempts, answers, and results are stored and displayed in a History panel
- ⚡ **Daily Quota System** — Tracks and limits the number of challenges per user per day
- 🛡️ **Route Protection** — Authentication enforced at a granular level on the frontend; protected API endpoints on the backend
- 🔒 **Secure by Design** — API keys stored in `.env` files excluded from version control; CORS middleware restricts requests to the frontend domain only
 
---

## 🏗️ Architecture
 
```
┌─────────────────────┐         ┌──────────────────────┐
│   React (Vite)      │ ──────▶ │   FastAPI (Python)   │
│   Tailwind CSS      │         │   Uvicorn server     │
│   Clerk React SDK   │         │   SQLAlchemy ORM     │
└─────────────────────┘         └──────────┬───────────┘
                                            │
                          ┌─────────────────┼──────────────────┐
                          ▼                 ▼                  ▼
                    OpenAI API         Clerk Webhooks       MySQL DB
                  (challenge gen)    (user session sync)  (persistence)
```
 
---
 
## 🗂️ Project Structure
 
```
ai-coding-challenge-platform/
├── backend/
│   ├── ai_generator.py     # OpenAI API integration — challenge generation logic
│   ├── webhooks.py         # Clerk webhook handler — keeps user sessions in sync
│   ├── challenge.py        # Challenge logic — answers, difficulty, scoring
│   ├── server.py           # Entry point — CORS, Clerk integration, React connection
│   ├── models.py           # SQLAlchemy ORM models
│   ├── database.py         # Database connection
│   ├── utils.py            # Shared utility functions
│   └── app.py              # Application core
├── frontend/
│   ├── ClerkProviderWithRoutes.jsx   # Route protection wrapper
│   ├── AuthenticationPage.jsx        # Sign-in / sign-up UI
│   ├── ChallengeGenerator.jsx        # Main challenge interface
│   ├── MCQChallenge.jsx              # Multiple choice question display
│   ├── HistoryPanel.jsx              # User history view
│   ├── Layout.jsx                    # Navbar and footer
│   ├── api.js                        # Fetch config for backend requests
│   ├── main.jsx                      # App entry — ClerkProvider wrapper
│   └── App.jsx                       # Root component and routing
└── README.md
```
 
---

## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| Frontend | React (Vite), Tailwind CSS, Clerk React SDK |
| Backend | FastAPI, Uvicorn, Python |
| Auth | Clerk (session management, webhooks, route protection) |
| AI | OpenAI GPT (dynamic challenge generation) |
| Database | MySQL, SQLAlchemy ORM |
