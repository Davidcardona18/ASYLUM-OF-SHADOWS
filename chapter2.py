#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

def start_chapter(knowledge=False, haunted=False, tools=False, **kwargs):
    """
    The player navigates the Hall of Mirrors. Choices determine progression or a loop-back to Chapter 1.
    """
    print("\nChapter 2: Hall of Mirrors")
    print("You find yourself trapped in a hall of mirrors that reflect your darkest fears.")
    print("The reflections begin to move independently, distorting reality.")
    
    # Present choices to the player
    print("\nYour choices:")
    print("1. Smash the mirror")
    print("2. Confront the moving reflection")
    print("3. Try to escape")
    
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
        print("\nYou break the mirror and escape, but at the cost of losing health.")
        return "chapter3", {"health": "weakened"}
    elif choice == 2:
        if knowledge:
            print("\nYou resist the illusions using the knowledge gained in Chapter 1.")
            return "chapter3", {"mental_clarity": "improved"}
        else:
            print("\nThe reflections overwhelm you, weakening your mind.")
            return "chapter3", {"mental_clarity": "weakened"}
    elif choice == 3:
        print("\nThe asylum distorts, pulling you back to Chapter 1.")
        return "chapter1", {"loop": True}
