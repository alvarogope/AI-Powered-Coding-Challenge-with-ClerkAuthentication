In this project I developed a Full-Stack AI-Integrate Challenge PLatform that generates coding challenges.
Each challenge is personalized and has a difficulty setting.
Users can log-into their account where it will appear their history of the challenges.
The login is protected by Clerk, that also links the user sessions and the data persistence tracking the challenges.

Tech Stack:
BACKEND
  FastAPI
  Uvicorn to run the FastAPI
  SQLAlchemy
  Python-Dotenv for managing the environment variables
  
FRONTEND
  React (Vite) for the User Interface
  Clerk React SDK that manages the authentication and the UI for sign-in/sign-up
  Tailwind CSS for the layout

Features & Security:
  Full-Stack Auth - Session managed using Clerk on client and server.
  Database - The data storage for the number of challenges, the difficulty chose, the answer given and the correction.
  The API keys that were stored in the .env files were excluded from version control in PyCharm using the .gitignore
  CORSMiddleware - By using this I ensured that the API only accepts the requests from the frontend domains.

Project Files explained:
BACKEND
  server.py - This is the entry point of the API and enables CORSMiddleware, integrates Clerk, and connects with React from the Frontend

  models.py - It uses SQLAlchemy ORM to define the challenges

  database.py - Connects python code to the SQL database

  .env - Contains the Clerk Security Key. This file was excluded from GitHub for security reasons.

  pyproject.toml - Here I list the libraries required to run the backend.

  FRONTEND
  main.jsx - Wraps the entire app in the ClerkProvider
  App.jsx - I use the Clerk UI components using the <SignedIn> and <SignedOut>
