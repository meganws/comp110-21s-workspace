"""Examples of dictionaries."""


# establish a tuype of dict[key type, value type]
# empty dictionary literal is {}
players: dict[str, int] = {}

# inset a new key-value pair
# reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4 # This intentionally off by one
players["Bacot"] = players['Bacot'] + 1
print(players)
print(players['Brooks'])

# for..in loops will give you each key one-by-one
# defining key nad value is not necessay since
# you have already definined players as dict[int, str]
for player_name in players:
    key: str = player_name
    value: int = players[key]
    print(f'{player_name} -> {players[player_name]}')
    print(f'{key} -> {value}')
    

# you can have keys and values of any times. Notice this is the inverse
# mapping that we have about. Additionally, this is an example of a dictionary literal
jerseys: dict[int, str] = {15: 'Brooks', 2: 'Love', 5: 'Bacot'}
jerseys[23] = 'Jordan'
# with lists you have to .append, but here you can just add a key value
# don't have to use .append
print(jerseys)
print(jerseys[23])


# the pop methos allows you to remove key-value pair by its key. The pop
# method returns the value associated with the pop key.
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)