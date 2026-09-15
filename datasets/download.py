"""Загрузка внешних датасетов для лабораторных работ.

Датасеты не хранятся в репозитории (см. .gitignore). Скрипт скачивает файлы
в папку datasets/data/ по списку ниже. Встроенные датасеты (sklearn, seaborn,
keras) загружаются самими библиотеками и здесь не перечислены.

Использование:
    python datasets/download.py
"""

from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

# Реестр внешних датасетов. Для каждого файла можно указать несколько зеркал:
# используется первое доступное.
DATASETS: dict[str, list[str]] = {
    "titanic.csv": [
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    ],
    "heart.csv": [
        "https://raw.githubusercontent.com/amankharwal/Website-data/master/heart.csv",
        "https://raw.githubusercontent.com/sharmaroshan/Heart-UCI-Dataset/master/heart.csv",
    ],
    "airline-passengers.csv": [
        "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv",
    ],
    "mall-customers.csv": [
        "https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2024%20-%20K-Means%20Clustering/Mall_Customers.csv",
    ],
}

HEADERS = {"User-Agent": "Mozilla/5.0 (aiuse-course)"}


def _download(url: str, dest: Path, timeout: int = 60) -> bool:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp, open(dest, "wb") as fh:
            while chunk := resp.read(1 << 16):
                fh.write(chunk)
        return True
    except Exception as exc:  # noqa: BLE001 — сообщаем пользователю и пробуем зеркало
        print(f"    ошибка: {exc}", file=sys.stderr)
        return False


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ok, skipped, failed = 0, 0, 0

    for filename, urls in DATASETS.items():
        dest = DATA_DIR / filename
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[skip]  {filename} (уже загружен)")
            skipped += 1
            continue

        print(f"[get ]  {filename}")
        downloaded = False
        for url in urls:
            if _download(url, dest):
                size_kb = dest.stat().st_size / 1024
                print(f"[ok  ]  {filename} ({size_kb:.1f} КБ)")
                ok += 1
                downloaded = True
                break
        if not downloaded:
            print(f"[fail]  {filename}", file=sys.stderr)
            dest.unlink(missing_ok=True)
            failed += 1

    print(f"\nГотово: загружено {ok}, пропущено {skipped}, ошибок {failed}.")
    print(f"Файлы сохранены в: {DATA_DIR}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
