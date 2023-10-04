import math

def test_grade():
    grade = 49
    assert grade >= 50

def test_temp():
    celcius = 28
    farenheit = 33
    assert celcius + farenheit == celcius + 34

def test_square():
    h = 10
    w = 10
    area = 99
    assert area == h * w
