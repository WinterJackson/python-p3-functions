#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")

def greet(name): 
    print(f"Hello, {name}!")
greet ("Noreen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    print (num1 + num2)

def halve(number):
    if isinstance (number, (int, float)):
        return (None)
    
    return number / 2

def test_add (num1, num2):
    assert(add(num1, num2) == 100)

test_add (45, 55)