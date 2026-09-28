"""Минимум списка одним проходом, без вызова min."""

from __future__ import annotations


def list_minimum(items: list) -> object:
    if not items:
        raise ValueError("пустой список")
    smallest = items[0]
    for item in items[1:]:
        if item < smallest:
            smallest = item
    return smallest
