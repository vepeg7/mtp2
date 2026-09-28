"""Факториал циклом. math.factorial не используется."""

from __future__ import annotations


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("отрицательный аргумент")
    product = 1
    for number in range(2, n + 1):
        product *= number
    return product
