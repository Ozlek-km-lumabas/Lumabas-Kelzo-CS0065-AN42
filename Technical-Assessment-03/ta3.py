# ============================================================
# INTELLIGENT TUTORING SYSTEM
# CASE-BASED REASONING (CBR)
#
# Case Study 3: Intelligent Tutoring System
# ============================================================

# ============================================================
# PART 1 - CASE BASE
# ============================================================

# The case base contains previous student problems.
#
# Each case has:
# - topic
# - error
# - difficulty
# - solution

case_base = [

    {
        "problem": {
            "topic": "Fractions",
            "error": "Incorrect addition",
            "difficulty": "Easy"
        },
        "solution": "Review how to find common denominators and practice adding fractions."
    },

    {
        "problem": {
            "topic": "Fractions",
            "error": "Incorrect subtraction",
            "difficulty": "Medium"
        },
        "solution": "Practice finding common denominators and subtracting fractions."
    },

    {
        "problem": {
            "topic": "Algebra",
            "error": "Sign error",
            "difficulty": "Medium"
        },
        "solution": "Review positive and negative numbers and practice algebraic expressions."
    },

    {
        "problem": {
            "topic": "Algebra",
            "error": "Wrong formula",
            "difficulty": "Hard"
        },
        "solution": "Review the appropriate algebraic formula and solve guided examples."
    },

    {
        "problem": {
            "topic": "Geometry",
            "error": "Wrong formula",
            "difficulty": "Easy"
        },
        "solution": "Review basic area and perimeter formulas and complete simple geometry exercises."
    }

]

# ============================================================
# PART 2 - DISPLAY THE CASE BASE
# ============================================================

def display_case_base():

    print("\n==========================================")
    print("CURRENT CASE BASE")
    print("==========================================")

    for i, case in enumerate(case_base, start=1):

        problem = case["problem"]

        print(f"\nCase {i}:")
        print(f"  Topic: {problem['topic']}")
        print(f"  Error: {problem['error']}")
        print(f"  Difficulty: {problem['difficulty']}")
        print(f"  Solution: {case['solution']}")

# ============================================================
# PART 3 - GET NEW STUDENT PROBLEM
# ============================================================

