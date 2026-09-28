"""Частотный словарь по текстовому файлу."""

from __future__ import annotations

import re
from pathlib import Path

# Буква ё вне диапазона а-я, поэтому она указана отдельно.
_TOKEN = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")


def word_counts(path: str | Path) -> dict[str, int]:
    text = Path(path).read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    for match in _TOKEN.finditer(text):
        word = match.group(0).lower()
        counts[word] = counts.get(word, 0) + 1
    return counts
