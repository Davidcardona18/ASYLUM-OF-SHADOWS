#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

def start_chapter(**kwargs):
    """
    Introduction to the game. The player enters a dark asylum and makes a critical choice.
    Returns the next chapter and conditions as a tuple.
    """
    print("\nChapter 1: The Asylum")
    print("You enter a dark, decrepit asylum. Whispers echo from the walls, and a shadowy figure looms in the distance.")
    
    # Present choices to the player
    print("\nYour choices:")
    print("1. Investigate the figure")
    print("2. Avoid the figure")
    print("3. Open a nearby door")
    
    # Get player input and validate it
    while True:
        try:
            choice = int(input("What will you do? (Enter 1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break  # Valid choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Handle the player's choice
    if choice == 1:
        print("\nYou approach the figure. It whispers cryptic warnings that may help you later.")
        print("Transitioning to Chapter 2 with extra knowledge...")
        return "chapter2", {"knowledge": True}
    elif choice == 2:
        print("\nYou avoid the figure, but its unsettling presence lingers. It may haunt you later.")
        print("Transitioning to Chapter 2 with the figure haunting you...")
        return "chapter2", {"haunted": True}
    elif choice == 3:
        print("\nYou open a nearby door and find a toolbox with useful items.")
        print("Transitioning to Chapter 2 with tools...")
        return "chapter2", {"tools": True}
