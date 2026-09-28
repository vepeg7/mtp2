"""Подсчёт гласных: кириллица и латиница."""

from __future__ import annotations

# аеёиоуыэюя плюс aeiouy; ё входит в набор явно.
_VOWELS = frozenset("аеёиоуыэюяaeiouy")


def count_vowels(text: str) -> int:
    total = 0
    for char in text.lower():
        if char in _VOWELS:
            total += 1
    return total
