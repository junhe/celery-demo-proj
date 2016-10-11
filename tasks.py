import time

from celeryapp import app

@app.task
def add(x, y):
    time.sleep(1)
    return x + y


@app.task
def mul(x, y):
    time.sleep(1)
    return x * y


@app.task
def xsum(numbers):
    time.sleep(1)
    return sum(numbers)
