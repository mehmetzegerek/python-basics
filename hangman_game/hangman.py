import random

words = ["Shoe","Cat","Istanbul","Remote"]
word = random.choice(words)
result = ["_" for x in word]
health = 10

def get_first(iterable:list,key:str):
    for item in iterable:
        if item == key:
            return key
    return None
        

def show_available(word:str,src:str = None):
    global result
    if src is not None: 
        for x in range(len(result)):
            if word[x].lower() == src.lower():
                result[x] = src
    return " ".join(str(e) for e in [x for x in result])

def check_selection(word:str,src:str = None):
    global health
    is_player_passed = False
    for x in range(len(result)):
        if word[x].lower() == src.lower():
            print("You're lucky the value you enter is present in the word")
            is_player_passed = True
            break
    if not is_player_passed : health -= 1 
    print(show_available(word=word,src=src))
    
def show_man():
    global health
    output_dict = {
        10 : """
            _______
            |     |
            |
            |
            |
            |\n
        """,
        9: """
            _______
            |     |
            |     ◯ 
            |
            |
            |\n
        """,
        8:"""
            _______
            |     |
            |     ◯ 
            |    /
            |
            |\n
        """,
        7:"""
            _______
            |     |
            |     ◯ 
            |    /|
            |
            |\n
        """,
        6:"""
            _______
            |     |
            |     ◯ 
            |    /|\\
            |
            |\n
        """,
        5:"""
            _______
            |     |
            |     ◯ 
            |    /|\\
            |    /
            |\n
        """,
        4:"""
            _______
            |     |
            |     ◯ 
            |    /|\\
            |    / \\
            |\n
        """,
        3:"""
            _______
            |     |
            |     ◯! 
            |    /|\\
            |    / \\
            |\n
        """,
        2:"""
            _______
            |     |
            |     ◯! 
            |    /}\\
            |    / \\
            |\n
        """,
        1:"""
            _______
            |     |
            |    *◯' 
            |    /}\\
            |    / \\
            |\n
        """,
        0:"""
            _______
            |     |
            |     X 
            |    /}\\
            |    / \\
            |
            
            You're lost !\n
        """,
    }
    return output_dict[health]   

while health > 0:
    print(f"\nYou're health is : {health}\n")
    print(show_available(word=word),"\n")
    player_choice = input("Make a choice : ")
    check_selection(word=word,src=player_choice)
    print(show_man())
    
    
    if get_first(result,"_") is None :
        print("You won !")
        break
    
    