def get_new_problem():

    print("\n==========================================")
    print("NEW STUDENT PROBLEM")
    print("==========================================")

    print("\nAvailable topics:")
    print("1. Fractions")
    print("2. Algebra")
    print("3. Geometry")

    topic_choice = input("\nChoose a topic (1-3): ")

    if topic_choice == "1":
        topic = "Fractions"

    elif topic_choice == "2":
        topic = "Algebra"

    elif topic_choice == "3":
        topic = "Geometry"

    else:
        print("Invalid choice. Using Fractions.")
        topic = "Fractions"

    print("\nAvailable error types:")
    print("1. Incorrect addition")
    print("2. Incorrect subtraction")
    print("3. Sign error")
    print("4. Wrong formula")

    error_choice = input("\nChoose an error type (1-4): ")

    if error_choice == "1":
        error = "Incorrect addition"

    elif error_choice == "2":
        error = "Incorrect subtraction"

    elif error_choice == "3":
        error = "Sign error"

    elif error_choice == "4":
        error = "Wrong formula"

    else:
        print("Invalid choice. Using Incorrect addition.")
        error = "Incorrect addition"

    print("\nAvailable difficulty levels:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty_choice = input("\nChoose difficulty (1-3): ")

    if difficulty_choice == "1":
        difficulty = "Easy"

    elif difficulty_choice == "2":
        difficulty = "Medium"

    elif difficulty_choice == "3":
        difficulty = "Hard"

    else:
        print("Invalid choice. Using Medium.")
        difficulty = "Medium"


    # Create the new problem dictionary
    new_problem = {
        "topic": topic,
        "error": error,
        "difficulty": difficulty
    }

    return new_problem

# ============================================================
# PART 4 - SIMILARITY ASSESSMENT
# ============================================================

def calculate_similarity(new_problem, old_problem):

    # Start with zero matching attributes
    score = 0

    # Check topic
    if new_problem["topic"] == old_problem["topic"]:
        score += 1

    # Check error type
    if new_problem["error"] == old_problem["error"]:
        score += 1

    # Check difficulty
    if new_problem["difficulty"] == old_problem["difficulty"]:
        score += 1

    # There are 3 attributes.
    # Convert the score into a percentage.
    similarity = (score / 3) * 100

    return similarity

# ============================================================
# PART 5 - RETRIEVE SIMILAR CASES
# ============================================================

def retrieve_cases(new_problem):

    results = []

    # Compare the new problem with every case
    for i, case in enumerate(case_base):

        similarity = calculate_similarity(
            new_problem,
            case["problem"]
        )

        results.append({
            "case_number": i + 1,
            "case": case,
            "similarity": similarity
        })

    # Sort from highest similarity to lowest similarity
    results.sort(
        key=lambda result: result["similarity"],
        reverse=True
    )

    return results

# ============================================================
# PART 6 - DISPLAY SIMILARITY RESULTS
# ============================================================

def display_similarity_results(results):

    print("\n==========================================")
    print("SIMILARITY RESULTS")
    print("==========================================")

    for result in results:

        print(
            f"Case {result['case_number']}: "
            f"{result['similarity']:.1f}% similarity"
        )

# ============================================================
# PART 7 - DISPLAY RETRIEVED CASE
# ============================================================

def display_retrieved_case(best_result):

    case = best_result["case"]
    problem = case["problem"]

    print("\n==========================================")
    print("MOST RELEVANT PAST CASE")
    print("==========================================")

    print(f"Similarity: {best_result['similarity']:.1f}%")

    print("\nPrevious Problem:")
    print(f"  Topic: {problem['topic']}")
    print(f"  Error: {problem['error']}")
    print(f"  Difficulty: {problem['difficulty']}")

    print("\nPrevious Solution:")
    print(f"  {case['solution']}")

# ============================================================
# PART 8 - ADAPT THE SOLUTION
# ============================================================

def adapt_solution(best_case, new_problem):

    # Get the previous solution
    original_solution = best_case["solution"]

    # Start with the previous solution
    adapted_solution = original_solution

    # Add personalized instructions based on difficulty
    if new_problem["difficulty"] == "Easy":

        adapted_solution += (
            " Start with simple guided examples "
            "before moving to harder exercises."
        )

    elif new_problem["difficulty"] == "Medium":

        adapted_solution += (
            " Complete 5 practice problems "
            "with moderate difficulty."
        )

    elif new_problem["difficulty"] == "Hard":

        adapted_solution += (
            " Complete challenging practice problems "
            "and review the solution step-by-step."
        )

    # Add feedback based on the type of error
    if new_problem["error"] == "Sign error":

        adapted_solution += (
            " Pay special attention to positive "
            "and negative signs."
        )

    elif new_problem["error"] == "Wrong formula":

        adapted_solution += (
            " Review how to identify the correct "
            "formula before solving."
        )

    elif new_problem["error"] == "Incorrect addition":

        adapted_solution += (
            " Check each addition step carefully."
        )

    elif new_problem["error"] == "Incorrect subtraction":

        adapted_solution += (
            " Check the subtraction steps and "
            "make sure the signs are correct."
        )

    return adapted_solution

# ============================================================
# PART 9 - DISPLAY ADAPTED SOLUTION
# ============================================================

def display_adapted_solution(solution):

    print("\n==========================================")
    print("ADAPTED FINAL SOLUTION")
    print("==========================================")

    print(solution)

# ============================================================
# PART 10 - RETAIN NEW CASE
# ============================================================

def retain_case(new_problem, final_solution):

    new_case = {
        "problem": new_problem.copy(),
        "solution": final_solution
    }

    # Add the new case to the case base
    case_base.append(new_case)

    print("\n==========================================")
    print("RETAIN STAGE")
    print("==========================================")

    print("✓ New case saved successfully!")
    print("✓ The case base has been updated.")

# ============================================================
# PART 11 - DISPLAY NEW CASE BASE
# ============================================================

def display_updated_case_base():

    print("\n==========================================")
    print("UPDATED CASE BASE")
    print("==========================================")

    for i, case in enumerate(case_base, start=1):

        problem = case["problem"]

        print(
            f"\nCase {i}: "
            f"{problem['topic']} - "
            f"{problem['error']} - "
            f"{problem['difficulty']}"
        )

        print(f"Solution: {case['solution']}")

# ============================================================
# MAIN PROGRAM
# ============================================================

print("==========================================")
print("INTELLIGENT TUTORING SYSTEM")
print("CASE-BASED REASONING")
print("==========================================")

print("\nThis system uses previous student cases")
print("to recommend a personalized learning solution.")

# Show original case base
display_case_base()

# ------------------------------------------------------------
# STEP 1: Get new problem
# ------------------------------------------------------------

new_problem = get_new_problem()

print("\n==========================================")
print("NEW PROBLEM ENTERED")
print("==========================================")

print(f"Topic: {new_problem['topic']}")
print(f"Error: {new_problem['error']}")
print(f"Difficulty: {new_problem['difficulty']}")

# ------------------------------------------------------------
# STEP 2: RETRIEVE
# ------------------------------------------------------------

results = retrieve_cases(new_problem)

display_similarity_results(results)

# ------------------------------------------------------------
# STEP 3: Get most similar case
# ------------------------------------------------------------

best_result = results[0]

display_retrieved_case(best_result)

# ------------------------------------------------------------
# STEP 4: REUSE + ADAPT
# ------------------------------------------------------------

final_solution = adapt_solution(
    best_result["case"],
    new_problem
)

display_adapted_solution(final_solution)

# ------------------------------------------------------------
# STEP 5: RETAIN
# ------------------------------------------------------------

retain_case(
    new_problem,
    final_solution
)

# ------------------------------------------------------------
# STEP 6: Display updated case base
# ------------------------------------------------------------

display_updated_case_base()

print("\n==========================================")
print("CBR PROCESS COMPLETE")
print("==========================================")

print("\nThe system has:")
print("1. Retrieved a similar past case.")
print("2. Reused its previous solution.")
print("3. Adapted the solution to the new problem.")
print("4. Retained the new case in the case base.")