# D'ontea Johnson 3.11.2025 Assignment 1.3 On the Wall + Flowchart

# The purpose of this code is to sing the song "N bottles of beer on the wall", N represents the number of bottles depending on user input. 

def bottles_of_beer():
    beer = int(input('How many bottles of beer are on the wall? ')) # prompts user to designate how many beers are on the wall. 
    print()
    while beer > 2: # this starts the songs countdown until the counter is less than 2. 
        print(f'{beer} Bottles of Beer on the wall. {beer} bottles of beer. You take one down, pass it around, {beer-1} bottles of beer on the wall.')
        print()
        beer -= 1
    while beer == 2: # this statement changes the final bottles into bottle. 
        print(f'{beer} Bottles of Beer on the wall. {beer} bottles of beer. You take one down pass it around, {beer-1} bottle of beer on the wall.')
        print()
        beer -= 1
    if beer == 1: # this statement changes the final line to indicate that there are no more bottles of beer on the wall and also requests that the user to get more. 
        print(f'{beer} Bottle of Beer on the wall. {beer} bottle of beer. You take one down pass it around, no more bottles of beer on the wall.')
        print()
        print('Time to get more...')
    if beer <= 0: # prevents any illogical statements. 
        print('There is no beer to pass around...')
        
bottles_of_beer()