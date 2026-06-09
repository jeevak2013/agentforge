from pathlib import Path


def print_clean_tree(directory: Path, prefix: str = ""):
    # Explicitly exclude the clutter folders seen in your image
    exclude = {".venv", ".pytest_cache", ".ruff_cache", ".vscode", ".git"}

    items = sorted(
        [x for x in directory.iterdir() if x.name not in exclude],
        key=lambda x: (x.is_file(), x.name.lower()),
    )

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{item.name}")

        if item.is_dir():
            print_clean_tree(item, prefix + ("    " if is_last else "│   "))


if __name__ == "__main__":
    print_clean_tree(Path("."))
