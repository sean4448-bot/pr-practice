import sys


def count_stats(text: str) -> dict:
    lines = text.splitlines()
    words = text.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": len(text),
    }


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <file>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        text = f.read()

    stats = count_stats(text)
    print(f"lines: {stats['lines']}")
    print(f"words: {stats['words']}")
    print(f"chars: {stats['chars']}")


if __name__ == "__main__":
    main()
