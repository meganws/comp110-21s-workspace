"""Example functions that can be important elsewhere."""

THE_ANSWER: int = 42

def shout(message: str) -> None:
    print(message.upper())


def whisper(message: str) -> None:
    print(message.lower())

if __name__ == "__main__":
    print("helpers.py was run as a module.")
else:
    print(__name__)
    print("helpers.py was imported as a module.")