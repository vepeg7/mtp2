"""Сравнение попытки и двоичный подбор секрета."""

from __future__ import annotations


def compare_guess(secret: int, guess: int) -> str:
    if guess < secret:
        return "higher"
    if guess > secret:
        return "lower"
    return "equal"


def autoplay(secret: int, low: int = 1, high: int = 100) -> list[tuple[int, str]]:
    # Верхняя середина: иначе секрет 50 угадывается первым же ходом.
    steps: list[tuple[int, str]] = []
    left = low
    right = high
    while left <= right:
        current = (left + right + 1) // 2
        verdict = compare_guess(secret, current)
        steps.append((current, verdict))
        if verdict == "equal":
            break
        if verdict == "higher":
            left = current + 1
        else:
            right = current - 1
    return steps
