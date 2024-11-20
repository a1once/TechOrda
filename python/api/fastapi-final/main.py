from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from starlette.requests import Request
from fastapi.responses import Response

app = FastAPI()
items: List[str] = []

class Item(BaseModel):
    element: str

class Expression(BaseModel):
    expr: str

# Метрики
REQUESTS_TOTAL = Counter('http_requests_total', 'Number of HTTP requests received', ['method', 'endpoint'])
REQUESTS_DURATION = Histogram('http_requests_milliseconds', 'Duration of HTTP requests in milliseconds', ['method', 'endpoint'])
LAST_SUM1N_RESULT = Gauge('last_sum1n', 'Value stores last result of sum1n')
LAST_FIBO_RESULT = Gauge('last_fibo', 'Value stores last result of fibo')
LIST_SIZE = Gauge('list_size', 'Value stores current list size')
LAST_CALCULATOR_RESULT = Gauge('last_calculator', 'Value stores last result of calculator')
CALCULATOR_ERRORS_TOTAL = Counter('errors_calculator_total', 'Number of errors in calculator')

# Middleware для сбора метрик запросов
@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    method = request.method
    endpoint = request.url.path

    # Инкрементируем счетчик запросов
    REQUESTS_TOTAL.labels(method=method, endpoint=endpoint).inc()
    
    # Начинаем измерение времени выполнения запроса
    with REQUESTS_DURATION.labels(method=method, endpoint=endpoint).time():
        response = await call_next(request)

    return response

@app.get("/sum1n/{n}")
async def sum1n(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="n должно быть положительным числом")
    total = sum(range(1, n + 1))
    LAST_SUM1N_RESULT.set(total)  # Обновление метрики
    return {"result": total}

@app.get("/fibo")
async def fibo(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="n должно быть положительным числом")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    LAST_FIBO_RESULT.set(a)  # Обновление метрики
    return {"result": a}

@app.post("/reverse")
async def reverse_string(string: str = Header(...)):
    reversed_str = string[::-1]
    return {"result": reversed_str}

@app.put("/list")
async def add_item(item: Item):
    items.append(item.element)
    LIST_SIZE.set(len(items))  # Обновление метрики
    return {"result": items}

@app.get("/list")
async def get_items():
    return {"result": items}

@app.post("/calculator")
async def calculate(expression: Expression):
    expr = expression.expr
    try:
        num1_str, operator, num2_str = expr.split(',')

        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")

        num1 = float(num1_str)
        num2 = float(num2_str)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = num1 / num2

        LAST_CALCULATOR_RESULT.set(result)  # Обновление метрики
        return {"result": result}

    except ZeroDivisionError:
        CALCULATOR_ERRORS_TOTAL.inc()  # Увеличение счетчика ошибок
        raise HTTPException(status_code=403, detail="zerodiv")
    except Exception:
        CALCULATOR_ERRORS_TOTAL.inc()  # Увеличение счетчика ошибок
        raise HTTPException(status_code=400, detail="invalid")

# Роут для экспорта метрик
@app.get("/metrics")
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)