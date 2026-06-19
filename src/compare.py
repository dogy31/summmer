def compare_folders(entries_src, entries_backup, root_src, root_backup):
    src_files = {rel_path: (size, mtime) for rel_path, entry_type, size, mtime in entries_src if entry_type == "FILE"}
    backup_files = {rel_path: (size, mtime) for rel_path, entry_type, size, mtime in entries_backup if entry_type == "FILE"}

    missing = set(src_files.keys()) - set(backup_files.keys())
    extra = set(backup_files.keys()) - set(src_files.keys())
    changed = []

    for path in src_files.keys() & backup_files.keys():
        if src_files[path] != backup_files[path]:
            changed.append(path)

    return {"missing": missing, "extra": extra, "changed": changed}


def print_comparison(comparison):
    print("\nСравнение с резервной копией:")
    missing = comparison["missing"]
    extra = comparison["extra"]
    changed = comparison["changed"]

    if missing:
        print("  Отсутствуют в бэкапе:")
        for path in sorted(missing):
            print(f"    - {path}")
    if extra:
        print("  Лишние в бэкапе:")
        for path in sorted(extra):
            print(f"    - {path}")
    if changed:
        print("  Изменены:")
        for path in sorted(changed):
            print(f"    - {path}")
    if not missing and not extra and not changed:
        print("  Папки идентичны.")
