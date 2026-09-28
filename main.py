"""Короткий прогон заданий второй лабораторной."""

from __future__ import annotations

from pathlib import Path

from factorial import factorial
from guess import autoplay
from minimum import list_minimum
from vowels import count_vowels
from words import word_counts

_ROOT = Path(__file__).resolve().parent


def main() -> None:
    print(f"factorial 5 = {factorial(5)}")
    print(f"factorial 0 = {factorial(0)}")
    phrase = "Егор учит Python и считает ёжика"
    print(f"гласных в фразе: {count_vowels(phrase)}")
    print(f"минимум списка: {list_minimum([4, 1, 9, 1])}")
    print(f"частоты: {word_counts(_ROOT / 'data' / 'words.txt')}")
    print("ходы угадывания 50:")
    for attempt, verdict in autoplay(50):
        print(f"  {attempt} -> {verdict}")


if __name__ == "__main__":
    main()
