#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

def start_chapter(key=False, journal=False, **kwargs):
    """
    The player navigates the Operating Room. Choices determine progression to Chapter 5 or a loop-back to Chapter 3.
    """
    print("\nChapter 4: The Operating Room")
    print("You enter a sterile, cold operating room filled with grotesque experiments and jars of organs.")
    
    print("\nYour choices:")
    print("1. Explore the room")
    print("2. Answer the voices")
    print("3. Block out the noise")
    
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
        if key:
            print("\nUsing the key, you unlock a hidden room with tools for the final battle.")
            return "chapter5", {"tools": True}
        else:
            print("\nYou find some useful items, but they might not be enough for what lies ahead.")
            return "chapter5", {"tools": False}
    elif choice == 2:
        if journal:
            print("\nThe journal helps you resist the voices, preserving your mental clarity.")
            return "chapter5", {"mental_clarity": "intact"}
        else:
            print("\nThe voices overwhelm you, and your mind begins to spiral.")
            return "chapter5", {"mental_clarity": "weakened"}
    elif choice == 3:
        print("\nYou block out the noise, but the asylum warps again, sending you back to the Butcher Room.")
        return "chapter3", {"loop": True}
