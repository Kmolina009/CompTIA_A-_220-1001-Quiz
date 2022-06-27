#Initial
Quesitons = [
    ("What's is TCP 22","Secure Shell"),
    ("What's is TCP 23","Telnet"),
]

for question, correct_answer in Quesitons:
    answer = input(f"{question}?")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        