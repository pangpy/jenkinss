# test_calculator.py

import pytest
from calculator import app, add, subtract


# 测试加法函数
def test_add():
    assert add(3, 2) == 5  # 正数加法
    assert add(-1, 1) == 0  # 负数与正数加法
    assert add(0, 0) == 0  # 零加零
    assert add(1.5, 2.5) == 4.0  # 浮点数加法


# 测试减法函数
def test_subtract():
    assert subtract(3, 2) == 1  # 正数减法
    assert subtract(-1, 1) == -2  # 负数减法
    assert subtract(0, 0) == 0  # 零减零
    assert subtract(2.5, 1.5) == 1.0  # 浮点数减法

    # 测试负结果
    assert subtract(2, 5) == -3
    assert subtract(-5, -2) == -3


# 测试加法 API
def test_addition_api():
    client = app.test_client()
    response = client.get('/result?a=3&b=2&operation=add')
    assert response.status_code == 200
    assert b'The result is: 5.0' in response.data


# 测试减法 API
def test_subtraction_api():
    client = app.test_client()
    response = client.get('/result?a=3&b=2&operation=subtract')
    assert response.status_code == 200
    assert b'The result is: 1.0' in response.data

    response = client.get('/result?a=2&b=5&operation=subtract')
    assert response.status_code == 200
    assert b'The result is: -3.0' in response.data


# 测试无效的操作
def test_invalid_operation_api():
    client = app.test_client()
    response = client.get('/result?a=3&b=2&operation=divide')
    assert response.status_code == 400
    assert b'Invalid operation' in response.data
