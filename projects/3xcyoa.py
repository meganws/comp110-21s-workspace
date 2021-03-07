"""Choose your own adventure: Heads or tails!"""
__author__ = "730388741"

from random import randint

points: int = 0
player: str = str("Me")
hate: str = str("Me")
choice: str = str("One")
total: int = 0

def main() -> None:
    """Main function."""
    print(greet())
    print(game())
    return None


def greet() -> None:
    """Greetings."""
    hello: str = str(input("Hello! What's your name? -"))
    global player
    player = hello
    print(f"It's nice to meet you, {player}.")
    print("This is simply a coin flip game. All you have to do is guess if the coin lands on heads or tails as many times in a row as possible.")
    return None


def dislike() -> None:
    """Someone you don't like."""
    someone: str = str(input("Name your least favorite celebrity. - "))
    global hate
    hate = someone
    print(f"If you guess wrong {hate} is going to laugh at you and possibly insult you very creatively!")


def game() -> str:
    selection: str = str(input(f"{player}, would you like to choose heads or tails, words of inspiration, or quit?"))
    global choice
    choice = selection
    heads: list[int] = [1]
    tails: list[int] = [2]
    if choice == "heads":
        choice == 1
        print(coin())
    if choice == "tails":
        choice == 2
        print(coin())
    if choice == "words of inspiration":
        choice == 3
    if choice == "quit":
        choice == 4
    else:
        print("That choice is invlaid.")


def coin(xs: list[int]) -> int:
    """Heads or tails."""
    chance: int = randint(1, 2)
    if choice == chance:
        global points
        points += 1
        print("That's right!")
    else:
        print("No, that's wrong.")
    global total
    total += 1
    return points
    




if __name__ == "__main__":
  main()