# ⚠ STRICT REVIEW MODE

This repository enforces **violation-only reviews**.

AI reviewers:
- MUST NOT suggest fixes
- MUST NOT output improved code
- MUST NOT refactor
- MUST ONLY point out violations

If rules are broken, output is INVALID.

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

## 0.3 Better to Fail Fast
Fail as early as possible when a problem is detected.  
Do not allow the program to continue running in an inconsistent state.

## 0.4 Prefer Composition Over Inheritance
Favor combining small, focused objects rather than relying on complex inheritance chains.  
This results in more flexible, testable, and maintainable designs.

## 0.5 Don’t Write Long Function Names
Function names should be concise and clear.  
Avoid overly long or overly descriptive names that reduce readability.

## 0.6 Keep Parameters Small (3–5 Max)
There is no scientific limit, but aim to use **3–5 parameters at most** to reduce cognitive load and improve cohesion.  
If more parameters are needed, consider grouping them into value objects or configuration classes.

## 0.7 Keep Methods per Class Small (3–5 Max)
There is no scientific limit, but aim for **3–5 methods per class** to maintain cohesion.  
If a class grows too large, consider splitting responsibilities across multiple smaller classes.

## 0.8 Not Everything Should Return a Dictionary
Avoid returning dictionaries for everything, especially for internal function calls.  
Return domain objects, simple types, or clearly structured data when appropriate.

## 0.9 Strict Abstract Usage: Raise `NotImplementedError`
When defining abstract-like methods without using `abc`, always raise `NotImplementedError` to ensure fail-fast consistency.

## 1.1 Never Use “-er” Names
Avoid naming classes with “-er” (e.g., Manager, Handler, Controller).  
These often indicate vague or unclear responsibilities.  
Prefer concrete, domain-driven names.

## 1.2 Make One Constructor Primary
When using alternative constructors (e.g., `@classmethod` factories), ensure only one constructor initializes the main logic.  
Others should delegate to the primary constructor.

## 1.3 Keep Constructors Code-Free
Constructors should only assign values and not contain heavy logic.  
Complex setup should be placed in separate initialization methods or factories.
