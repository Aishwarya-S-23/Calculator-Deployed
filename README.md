# Calculator API & Frontend

A full-stack calculator application built using **FastAPI**, **HTML/CSS/JavaScript**, and deployed using **Render** and **Vercel**.

This project was built to deeply understand:

- Frontend ↔ Backend communication
- FastAPI API development
- Expression parsing
- Operator precedence handling
- Recursive bracket evaluation
- Deployment workflows
- Full-stack architecture

---

# Live Demo

## Frontend

[https://your-frontend.vercel.app](https://calculator-deployed-besq.vercel.app/)

---

## Backend API

[https://your-backend.onrender.com
](https://calculator-deployed.onrender.com)
---

# Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)
- Bracket support `()`
- Recursive expression evaluation
- Operator precedence handling
- Responsive calculator UI
- FastAPI backend API
- Real-time frontend-backend integration
- Fully deployed full-stack application

---

# Tech Stack

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

---

## Backend

- FastAPI
- Pydantic
- Python

---

## Deployment

- Vercel (Frontend)
- Render (Backend)

---

# Project Structure

```text
calculator-project/
│
├── backend/
│   ├── main.py
│   ├── calculator.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

# Architecture

```text
Frontend UI (Vercel)
        ↓
Fetch API Request
        ↓
FastAPI Backend (Render)
        ↓
Tokenization
        ↓
Recursive Computation Engine
        ↓
JSON Response
        ↓
Frontend Display Update
```

---

# Backend Logic Flow

## 1. Tokenization

Expression input:

```text
(2+3)*4
```

gets converted into structured tokens:

```python
[
  ('operator', '('),
  ('operand', '2'),
  ('operator', '+'),
  ('operand', '3'),
  ('operator', ')'),
  ('operator', '*'),
  ('operand', '4')
]
```

---

## 2. Recursive Bracket Evaluation

Innermost bracket expressions are recursively solved first.

Example:

```text
(2+3)*4
```

becomes:

```text
5*4
```

then:

```text
20
```

---

## 3. Operator Precedence

The calculator follows standard precedence rules:

| Priority | Operators |
|---|---|
| Highest | `()` |
| Medium | `* / %` |
| Lowest | `+ -` |

---

# API Endpoint

## POST `/result`

### Request Body

```json
{
  "expression": "(2+3)*4"
}
```

### Response

```json
{
  "expression": "(2+3)*4",
  "result": 20
}
```

---

# Local Setup

## Clone Repository

```bash
git clone [https://github.com/your-username/repository-name.git](https://github.com/Aishwarya-S-23/Calculator-Deployed.git)
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Open:

```text
index.html
```

using:

- Browser
- VS Code Live Server

---

# Deployment

## Backend Deployment

Deployed using Render.

Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Frontend Deployment

Deployed using Vercel.

The frontend communicates with the deployed backend using Fetch API.

---

# Learning Outcomes

This project helped in understanding:

- FastAPI fundamentals
- REST APIs
- POST requests
- JSON request/response handling
- Pydantic validation
- CORS handling
- Frontend-backend communication
- Recursive computation logic
- BFS/DSA-oriented logical thinking
- Full-stack deployment workflow

---

# Future Improvements

- Scientific calculator mode
- Keyboard support
- Calculation history
- Authentication
- Dark/Light themes
- AST-based parser
- Better error handling
- Docker deployment
- React frontend version

---

# Author

Aishwarya S
CSE (AI & ML) Student  
