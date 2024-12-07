#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

def start_chapter(tools=False, mental_clarity=None, **kwargs):
    """
    The final confrontation with the mastermind. Choices determine the game's ending.
    Arguments:
        tools: Indicates if the player has extra tools from Chapter 4.
        mental_clarity: Indicates the player's mental state.
        kwargs: Handles additional conditions dynamically.
    """
    print("\nChapter 5: The Final Chamber")
    print("You finally confront the mastermind behind the asylum.")
    print("All the decisions you’ve made throughout the game will determine your fate.")
    print("The mastermind towers over you, and the weight of the asylum’s horrors presses down.")

    # Present choices to the player
    print("\nYour choices:")
    print("1. Fight for Freedom")
    print("2. Embrace the Darkness")
    print("3. Try to Avoid")

    while True:
        try:
            choice = int(input("What will you do? (Enter 1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Handle player's choices
    if choice == 1:
        # Fight for freedom
        if tools:
            print("\nYou use the tools and knowledge you’ve gathered to defeat the mastermind.")
            print("The final blow lands, and the mastermind crumples before you.")
            print("The asylum’s walls tremble and collapse as light pours into the once-dark corridors.")
            print("Ending 1: Win and Escape")
            print("Closing Text:")
            print(
                "The horrors you faced may never leave your mind, but you have survived. "
                "You step into the warmth of daylight, finally free from the nightmare. "
                "You are free. For now."
            )
        elif mental_clarity == "intact":
            print("\nWith sheer mental clarity, you resist the mastermind’s influence and overcome the battle.")
            print("The asylum collapses around you, and you escape.")
            print("Ending 1: Win and Escape")
            print("Closing Text:")
            print(
                "Though you escaped, the horrors of the asylum may haunt you forever. "
                "For now, you step into the light and leave the nightmare behind."
            )
        else:
            print("\nWithout the necessary tools or mental clarity, you fail to overcome the mastermind.")
            print("You fall into despair, consumed by the asylum’s evil.")
            print("Ending 3: Succumb to Madness")
            print("Closing Text:")
            print(
                "As the mastermind's laughter echoes in your ears, the asylum consumes you. "
                "The walls twist, and reality fractures into shards of torment. "
                "Your story ends here, your name lost to the whispers. "
                "The asylum wins, as it always does. Welcome to the darkness."
            )
    elif choice == 2:
        # Embrace the darkness
        print("\nThe asylum calls to you, its darkness wrapping around like a familiar cloak.")
        print("You lower your guard, letting the mastermind’s will merge with your own.")
        print("Ending 2: Become the Ruler")
        print("Closing Text:")
        print(
            "The darkness wraps around you like a familiar cloak. "
            "The voices, once foreign and terrifying, now feel like old friends. "
            "The asylum bends to your will, its twisted halls becoming your domain. "
            "You are no longer the prey—you are the master."
        )
    elif choice == 3:
        # Try to avoid
        print("\nYou try to avoid confronting the mastermind, but the asylum’s horrors overwhelm you.")
        print("Your mind collapses under the weight of despair.")
        print("Ending 3: Succumb to Madness")
        print("Closing Text:")
        print(
            "As the mastermind's laughter echoes in your ears, the asylum consumes you. "
            "Your identity dissolves into the shadows, becoming another specter that haunts these halls. "
            "The asylum wins, as it always does. Welcome to the darkness."
        )
