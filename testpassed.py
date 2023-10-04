import math

def test_grade():
    grade = 75
    assert grade >= 50

def test_temp():
    celcius = 28
    farenheit = 34
    assert celcius + farenheit == celcius + 34

def test_square():
    h = 10
    w = 10
    area = 100
    assert area == h * w
