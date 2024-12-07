#DAVID CARDONA
#MILESTONE 3
#NOVEMBER 15, 2024

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def main():
    # Game introduction
    print("=" * 50)
    print("Welcome to The Asylum of Shadows!")
    print("=" * 50)
    print(
        "\nGame Intro and Objective:\n"
        "In The Asylum of Shadows, you must navigate through a twisted asylum, "
        "making critical decisions determining your fate. Each chapter presents unique challenges, "
        "and some chapters loop back to previous ones, adding complexity and replayability. "
        "Your outcome depends on the choices you make throughout the game, leading to one of three possible endings.\n"
    )
    input("Press Enter to continue...\n")  # Pause for immersion

    # Ask for player's name
    player_name = input("What is your name, traveler? ")
    print(f"\nHello, {player_name}. Your journey begins now.")

    # Start the game dynamically
    current_chapter = "chapter1"
    conditions = {}

    # Game loop: Keeps running until the game ends
    while current_chapter:
        if current_chapter == "chapter1":
            current_chapter, conditions = chapter1.start_chapter(**conditions)
        elif current_chapter == "chapter2":
            current_chapter, conditions = chapter2.start_chapter(**conditions)
        elif current_chapter == "chapter3":
            current_chapter, conditions = chapter3.start_chapter(**conditions)
        elif current_chapter == "chapter4":
            current_chapter, conditions = chapter4.start_chapter(**conditions)
        elif current_chapter == "chapter5":
            # Final chapter ends the game
            chapter5.start_chapter(**conditions)
            current_chapter = None  # Exit the loop

    # End of game
    print("\nThank you for playing The Asylum of Shadows. Goodbye!")

if __name__ == "__main__":
    main()

