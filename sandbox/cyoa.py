"""Choose your own adventure: includes some kind of loop and is very extensive and a tiny bit frustrating."""
__author__ = "730388741"

from random import randint
points: int = 0
player: str = str("Me")
cactus: int = 0
EMOJI = str("\U0001F44B")
mushrooms: int = 0


def main() -> None:
    """Okay now here's main."""
    global points
    if points < 1:
        greet()
        print("This game is about going through some doors with some keys in a weird inn.")
        print("Sounds simple right? Yeah... simple.")
        print("Some doors will require you to collect multiple keys. Keys can be collected in rooms.")
        print("Some doors require more keys to open them than you can collect the first time.")
        print("This means that you might have to purposely respawn the keys.")
        print("Keys respawn when you go all the way back to the lobby by typing 'leave'.")
        print("They can also respawn if you leave the inn.")
        print("The amount of keys you have will be saved each time you reset the game until you exit the program.")
        print("Usually when you're doing quests like these, it's because you need something.")
        print("So keep that in mind. You need something.")
        print("Note: B-SOS helps a lot of people every day and they can't remember everybody's name,")
        print("so sometimes you might have to re-introduce yourself when you re-enter the inn.")
    print("You are in the lobby of the inn with three doors in front of you.")
    first_choice: str = str(input("Which room do you go in: 1, 2, 3, count keys, or leave - "))
    if first_choice == "count keys":
        keys: int = int(count_keys())
        print(f"You have {keys} key(s).")
        main()
    if first_choice == "leave":
        print("Goodbye.")
        print(f"You have {points} keys(s)!")
        okay()
        loop_thing()
    if first_choice == "1":
        first_room_one()
    if first_choice == "2":
        first_room_two()
        main()
    if first_choice == "3":
        first_room_three()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    return None


def greet() -> None:
    """Greeting."""
    global HOTEL_EMOJI
    print("Hello! I'm B-SOS. I'm the keeper of this inn.")
    hello: str = str(input("What's your name?- "))
    global player
    player = hello
    print(f"Nice to meet you, {player}")
    print(EMOJI)
    okay()
    return None


def count_keys(keys= int) -> int:
    """Count of keys for that int requirement."""
    global points
    number: int = int(points)
    return number


def first_room_one() -> None:
    """Room one of the first choice."""
    global points
    print(f"Okay, {player}. You walk into a dark room. Do you:")
    choice: str = str(input("Turn the light on, explore, or leave? - "))
    if choice == "leave":
        loop_thing()
    if choice == "turn the light on":
        print("You turn the light on and there is a hideous monster sitting in the middle of the room.")
        print("It starts to move and you get scared and run out of the room.")
        okay()
        loop_thing()
    if choice == "explore":
        points += 1
        print("You feel around the room in the dark with your hands extended in front of you.")
        print("You feel something small and cold. You grab at it with your hand. A key!")
        print(f"You now have {points} key(s)!")
        okay()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    first_room_one_junction()


def first_room_one_junction() -> None:
    """A junction after room one."""
    choice: str = str(input("You look at the other two rooms. Which one do you go through? 2 or 3 - "))
    if choice == "2":
        first_room_two()
        main()
    if choice == "3":
        first_room_three()
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        loop_thing()
    return None
        

def first_room_two() -> None:
    """First room number two option."""
    global points
    print("You walk into a room. There's a key on the ground so you pick it up.")
    points += 1
    print(f"You now have {points} key(s)!")
    main()
    return None


def first_room_three() -> None:
    """First room three options."""
    print("You enter the room and there are two doors in front of you.")
    choice: str = str(input("Which door do you go through? 1 or 2 or leave - "))
    if choice == "1":
        second_room_one()
    if choice == "2":
        second_room_two()
    if choice == "leave":
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()


def second_room_one() -> None:
    """Mashed potato man."""
    global points
    print("You open the door and there is a bathtub full of instant-mashed potatoes.")
    print("An old man is standing there, expectantly staring at you to get in.")
    print("He is wearing a pure white, fluffy bathrobe.")
    print("In his hand wasa sponge soaked in what you presumed was gravey in his hand.")
    choice: str = str(input("What do you do? get in or leave - "))
    if choice == "get in":
        points += 8
        print("The man notices your committment to the mashed potatoes and grants you 8 keys!")
        print(f"You now have {points} keys(s)!")
        okay()
        second_room_one_junction()
    if choice == "leave":
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    return None


def second_room_one_junction() -> None:
    """Doors behind mashed potato man."""
    print("Behind the bathtub there are three more doors.")
    choice: str = str(input("Which door do you go through? 1, 2, 3, or leave- "))
    if choice == "1":
        second_room_ones_room_one()
    if choice == "2":
        second_room_ones_room_two()
    if choice == "3":
        second_room_ones_room_three()
    if choice == "leave":
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    return None


def second_room_ones_room_one() -> None:
    """Art class you have to pay for."""
    global points
    print("You walk into an art class. The teacher becons for you to pose for the students to paint.")
    choice: str = str(input("Do you let them paint you? yes or no - "))
    if choice == "yes":
        print("It turns out the teacher is going to charge you for being painted!")
        print("Because you don't have any money on you, you pay them 6 keys.")
        points -= 6
        print(f"You now have {points} keys!")
        okay()
        after_art_room()
    if choice == "no":
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    return None


