score = 0

answer1 = input("Question 1: What is the capital of France? ")
if answer1.lower().strip() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")


answer2 = input("Question 2: What planet is known as the Red Planet? ")
if answer2.lower().strip() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.")


answer3 = input("Question 3: What is 5 + 7? ")
if answer3.strip() == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 12.")


print(f"\nGame Over! Your final score is: {score}/3")