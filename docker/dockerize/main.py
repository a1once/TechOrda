from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List

app = FastAPI()

items: List[str] = []

@app.get("/sum1n/{n}")
async def sum1n(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="n должно быть положительным числом")
    total = sum(range(1, n + 1))
    return {"result": total}

@app.get("/fibo")
async def fibo(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="n должно быть положительным числом")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return {"result": a}

@app.post("/reverse")
async def reverse_string(string: str = Header(...)):
    reversed_str = string[::-1]
    return {"result": reversed_str}

class Item(BaseModel):
    element: str

@app.put("/list")
async def add_item(item: Item):
    items.append(item.element)
    return {"result": items}

@app.get("/list")
async def get_items():
    return {"result": items}

class Expression(BaseModel):
    expr: str

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

        return {"result": result}

    except ZeroDivisionError:
        raise HTTPException(status_code=403, detail="zerodiv")
    except Exception:
        raise HTTPException(status_code=400, detail="invalid")