# The High-Score Tracker Game

# Start an intentional infinite loop
while True:

    # Ask the user to enter a score or "stop"
    user_input = input("Enter your game score (or type 'stop' to quit): ")

    # Check if the user wants to stop
    if user_input.strip().lower() == "stop":
        print("Game session ended!")
        break

    # Convert the input to an integer
    score = int(user_input)

    # Check if it's a high score
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")