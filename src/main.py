#!/usr/bin/env python3
import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Утилита сканирует папку и показывает структуру проекта."
    )
    parser.add_argument("path", help="Путь к папке для сканирования")
    return parser.parse_args()


def collect_structure(root_path):
    entries = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        rel_dir = os.path.relpath(dirpath, root_path)
        if rel_dir == ".":
            rel_dir = ""
        for dirname in sorted(dirnames):
            entries.append((os.path.join(rel_dir, dirname), "DIR"))
        for filename in sorted(filenames):
            entries.append((os.path.join(rel_dir, filename), "FILE"))
    return entries


def print_structure(root_path, entries):
    print(f"Сканируемая папка: {root_path}")
    print("Структура проекта:")
    if not entries:
        print("  (папка пуста)")
        return
    for rel_path, entry_type in entries:
        if not rel_path:
            continue
        print(f"  [{entry_type}] {rel_path}")


def main():
    args = parse_args()
    path = args.path

    if not os.path.exists(path):
        print(f"Ошибка: путь не найден: {path}", file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(path):
        print(f"Ошибка: указанный путь не папка: {path}", file=sys.stderr)
        sys.exit(1)

    root_path = os.path.abspath(path)
    entries = collect_structure(root_path)
    print_structure(root_path, entries)


if __name__ == "__main__":
    main()
