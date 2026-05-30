# 🚀 TaskVault — Secure Real-Time Task Management Web App

TaskVault is a modern full-stack task management web application built with **FastAPI**, **Python**, and a lightweight frontend stack using **HTML**, **CSS**, and **JavaScript**. The application focuses on secure authentication, cloud-based database integration, JWT-based authorization, and efficient task management through a clean REST API architecture.

Designed as a backend-focused project, TaskVault demonstrates practical implementation of:

* REST API Development
* JWT Authentication & Authorization
* Secure User Management
* PostgreSQL Database Integration
* CRUD Operations
* Frontend ↔ Backend Communication
* Cloud Deployment & Database Hosting

---

## 🌐 Live Application

🔗 **Live Demo:** [https://taskvault-4.onrender.com]

---

## 📌 Features

### 🔐 Authentication & Authorization

* User Registration
* Secure Login System
* Password Hashing
* JWT Token Authentication
* Protected API Routes
* User Authorization Checks
* Token Verification Middleware
* Token Expiration Handling
* Automatic Re-authentication Requirement after JWT expiration

---

### ✅ Task Management

* Create Tasks
* Update Tasks
* Delete Tasks
* View User-Specific Tasks
* Persistent Database Storage
* Real-Time Task Updates
* Secure Task Ownership Validation

---

### ⚡ Backend Features

* FastAPI-Powered REST APIs
* Modular Project Structure
* Async-Ready Architecture
* Pydantic Data Validation
* JWT Token Generation & Verification
* Database-Driven Operations
* Clean API Design
* Scalable Backend Architecture

---

### 🗄️ Database Features

* PostgreSQL Database Hosted on Render
* Cloud-Based Persistent Storage
* User Account Management
* Task Persistence
* Real-Time Data Synchronization
* Database Administration through pgAdmin
* Secure Database Connectivity

---

### 🎨 Frontend Features

* Responsive User Interface
* Clean Dashboard Design
* HTML5, CSS3 & JavaScript
* Fetch API / AJAX Integration
* Lightweight and Fast User Experience
* Seamless API Communication

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* JWT Authentication
* PostgreSQL
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* Render PostgreSQL
* pgAdmin

### Deployment

* Render

---

## 🔑 Authentication Flow

TaskVault uses **JWT (JSON Web Tokens)** for secure authentication and authorization.

### Authentication Process

1. User creates an account.
2. Password is securely hashed before storage.
3. User logs in with valid credentials.
4. Server generates a JWT access token.
5. Token is attached to protected API requests.
6. FastAPI validates the token before granting access.
7. If the token expires, the user must log in again to obtain a new session token.
8. Unauthorized requests are automatically blocked.

---

## 🗄️ Database Integration

TaskVault uses a cloud-hosted PostgreSQL database for:

* User Data Storage
* Secure Credential Management
* Task Persistence
* Real-Time Task Updates
* Authorization Data Management
* Long-Term Data Reliability

All task operations are dynamically synchronized through FastAPI endpoints and stored securely in Render PostgreSQL.

Database administration, querying, and monitoring can be performed using **pgAdmin**.

---

## 🌍 Deployment

TaskVault is deployed using:

* Render (Backend Hosting)
* Render PostgreSQL (Database Hosting)
* FastAPI ASGI Server

### Production Highlights

* Cloud-Hosted APIs
* Live Database Connectivity
* Public Endpoint Accessibility
* Secure Authentication System
* Scalable Backend Architecture
* Persistent Cloud Storage

---

## 🔒 Security Features

* JWT Authentication
* Password Hashing
* Protected API Routes
* User Authorization Checks
* Token Verification Middleware
* JWT Expiration Handling
* Re-authentication on Session Expiry
* Secure Database Connections

---

## ⭐ Project Goal

The purpose of TaskVault is to build a production-style task management platform while practicing:

* Secure Backend Architecture
* Authentication & Authorization Systems
* REST API Development
* PostgreSQL Database Integration
* Cloud Deployment Workflows
* Frontend/Backend Communication
* Real-World Software Engineering Practices

TaskVault serves as a practical demonstration of building secure, scalable, and database-driven web applications using modern Python backend technologies.

