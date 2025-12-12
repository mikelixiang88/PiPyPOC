"""Simple greeting module."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name} testtt!"


def main():
    """Main function for testing."""
    print(greet("PiPA"))


if __name__ == "__main__":
    main()