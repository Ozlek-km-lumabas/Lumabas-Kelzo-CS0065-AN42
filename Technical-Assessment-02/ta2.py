# ==========================================
# TASK 1: SET UP THE ENVIRONMENT
# ==========================================

# Ask the user for the initial state of each room
room_a = input("Is room A Dirty or Clean? ").capitalize()
room_b = input("Is room B Dirty or Clean? ").capitalize()

# Store the rooms in a dictionary
environment = {
    "A": room_a,
    "B": room_b
}


# Function to check if a room is dirty
def check_dirty(room):
    return environment[room] == "Dirty"


# Function to clean a room
def clean_room(room):
    environment[room] = "Clean"


# ==========================================
# TASK 2: RULE-BASED AGENT
# ==========================================

class CleaningAgent:

    def __init__(self):
        # Agent starts in room A
        self.location = "A"

    # Move to the other room
    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    # Perceive the current room and take action
    def perceive_and_act(self):

        # Rule 1:
        # If the current room is dirty, clean it
        if check_dirty(self.location):

            clean_room(self.location)

            return f"Room {self.location} has been cleaned."

        # Rule 2:
        # If the current room is clean, move
        else:

            self.move()

            return f"Moving to room {self.location}."


# ==========================================
# TASK 3: RUN THE SIMULATION
# ==========================================

# Ask the user how many steps to run
steps = int(input("\nHow many steps should the agent run? "))

# Create the agent
agent = CleaningAgent()


# Run the simulation
for step in range(1, steps + 1):

    print(f"\nStep {step}: Agent is in room {agent.location}")

    # Agent perceives the environment and acts
    action = agent.perceive_and_act()

    print(action)

    # Display current environment
    print("Environment state:", environment)