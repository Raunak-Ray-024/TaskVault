🚀 TaskVault — Secure Real-Time Task Management Web App

TaskVault is a modern full-stack task management web application built with FastAPI, Python, and a lightweight frontend stack using HTML, CSS, and JavaScript.
The application focuses on secure authentication, real-time database-driven task storage, JWT-based authorization, and clean API architecture.

Designed as a backend-focused project, TaskVault demonstrates practical implementation of:

REST API development,
JWT authentication,
User authorization workflows,
Database integration,
CRUD task management,
Frontend ↔ Backend integration

Cloud deployment using Render
🌐 Live Application
🔗 Live Demo

Render deployment link

📌 Features
🔐 Authentication & Authorization
User Registration,
Secure Login System,
Password hashing,
JWT Token Authentication,
Protected API routes,
Authorization before task access

✅ Task Management
Create Tasks,
Update Tasks,
Delete Tasks,
View User-Specific Tasks,
Persistent database storage,
Real-time data handling through backend APIs

⚡ Backend Features
FastAPI-powered REST APIs,
Modular API structure,
Async-ready architecture,
Pydantic validation,
Database integration,
Secure token generation using JWT

🎨 Frontend Features
Responsive UI,
Clean dashboard design,
HTML/CSS/JavaScript frontend,
API integration using Fetch/AJAX,
Simple and lightweight UX,

🛠️ Tech Stack
Backend,
Python,
FastAPI,
JWT Authentication,
SQL Database,
Uvicorn,
Frontend,
HTML5,
CSS3,
JavaScript

Deployment
Render

🔑 Authentication Flow
TaskVault uses JWT (JSON Web Tokens) for secure authentication.
Authentication Process,
User creates an account,
Password gets hashed before storage,
User logs in,
Server generates JWT token,
Token is attached to protected requests,
FastAPI validates token before allowing access,

🗄️ Database Integration
The application uses a connected database for:
User data storage,
Task persistence,
Real-time task updates,
Secure account management,
All task operations are dynamically synced through FastAPI endpoints.

🌍 Deployment
TaskVault is deployed using:
Render (Backend Hosting),
FastAPI ASGI Server,
Production Highlights,
Cloud-hosted APIs,
Live database connectivity,
Public endpoint accessibility,
Scalable backend architecture

🔒 Security Features
JWT Authentication,
Password Hashing,
Protected Routes,
User Authorization Checks,
Token Verification Middleware

⭐ Project Goal
The purpose of TaskVault is to build a production-style task management platform while practicing:
Secure backend architecture
Authentication systems
REST API development
Database integration
Deployment workflows
Frontend/backend communication
