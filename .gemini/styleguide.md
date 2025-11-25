# Project Style Guide

## 0.0 Don’t Repeat Yourself (DRY)
Avoid writing the same logic more than once.  
If a piece of code appears multiple times, extract it into a function, class, or utility module.  
Exception: When deliberately testing scenarios that require repetition.

## 0.1 Keep It Simple
Prefer straightforward, readable solutions over overly clever or abstract ones.  
Write code that is easy to understand, easy to debug, and easy to maintain.  
If a simpler approach works, choose it.

## 0.2 Lazy Import
Only import modules when they are needed.  
Avoid top-level imports for rarely used dependencies.  
Use local imports inside functions to improve startup time and reduce overhead.
