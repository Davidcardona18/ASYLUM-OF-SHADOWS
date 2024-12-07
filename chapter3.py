#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

def start_chapter(health=None, mental_clarity=None, **kwargs):
    """
    The player encounters a butcher. Choices determine progression to Chapter 4 or a loop-back to Chapter 2.
    """
    print("\nChapter 3: The Butcher Room")
    print("You encounter a butcher standing over a mutilated body. Blood drips from the walls.")
    
    print("\nYour choices:")
    print("1. Confront the butcher")
    print("2. Hide and observe")
    print("3. Flee")
    
    while True:
        try:
            choice = int(input("What will you do? (Enter 1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if choice == 1:
        print("\nYou fight the butcher. After a brutal struggle, you manage to find a key.")
        return "chapter4", {"key": True}
    elif choice == 2:
        print("\nYou hide and observe. You find a bloody journal containing hints for the next chapter.")
        return "chapter4", {"journal": True}
    elif choice == 3:
        print("\nYou panic and flee. The asylum warps, pulling you back to the Hall of Mirrors.")
        return "chapter2", {"loop": True}
