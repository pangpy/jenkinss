# test_calculator.py

import pytest
from calculator import add, subtract


# 测试加法
def test_add():
    assert add(3, 2) == 5  # 正数加法
    assert add(-1, 1) == 0  # 负数与正数加法
    assert add(0, 0) == 0  # 零加零
    assert add(1.5, 2.5) == 4.0  # 浮点数加法


# 测试减法
def test_subtract():
    assert subtract(3, 2) == 1  # 正数减法
    assert subtract(-1, 1) == -2  # 负数减法
    assert subtract(0, 0) == 0  # 零减零
    assert subtract(2.5, 1.5) == 1.0  # 浮点数减法

    # 测试负结果
    assert subtract(2, 5) == -3
    assert subtract(-5, -2) == -3
