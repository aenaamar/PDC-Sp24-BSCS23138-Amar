from fastapi import FastAPI, Response
import time
from circuit_breaker import CircuitBreaker

app = FastAPI()

cb = CircuitBreaker()

@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "bscs23138"
    return response


def fake_llm_call():
    time.sleep(2)  # simulate delay
    raise Exception("LLM API failed")  # force failure


#  WITHOUT circuit breaker 
@app.get("/llm-no-protection")
def call_llm_bad():
    return {"response": fake_llm_call()}


# WITH circuit breaker 
@app.get("/llm-protected")
def call_llm_good():
    try:
        result = cb.call(fake_llm_call)
        return {"response": result}
    except Exception:
        return {"response": "Fallback: LLM service unavailable"}