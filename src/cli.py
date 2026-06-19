import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Утилита сканирует папку и показывает структуру проекта."
    )
    parser.add_argument("path", help="Путь к папке для сканирования")
    parser.add_argument(
        "--backup",
        default=None,
        help="Путь к резервной копии для сравнения"
    )
    return parser.parse_args()
