my_dict = {
    'Which company produces the legendary crossover with the model name "Land Cruiser"?\nA) Honda\nB) Toyota\nC) Ford': [
        "B",
        "Toyota",
    ],
    "Which well-known competition involving red and yellow cards takes place on tracks and roads?\nA) Formula One\nB) NASCAR\nC) MotoGP": [
        "A",
        "Formula one",
    ],
    "What color indicates that a car is moving in reverse?\nA) Red\nB) White\nC) Green": [
        "B",
        "White",
    ],
    "Which animal's name became the logo for Ferrari?\nA) Lion\nB) Horse\nC) Bull": [
        "B",
        "Horse",
    ],
    'Complete the famous phrase: "The unit of force is..."\nA) Joule\nB) Watt\nC) Newton': [
        "C",
        "Newton",
    ],
    "What planet is the third from the Sun?\nA) Mars\nB) Venus\nC) Earth": [
        "C",
        "Earth",
    ],
    "What car brand is known for its four interlocking silver rings logo?\nA) BMW\nB) Audi\nC) Mercedes-Benz": [
        "B",
        "Audi",
    ],
}


list_q = [
    'Which company produces the legendary crossover with the model name "Land Cruiser"?',
    "Which well-known competition involving red and yellow cards takes place on tracks and roads?",
    "What color indicates that a car is moving in reverse?",
    "Which animal's name became the logo for Ferrari?",
    'Complete the famous phrase: "The unit of force is...',
    "What planet is the third from the Sun?",
    "What car brand is known for its four interlocking silver rings logo?",
]


answer_list = []


def start_game():
    introduction = (
        "*** QUIZ GAME *************************************************************\n"
        "*                                                                         *\n"
        "*  I'm happy to welcome you to our game.                                  *\n"
        "*  There are 7 exciting questions waiting for you.                        *\n"
        "*  Choose the correct answer by typing the corresponding letter or word.  *\n"
        "*  Good luck!                                                             *\n"
        "*                                                                         *\n"
        "***************************************************************************"
    )
    return introduction


def request_input():
    right = 0

    for index, (key, value) in enumerate(my_dict.items(), start=1):
        user_response = input(f"Q{index}. {key}\n" f"Enter your answer: ")

        if user_response.lower() in [i.lower() for i in value]:
            right += 1
            status = "Correct"
            print("Correct!\n")
        else:
            status = "Wrong"
            new_value = ": ".join(value)

            print(f'Incorrect. Correct answer: "{new_value}"\n')

        answer_list.append(
            f"Q{index}: {list_q[index - 1]};\n"
            f"Your Answer: {user_response};\n"
            f"Correct Answer: {value[0]} : {value[1]}; Status: {status}"
        )
    print(f"Game over! Correct answers: {right}. Wrong answers: {7 - right}.")

    word = "** *SUMMARY* **"
    print(f"{word}")

    for element in answer_list:
        print(f"{element}")


def main():
    print(start_game())
    request_input()
    while True:
        response = input("Do you want to play again? Yes or No: ")
        response_lower = response.lower()
        if response_lower == "no":
            print("Thank you!")
            break
        elif response_lower == "yes":
            answer_list.clear()
            request_input()
        else:
            print("Your answer is incorrect.")


main()
