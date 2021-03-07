"""Choose your own adventure, RPG-style"""
__author__ = 730388741

from random import randint

points: int = 0

def main() -> None:
    """Main funtion."""
    greet()
    print("This is a short RPG-style game. The choices you make will affect the outcome of the game.")
    print("Choose a class. Your class will affect your in-game experience.")
    class_selection()
    print(points)
    print("The monarch of your kingdom orders you to journey to the Cave of Dashmar to take care of a monster feared by your kingdom. They have taken notice to your skills and believe you are the best suited for this job.")
    print(a_fork_in_the_road())
    return None


def greet() -> None:
    """Greeting."""
    print("Welcome, adventurer! What shall we call you?")
    player: str = str(input("Enter a nickname "))
    print(f"It's nice to meet you, {player}.")
    return None


def class_selection(class_selection: str = ("warrior," "mage," "rogue," "mythborn")) -> str:
    """Class selection."""
    selection: str = input("Warrior, mage, rogue, mythborn, or end experience ")
    if selection == "warrior" or "mage" or "rogue" or "mythborn":
        global points
        points += 1
        if selection == "warrior":
            warrior: str = str("Your class is: Warrior.")
            return warrior
        if selection == "mage":
            mage: str = str("Your class is: Mage.")
            return mage
        if selection == "rogue":
            rogue: str = str("Your class is now: Rogue.")
            return rogue
        if selection == "mythborn":
            mythborn: str = str("Your class is now: Mythborn")
            return mythborn
    else:
        finish: str = str("Farewell, adventurer.")
        print(finish)
        quit()


def a_fork_in_the_road() -> str:
    """What happens when you come to a fork in the road?"""
    print("You are walking on a narrow path through the forest when you come to a fork in the road.")
    if input("Do you choose to go left or right? -") == "left":
        print("Take the path going to the left. You stumble upon an abandoned camp, and upon further inspection you find that there is plently of loot unattended.")
        if input("Do you choose to: leave, steal, or explore ") == "steal":
            outcome: str = str("You swipe the gold coins and small weapons and put them in your pack. Before you could grab everything, there is a rustle in the trees and out walks a party of enemy soldiers. They are not happy you are stealing their things. Outnumbering you, they strike you down." + gameover())
            return outcome
        if input("Do you choose to: leave, steal, or explore ") == "explore":
            outcome: str = str("You explore the camp. You see shiny gold and weapons lying around but you don't take them, instead just wondering who lives in this camp. As you finish your thoughts a party of enemy soldiers appear. With swords drawn, they question who you are.")



def warrior_stats(xs: list[int]) -> int:
    """Defining stats for the classes"""
    stats: list[str] = ["strength", "intelligence", "dexterity", "communication", "mythic"]
    strength: int = 8
    intelligence: int = 5
    dexterity: int = 6
    communication: int = 4
    mythic: int = 0
    


# have the different stats here in list form

def gameover() -> str:
    finish: str = str("Your adventure has come to an end.")
    print(points)
    return finish


# instead of having the description in the class choosing, have individual functions for each class with descriptions and stats


if __name__ == "__main__":
    main()
