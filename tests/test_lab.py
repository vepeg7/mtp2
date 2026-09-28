"""Проверки лабораторной №2."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from factorial import factorial
from guess import autoplay, compare_guess
from minimum import list_minimum
from vowels import count_vowels
from words import word_counts

_ROOT = Path(__file__).resolve().parents[1]


def test_count_vowels() -> None:
    assert count_vowels("АеёИоуыэюя") == 10
    assert count_vowels("AeIoUy") == 6
    assert count_vowels("бвг") == 0


def test_list_minimum() -> None:
    assert list_minimum([4, 1, 9, 1]) == 1
    with pytest.raises(ValueError):
        list_minimum([])


def test_factorial() -> None:
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(6) == 720
    with pytest.raises(ValueError):
        factorial(-3)


def test_word_counts() -> None:
    counted = word_counts(_ROOT / "data" / "words.txt")
    assert counted == {"кот": 2, "пёс": 2, "ёлка": 1}


def test_compare_guess() -> None:
    assert compare_guess(10, 3) == "higher"
    assert compare_guess(10, 12) == "lower"
    assert compare_guess(10, 10) == "equal"


def test_autoplay() -> None:
    trace = autoplay(50)
    assert trace[-1][1] == "equal"
    assert {verdict for _, verdict in trace} >= {"higher", "lower", "equal"}
    assert autoplay(1)[-1] == (1, "equal")
    assert autoplay(100)[-1] == (100, "equal")


def test_main_cli() -> None:
    completed = subprocess.run(
        [sys.executable, "main.py"],
        cwd=_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert "120" in completed.stdout
