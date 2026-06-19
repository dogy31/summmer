import hashlib
import os


def compute_hash(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as file:
        while True:
            chunk = file.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def collect_duplicates(root_path, entries):
    duplicates = {}
    for rel_path, entry_type, size, mtime in entries:
        if entry_type != "FILE":
            continue
        full_path = os.path.join(root_path, rel_path)
        file_hash = compute_hash(full_path)
        duplicates.setdefault(file_hash, []).append(rel_path)
    return duplicates


def print_duplicates(duplicates):
    print("\nГруппы дубликатов:")
    found = False
    for file_hash, paths in duplicates.items():
        if len(paths) < 2:
            continue
        found = True
        print(f"  Хеш {file_hash}:")
        for path in paths:
            print(f"    - {path}")
    if not found:
        print("  Дубликаты не найдены.")
