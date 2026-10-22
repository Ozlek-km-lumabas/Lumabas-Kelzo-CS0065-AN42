# ============================================================
# KNOWLEDGE REPRESENTATION, RULE-BASED REASONING,
# AND CASE-BASED REASONING
# ============================================================

# ============================================================
# PART 1 - KNOWLEDGE BASE
# ============================================================

facts = {
    "temperature": 32,
    "is_raining": True,
    "humidity": 85,
    "person_present": True,
    "fan_on": False,
    "window_open": False
}

# ============================================================
# PART 2 - RULE-BASED REASONING
# ============================================================

# Rule 1
def rule_hot_room(facts):

    if facts["temperature"] > 30 and facts["person_present"]:
        return "Turn on the fan"

# Rule 2
def rule_raining(facts):

    if facts["is_raining"] and facts["window_open"]:
        return "Close the window"

# Rule 3
def rule_high_humidity(facts):

    if facts["humidity"] > 80 and facts["person_present"]:
        return "Turn on the fan"

# Inference engine
def inference_engine(facts):

    rules = [
        rule_hot_room,
        rule_raining,
        rule_high_humidity
    ]

    actions = []

    for rule in rules:

        result = rule(facts)

        if result is not None:
            actions.append(result)

    # Remove duplicate actions
    return list(set(actions))

# Display RBR results
print("==========================================")
print("RULE-BASED REASONING")
print("==========================================")

actions = inference_engine(facts)

print("\nKnowledge Base:")

for key, value in facts.items():
    print(f"{key}: {value}")

print("\nRule-Based Reasoning Actions:")

for action in actions:
    print("-", action)

# ============================================================
# PART 3 - CASE-BASED REASONING
# ============================================================

case_base = [

    {
        "problem": {
            "temperature": 32,
            "is_raining": True,
            "humidity": 85,
            "person_present": True
        },
        "solution": "Turn on the fan and close the window."
    },

    {
        "problem": {
            "temperature": 25,
            "is_raining": False,
            "humidity": 50,
            "person_present": True
        },
        "solution": "Keep the fan off and open the window."
    },

    {
        "problem": {
            "temperature": 35,
            "is_raining": False,
            "humidity": 70,
            "person_present": True
        },
        "solution": "Turn on the fan."
    }
]

# Calculate similarity
def calculate_similarity(current_problem, past_problem):

    score = 0

    for feature in current_problem:

        if current_problem[feature] == past_problem[feature]:
            score += 1

    return score

# Retrieve most similar case
def retrieve_case(current_problem, case_base):

    best_case = None
    best_score = -1

    for case in case_base:

        score = calculate_similarity(
            current_problem,
            case["problem"]
        )

        if score > best_score:

            best_score = score
            best_case = case

    return best_case, best_score

# Revise solution
def revise_solution(solution):

    print("\nRetrieved solution:")
    print(solution)

    choice = input(
        "\nDo you want to keep this solution? (y/n): "
    ).lower()

    if choice == "y":

        return solution

    else:

        new_solution = input(
            "Enter the revised solution: "
        )

        return new_solution

# Retain new case
def retain_case(problem, solution, case_base):

    new_case = {
        "problem": problem.copy(),
        "solution": solution
    }

    case_base.append(new_case)

    print("\nNew case has been retained.")

# ============================================================
# CBR SIMULATION
# ============================================================

print("\n==========================================")
print("CASE-BASED REASONING")
print("==========================================")

current_problem = {
    "temperature": facts["temperature"],
    "is_raining": facts["is_raining"],
    "humidity": facts["humidity"],
    "person_present": facts["person_present"]
}

# RETRIEVE
best_case, score = retrieve_case(
    current_problem,
    case_base
)

print("\nMost similar past case:")
print(best_case["problem"])

print("\nSimilarity score:", score)

# REUSE
solution = best_case["solution"]

# REVISE
solution = revise_solution(solution)

# RETAIN
retain_case(
    current_problem,
    solution,
    case_base
)

print("\nFinal CBR solution:")
print(solution)

print("\nTotal cases in case base:", len(case_base))