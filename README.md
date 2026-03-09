# AI-Integrated Coding Challenge Platform

A full-stack web application that dynamically generates personalized coding challenges using OpenAI's GPT. Users can select a difficulty level, receive a unique AI-generated programming question, submit their answer, and receive instant feedback — all within a secure, authenticated environment that tracks their full challenge history.

---

## Project Overview

This platform eliminates the need for a static challenge database entirely. Instead of storing pre-written questions, the application uses an **AI pipeline powered by OpenAI** to generate every challenge dynamically based on the user's chosen difficulty. This means no two challenges are ever the same.

Authentication is handled end-to-end by **Clerk**, which manages user sessions on both the frontend and backend. When a new user registers, a **webhook** automatically syncs their data between Clerk and the local MySQL database — ensuring user identity, challenge history, and daily quotas stay in perfect sync across the entire stack.

On the frontend, routes are protected at a **granular level** using Clerk's `<SignedIn>` and `<SignedOut>` components, meaning unauthenticated users are blocked from accessing any part of the app beyond the login page.

---

## Tech Stack

### Backend
| Tool | Purpose |
|------|---------|
| **FastAPI** | High-performance Python framework for building the REST API |
| **Uvicorn** | ASGI server that runs the FastAPI application |
| **SQLAlchemy** | ORM for defining and interacting with the database using Python instead of raw SQL |
| **MySQL** | Relational database storing challenge attempts, difficulty settings, answers, and corrections |
| **OpenAI API (GPT)** | AI engine that dynamically generates coding questions and explanations |
| **Clerk (Backend)** | JWT token verification to authenticate every incoming API request |
| **Python-Dotenv** | Secure management of environment variables |
| **UV** | Fast Python package manager used instead of pip to manage all dependencies |
| **NGROK** | Tunnels Clerk webhooks to the local development server during development |

### Frontend
| Tool | Purpose |
|------|---------|
| **React + Vite** | High-performance, component-based user interface |
| **React Router DOM** | Client-side navigation between pages without full browser reloads |
| **Clerk React SDK** | Manages authentication state globally and provides pre-built sign-in/sign-up UI |
| **Tailwind CSS** | Modern, responsive layout and styling |

---

## Features & Security

** AI-Generated Challenges**
Challenges are never hard-coded. Every question is generated in real time by OpenAI's GPT based on the user's chosen difficulty, making each session unique.

** Full-Stack Authentication**
Clerk manages the entire authentication flow — sign-up, login, Google Social Auth, and session management. The frontend splits Clerk credentials intentionally: the **Publishable Key** is used in React for the UI, while the **Secret Key** is kept exclusively in the backend `.env` file for JWT validation.

** Webhook Synchronisation**
When a new user registers through Clerk, a webhook automatically fires and syncs the user's data to the local database. This keeps Clerk and the backend in real-time alignment without any manual intervention.

** Route Protection**
Frontend routes are protected at a granular level using Clerk's `<SignedIn>` and `<SignedOut>` components. Unauthenticated users cannot access the challenge generator or history panel.

** Daily Challenge Quota**
The database tracks how many challenges each user has generated per day, enforcing server-side limits to prevent API abuse.

** CORS Middleware**
Configured on the backend to ensure the API exclusively accepts requests from the authorized frontend domain, blocking any unauthorized cross-origin access.

** Environment Security**
All sensitive credentials (OpenAI API key, Clerk Secret Key, database URL) are stored in `.env` files, which are explicitly excluded from version control via `.gitignore`.

---

## Project Structure

```
ai-challenge-platform/
│
├── backend/
│   ├── ai_generator.py       # OpenAI API logic — generates challenges dynamically
│   ├── webhooks.py           # Syncs Clerk user data with the local database in real time
│   ├── challenge.py          # Handles challenge logic — answers, difficulty, corrections
│   ├── models.py             # SQLAlchemy ORM models defining the database schema
│   ├── database.py           # Connects Python to the MySQL database
│   ├── utils.py              # Reusable helper functions shared across the backend
│   ├── server.py             # API entry point — enables CORS, integrates Clerk, connects to React
│   ├── app.py                # Main FastAPI application instance
│   ├── .env                  # Secret keys (excluded from GitHub via .gitignore)
│   └── pyproject.toml        # Lists all backend libraries and dependencies
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx                      # Wraps the entire app in ClerkProvider
│   │   ├── App.jsx                       # Uses <SignedIn> / <SignedOut> for route protection
│   │   ├── ClerkProviderWithRoutes.jsx   # Protects navigation by wrapping React Router
│   │   ├── AuthenticationPage.jsx        # Login and sign-up UI
│   │   ├── ChallengeGenerator.jsx        # Main interface where users interact with challenges
│   │   ├── MCQChallenge.jsx              # Renders Multiple Choice Question challenges
│   │   ├── HistoryPanel.jsx              # Displays the user's past attempts and results
│   │   ├── Layout.jsx                    # Shared navigation bar and footer across all pages
│   │   └── api.js                        # Fetch configuration for all requests to server.py
│   └── vite.config.js
│
├── .gitignore                # Excludes .env, .venv, node_modules from version control
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- MySQL database
- Clerk account — [clerk.com](https://clerk.com)
- OpenAI API key — [platform.openai.com](https://platform.openai.com)
  
---

## What I Learned

- Architecting a **full-stack application** with a fully decoupled React frontend and FastAPI backend
- Building an **AI pipeline** that eliminates static data by generating content dynamically via OpenAI
- Implementing **JWT-based authentication** across both client and server using Clerk
- Setting up **webhooks** for real-time asynchronous communication between third-party services and a local server
- Using **SQLAlchemy ORM** to model and query relational data without writing raw SQL
- Protecting **frontend routes at a granular level** using Clerk's authentication components
- Splitting **API credentials by responsibility** — public key on the frontend, secret key on the backend
- Applying professional **environment security practices** with `.env` files and `.gitignore`

---

## Future Improvements

- [ ] Deploy to cloud (Railway for backend, Vercel for frontend)
- [ ] Add a leaderboard to compare scores across users
- [ ] Support multiple programming languages per challenge
- [ ] Difficulty progression system based on user performance over time
- [ ] Export challenge history as a PDF report

---

## License

This project is open source and available under the [MIT License](LICENSE).
