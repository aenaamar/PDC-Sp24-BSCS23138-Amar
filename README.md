Aena Amar-bscs23138

## Project: Building Resilient Distributed Systems

This project demonstrates fault tolerance using a Circuit Breaker pattern in FastAPI.

## How to Run

1. Install dependencies:
pip install fastapi uvicorn

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/llm-no-protection
http://127.0.0.1:8000/llm-protected

## Description

- /llm-no-protection → shows system failure (no fault tolerance)
- /llm-protected → shows Circuit Breaker with fallback response



