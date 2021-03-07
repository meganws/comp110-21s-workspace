"""Choose your own adventure: pokemon-style."""
__author__ = 730388741

player: str = str("Me")
points: int = int(0)

def main() -> None:
    print(greet())
    print(creature_selection())
    return None
    

def greet() -> None:
    """Greeting."""
    name: str = str(input("Hello! What's your name? - "))
    global player
    player = name
    print(f"Nice to meet you, {player}! You can call me B-SOS.")
    print("This is a creature-battling game (like Pokemon, but not) where you will be battling your not-Pokemon against your opponent's Pocket Creature.")
    
def creature_selection() -> None:
    selection: str = input("Choose your Pocket Creature's attribute, or quit: Fighter, Spellcaster, Archer, or Quit. -")
    stats_list: list[int]
    if selection == "fighter" or "spellcater" or "archer":
        if selection == "fighter":
            attack: int = 7
            defense: int = 4
            speed: int = 5
            hp = 30
            global points
            points = hp
        if selection == "spellcaster":
            attack: int = 5
            defense: int = 7
            speed: int = 5
            hp = 30
            global points
            points = hp
        if selection == "archer":
            attack: int = 6
            defense: int = 4
            speed: int = 6
            hp = 30
            global points
            points = hp
    else:
        attack: int = 0
        defense: int = 0
        speed: int = 0
    stats_list = [attack, defense, speed]
    print(f"You chose {selection}. Here are your stats.")
    print(f"Attack: {stats_list[attack]}")
    print(f"Defense: {stats_list[defense]}")
    print(f"Speed: {stats_list[speed]}")
    return None


def end() -> str:
    """Ending function."""
    end: str = str("Your experience ends here. You ended with {points} points.")
    return end



if __name__ == "__main__":
  main()