def after_art_room() -> None:
    global mushrooms
    print("Angry, you push the art teacher out of the way and you see a closet behind them.")
    print("You walk into the closet and see a goblet full of mushrooms.")
    choice: str = str(input("What do you do with the mushrooms? Eat, steal, leave - "))
    if choice == "eat":
        print("You eat the mushrooms. Not long after, you start seeing Ronald McDonald staring at you.")
        print("He is beconing for you to follow him through the intergalactic portal.")
        portal: str = str(input("Do you follow him? Yes or no- "))
        if portal == "yes":
            print("You follow him through the portal.")
            okay()
            portal_woo()
        if portal == "no":
            print("You thank Ronald for the invitation, but you forgot you had to walk your fish.")
            fish()
            okay()
        else:
            print("Before you could form a coherent sentence, Ronald grabbed you and pulled you through the portal.")
            portal_woo()
    if choice == "steal":
        mushrooms += 3
        print("You look around and make sure no one is watching.")
        print("You stash the mushrooms in your bag and flee the scene.")
        print(f"You now have {mushrooms} mushrooms!")
        okay()
        main()
    if choice == "leave":
        main()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
        okay()
        loop_thing()
    return None


def fish() -> None:
    global points
    print("Suddenly a fishbowl appears in you lap.")
    print("You gaze into it and become mezmerized by the colors of its scales.")
    print("The fish morphs into a piranha.")
    choice: str = str(input("Do you fight the piranha? Yes or no- "))
    if choice == "yes":
        print("You wield your flame sword and charge at the piranh, screaming your battle cry.")
        print("The piranha starts quivering and dissapates into 8 keys.")
        points += 8
        print(f"You now have {points} keys!")
        okay()
        print("You come off your high. You are still in the art room closet.")
        print("You leave the art room, but not before draining all the black and red paint that was in the closet.")
        okay()
        main()
    if choice == "no":
        print("You shrink in fear like the quivering baby you are.")
        print("A prey-like scream escapes your throat.")
        print("Shortly after, something cold splashed on your face and you wake with a start.")
        print("The art teacher is standing over you.")
        print("You groan and hand them 6 more keys before being kicked out.")
        points -= 6
        print(f"You now have {points} keys!")
        main()
    return None


def portal_woo() -> None:
    global points
    global mushrooms
    global cactus
    print("You walk into the portal with Ronald. You are met by a plethora of notable figures.")
    print("Barney, Fantastic Mr. Fox, Bugs Bunny. Everyone greets you with smiles on their faces.")
    if points <= 15:
        print("You wave at everyone. Right when you do, something cold splashes on your face.")
        print("You come to and see worried children standing over you.")
        print("The art teacher looms over you and holds out their hand again.")
        print("Grumbling, you hand them another 6 keys.")
        points -= 6
        print(f"You now have {points} keys!")
        okay()
        main()
    print("You show off your epic loot you have collected during your time at the inn.")
    print("Their eyes widen, and they duck their heads together in a huddle, occasionally peeking at you.")
    print("They nod, surround you, push you over, and steal all of your things.")
    points = 0
    mushrooms = 0
    cactus = 0
    print(f"You now have {points} keys!")
    okay()
    print(f"You now have {mushrooms} mushrooms.")
    okay()
    print(f"You now have {cactus} cactus!")
    okay()
    print("You come to and are surrounded by security guards.")
    print("They are holding your belongings and escort you out of the inn.")
    print("You are not allowed back in the inn.")
    quit_funtion()
    return None


def second_room_ones_room_two() -> None:
    """Karaoke night with grandma."""
    global points
    song_choice()
    print("You walk into a dimly-lit room. A spotlight flashed in your face you were met with applause.")
    print("A microphone was tossed at you.")
    print(f"The music to {song_choice()} started playing through some hidden speakers.")
    print("Panicking, you start screaming the lyrics, which you know by heart, without missing a beat.")
    if song_choice() == str("S&M"):
        print("You see your grandma jump up from the crowd, her face red with embarrassment.")
        print("You run after her as she leaves the inn, trying to clean up the lyrics of the song.")
        print("You drop half of your keys in the process.")
        points = int(points / 2)
        print(f"You now have {points} keys!")
        okay()
        loop_thing()
    if song_choice() == ("Amazing Grace"):
        print("The crowd gives you a standing ovation, throwing flowers and keys at you.")
        points += 4
        print(f"You now have {points} keys!")
        okay()
        main()
    else:
        print("When you finish all you hear is a cough as the crowd stays silent.")
        print("Then suddenly you see your grandma stand up and clap vigorously.")
        print("She walks on to the stage, pinches your cheek, and fishes in her purse and hands you 5 keys.")
        points += 5
        print(f"You now have {points} keys!")
        okay()
        main()
    return None


