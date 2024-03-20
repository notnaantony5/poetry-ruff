"""Программа."""

import json
from pathlib import Path


def main() -> None:
    """Функия main."""
    path = input("Привет, введи путь к файлу .json")
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        names = json.load(f)
    user_input = input(
        "Введите имя фамилию и возраст через пробел\nИван Иванов 30",
    )
    first_name, last_name, age = user_input.split()
    age = int(age)
    with path.open("w", encoding="utf-8") as f:
        names.append(
            {"first_name": first_name, "last_name": last_name, "age": age},
        )
        json.dump(names, f, ensure_ascii=False, indent=4)
    try:
        pass
    except FileNotFoundError:
        print("првипвпфы")


main()
