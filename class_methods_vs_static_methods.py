#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tutorial: Class methods vs Static methods in Python

How to use:
- Run: python class_vs_static_tutorial.py
- Read the comments carefully; each section is small and focused.
- Optional: run mypy for typing checks: mypy class_vs_static_tutorial.py

Key takeaways:
- @classmethod receives the class (cls) and is bound to the class, not the instance.
- @staticmethod receives no implicit first argument; it's just a namespaced function.
- Class methods are great for: alternative constructors (factories), class-wide configuration,
  polymorphic constructors (inheritance-aware), and managing class-level caches/registries.
- Static methods are great for: validation helpers, pure utilities logically belonging to the class.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Type, TypeVar, Optional, Any, Iterable
from datetime import date

T = TypeVar("T")


# ========== 1) Minimal difference: instance vs class vs static ==========

class MinimalDemo:
    class_var = 0

    def __init__(self, x: int) -> None:
        self.x = x  # instance attribute

    def instance_method(self) -> int:
        """
        Instance methods receive 'self' as the first argument.
        They can access both instance attributes and class attributes.
        """
        return self.x + MinimalDemo.class_var

    @classmethod
    def class_method(cls) -> int:
        """
        Class methods receive 'cls' (the class object).
        They can read/modify class-level state, and they are inherited polymorphically.
        """
        cls.class_var += 1
        return cls.class_var

    @staticmethod
    def static_method(a: int, b: int) -> int:
        """
        Static methods receive no implicit 'self' or 'cls'.
        Use them for pure utility functions that logically belong to the class's namespace.
        """
        return a + b


# ========== 2) Alternative constructors (factory methods) with @classmethod ==========

@dataclass
class Person:
    name: str
    age: int

    @classmethod
    def from_birth_year(cls: Type[T], name: str, birth_year: int) -> T:
        """
        Factory method: constructs a Person from birth year.
        Using 'cls' makes this inheritance-aware (returns subclass when called on subclass).
        """
        return cls(name=name, age=date.today().year - birth_year)

    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Stateless validation that does not depend on instance or class state.
        Perfect candidate for a static method.
        """
        return age >= 18


# ========== 3) Inheritance: classmethod is polymorphic; staticmethod is not ==========

@dataclass
class Employee(Person):
    employee_id: str = "N/A"

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int, employee_id: str = "N/A") -> "Employee":
        """
        Overrides the factory to include employee_id. If not overridden,
        calling Person.from_birth_year on Employee would still return Employee,
        because factories use 'cls' and are inheritance-aware.
        """
        obj = super().from_birth_year(name, birth_year)  # returns cls(...)
        # 'obj' is already an Employee when called as Employee.from_birth_year
        # but to be explicit, ensure attribute exists:
        if isinstance(obj, Employee):
            obj.employee_id = employee_id
            return obj
        # Fallback if parent returned base instance (uncommon if using 'cls'):
        return cls(name=obj.name, age=obj.age, employee_id=employee_id)

    @staticmethod
    def normalize_id(raw: str) -> str:
        """
        Static utility logically related to Employee, but not needing class/instance state.
        """
        return raw.strip().upper().replace("-", "")


# ========== 4) Class-level caching/registry with @classmethod
