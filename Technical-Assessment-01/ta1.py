import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ============================================================
# GET USER INPUT
# ============================================================

num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

print("\nMovement Rules:")
print("1 - Random movement")
print("2 - Avoid other agents")
print("3 - Preferred direction (right)")

movement_choice = int(input("Choose movement rule: "))


# ============================================================
# AGENT DEFINITION
# ============================================================

class RandomWalker(ap.Agent):

    def setup(self):
        # Random starting position
        self.position = (
            random.randint(0, self.model.p.grid_size[0] - 1),
            random.randint(0, self.model.p.grid_size[1] - 1)
        )

        # Store the agent's movement history
        self.path = [self.position]

    def step(self):

        # Possible movements
        directions = [
            (1, 0),    # Right
            (-1, 0),   # Left
            (0, 1),    # Up
            (0, -1)    # Down
        ]

        # ----------------------------------------------------
        # RULE 1: RANDOM MOVEMENT
        # ----------------------------------------------------

        if self.model.p.movement_rule == 1:

            direction = random.choice(directions)

            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            # Keep agent inside grid
            new_x = max(
                0,
                min(self.model.p.grid_size[0] - 1, new_x)
            )

            new_y = max(
                0,
                min(self.model.p.grid_size[1] - 1, new_y)
            )

            self.position = (new_x, new_y)

        # ----------------------------------------------------
        # RULE 2: AVOID OTHER AGENTS
        # ----------------------------------------------------

        elif self.model.p.movement_rule == 2:

            random.shuffle(directions)

            for direction in directions:

                new_x = self.position[0] + direction[0]
                new_y = self.position[1] + direction[1]

                # Check boundaries
                if not (
                    0 <= new_x < self.model.p.grid_size[0]
                    and
                    0 <= new_y < self.model.p.grid_size[1]
                ):
                    continue

                new_position = (new_x, new_y)

                # Check whether another agent occupies the cell
                occupied = False

                for other in self.model.agents:

                    if other is not self and other.position == new_position:
                        occupied = True
                        break

                # Move if the position is not occupied
                if not occupied:
                    self.position = new_position
                    break

        # ----------------------------------------------------
        # RULE 3: PREFERRED DIRECTION
        # ----------------------------------------------------

        elif self.model.p.movement_rule == 3:

            # Agent prefers moving right
            preferred_direction = (1, 0)

            new_x = self.position[0] + preferred_direction[0]
            new_y = self.position[1] + preferred_direction[1]

            # If moving right would leave the grid,
            # choose a random valid direction instead.
            if new_x >= self.model.p.grid_size[0]:

                valid_directions = []

                for direction in directions:

                    test_x = self.position[0] + direction[0]
                    test_y = self.position[1] + direction[1]

                    if (
                        0 <= test_x < self.model.p.grid_size[0]
                        and
                        0 <= test_y < self.model.p.grid_size[1]
                    ):
                        valid_directions.append(direction)

                if valid_directions:
                    direction = random.choice(valid_directions)

                    new_x = self.position[0] + direction[0]
                    new_y = self.position[1] + direction[1]

            self.position = (new_x, new_y)

        # Record new position
        self.path.append(self.position)


# ============================================================
# MODEL DEFINITION
# ============================================================

class RandomWalkModel(ap.Model):

    def setup(self):

        # Create agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        # Create grid
        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        # Add agents to grid
        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()


# ============================================================
# PARAMETERS
# ============================================================

parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps,
    'movement_rule': movement_choice
}


# ============================================================
# CREATE MODEL
# ============================================================

model = RandomWalkModel(parameters)

model.setup()


# ============================================================
# MATPLOTLIB ANIMATION
# ============================================================

fig, ax = plt.subplots()

ax.set_xlim(-0.5, grid_size - 0.5)
ax.set_ylim(-0.5, grid_size - 0.5)

ax.set_xticks(range(grid_size))
ax.set_yticks(range(grid_size))

ax.grid(True)

ax.set_title("Random Walker Simulation")


# Agent dots
scat = ax.scatter([], [], s=200)


# Lines showing paths
path_lines = []

for agent in model.agents:

    line, = ax.plot([], [], linewidth=1)

    path_lines.append(line)


# ============================================================
# ANIMATION UPDATE
# ============================================================

def update(frame):

    # Move agents
    model.step()

    # Get current positions
    x = [
        agent.position[0]
        for agent in model.agents
    ]

    y = [
        agent.position[1]
        for agent in model.agents
    ]

    # Update agent dots
    scat.set_offsets(list(zip(x, y)))

    # Update paths
    for i, agent in enumerate(model.agents):

        path_x = [
            position[0]
            for position in agent.path
        ]

        path_y = [
            position[1]
            for position in agent.path
        ]

        path_lines[i].set_data(path_x, path_y)

    ax.set_title(
        f"Step {frame + 1} / {num_steps}"
    )

    return [scat] + path_lines


# ============================================================
# START ANIMATION
# ============================================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    blit=False,
    repeat=False
)

plt.show()


# ============================================================
# FINAL POSITION ANALYSIS
# ============================================================

print("\n====================================")
print("FINAL AGENT POSITIONS")
print("====================================")

for i, agent in enumerate(model.agents):

    print(
        f"Agent {i + 1}: {agent.position}"
    )


# ============================================================
# DISTRIBUTION ANALYSIS
# ============================================================

position_counts = {}

for agent in model.agents:

    position = agent.position

    if position not in position_counts:
        position_counts[position] = 0

    position_counts[position] += 1


print("\n====================================")
print("FINAL POSITION DISTRIBUTION")
print("====================================")

for position, count in position_counts.items():

    print(
        f"Position {position}: "
        f"{count} agent(s)"
    )


# ============================================================
# SUMMARY
# ============================================================

occupied_cells = len(position_counts)

print("\n====================================")
print("SUMMARY")
print("====================================")

print(f"Total agents: {num_agents}")
print(f"Grid size: {grid_size} x {grid_size}")
print(f"Simulation steps: {num_steps}")
print(f"Occupied cells: {occupied_cells}")

if occupied_cells < num_agents:
    print(
        "Some agents ended on the same grid cells."
    )
else:
    print(
        "Agents ended on separate grid cells."
    )