def song_choice() -> str:
    """Randint song choice."""
    song: int = randint(1, 3)
    if song == 1:
        song_name = str(int(song))
        song_name: str = str("S&M")
        return song_name
    if song == 2:
        name_song = str(int(song))
        name_song: str = str("Amazing Grace")
        return name_song
    else:
        songname = str(int(song))
        songname: str = str("Twinkle, Twinkle Little Star")
        return songname


def second_room_ones_room_three() -> None:
    """Do you have enough keys to get through."""
    global points
    global cactus
    print("You walk into a room and there is a locked door. You see there is someone guarding the door.")
    print("They say, 'This door requires 35 keys to get through'")
    if points >= 35:
        if points >= 40:
            print("You hand the guard your keys so they can open the door.")
            print("Their gaze flicks from you, to the keys, and back at you.")
            print("Slowly, they slide the keys into their pocket, not breaking eye contact the entire time.")
            okay()
            print("You start to protest, but then they say:")
            print("'You don't need ALL of these, do you?'")
            print("'If you're able to get THIS many, then obviously you're enjoying yourself, right?'")
            print("You ask why the guard is doing this, why they are taking all of your hard work and making you start over.")
            okay()
            print("The guard ponders for a moment, a finger stroaking their chin, before they just shrug.")
            print(f"I dunno, I don't like the number {points}. It's too... high.")
            points = 0
            print(f"You now have {points} keys!")
            protest: str = str(input("Do you try to fight?"))
            if protest == "yes":
                protest_woo()
            if protest == "no":
                main()
            if protest == "no u":
                print("The guard blinks at you and nods in agreement.")
                print("'You make a compelling point.'")
                print("They fish the keys out of their pocket and opens the door for you.")
                print("You see your lost slipper inside!")
                okay()
                print("But wait, what's this?")
                print("Another cactus!")
                cactus += 1
                print(f"You now have {cactus} cactus(es)!")
                okay()
                choice: str = str(input("Would you like to play again? yes or no - "))
                if choice == "yes":
                    points = 0
                    loop_thing()
                else:
                    quit_funtion()
                return None
        winner_room()
    else:
        print("You tell the you don't have that many keys.")
        print("They get annoyed with you and take all your keys, but gives you a consolation cactus.")
        points = 0
        cactus += 1
        print(f"You now have {points} keys!")
        print(f"You now have {cactus} cacti")
        okay()
        loop_thing()
    return None


def protest_woo() -> None:
    global points
    global cactus
    print("You start to shout your protests.")
    print("The guard rolls their eyes.")
    print("Fine, here's something to shut you up.")
    cactus += 1
    points += 1
    print(f"You now have {points} keys!")
    print(f"You now have {cactus} cacti!")
    okay()
    print("Before you could protest more, the guard shoves you out of the inn.")
    loop_thing()
    return None


def winner_room() -> None:
    """You beat the game."""
    global points
    print(f"You show they guard your {points} keys. They nod slowly and open the door for you.")
    print("Inside the room was what you were seeking: your lost slipper!")
    print(f"Congratualtions! You beat the game with {points} keys.")
    okay()
    choice: str = str(input("Would you like to play again? yes or no - "))
    if choice == "yes":
        points = 0
        loop_thing()
    else:
        quit_funtion()
    return None
    

def second_room_two() -> None:
    """Don't be too cocky/good things happen to those without high expectations."""
    global points
    global cactus
    if cactus == 1:
        print("You show the professor your cactus.")
        print("He enjoys its company and gives you 10 keys as a token of his gratitude.")
        points += 10
        print(f"You now have {points} keys!")
        okay()
    print("You walk into a room with a single desk in the middle.")
    print("Written on the white board in the back of the room is: 'Do you pass the test?'")
    print("You look closer and there is a programming test on the desk.")
    choice: str = str(input("Do you pass the test? yes or no- "))
    if choice == "yes":
        print("You went in with confidence and disappointed. When you got your test back you see a fat F.")
        print("Since the F on your programming test was crushing enough, you don't lose any keys.")
        points += 0
        print(f"You now have {points} keys!")
        okay()
        first_room_three()
    if choice == "no":
        print("You went in expecting the least, but when you got your test back you saw a fat A!")
        print("For doing so well on you test, Professor Jordan rewards you 2 keys.")
        points += 2
        print(f"You now have {points} keys!")
        okay()
        first_room_three()
    else:
        print("Because you chose an invalid option, you got confused and left the inn.")
    return None


def loop_thing() -> None:
    """While loops are annoying so let's try this."""
    print(f"You now have {points} keys!")
    choice: str = str(input("Do you want to go into the inn? yes or no- "))
    if choice == "yes":
        main()
    else:
        print(f"Goodbye! You finished with {points} keys.")
        quit_funtion()
    return None


def okay() -> None:
    """To have a reading break between important sections."""
    choice: str = str(input("Type okay to continue- "))
    if choice == "okay":
        return None
    if choice == "Okay":
        return None
    else:
        print("That doesn't say 'okay', now does it?")
        okay()
        return None


def quit_funtion() -> None:
    """Function to exit the game."""
    quit()


if __name__ == "__main__":
    main()