questions = ("10 + 10 = ",
             "11 / 11 = ",
             "20 - 10 = ",
             "30 / 15 = ",
             "3 * 3 = ")

options = (("A. 12 ", "B. 18 ", "C. 30 ", "D. 20 ", "E. 11 "),
           ("A. 1 ", "B. 2", "C. 3", "D. 4", "E. 5"),
           ("A. 11", "B. 10", "C. 23", "D. 9", "E. 5"),
           ("A. 2", "B. 0", "C. 3", "D. 4", "E. 1"),
           ("A. 1", "B. 27", "C. 9", "D. 15", "E. 19"))

answers = ("D", "A", "B", "A", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Ketikkan Jawaban Anda (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 20
        print("BENAR!")
    else:
        print("SALAH!")
        print(f"Jawaban Yang Benar Adalah {answers[question_num]}.")
    question_num += 1

print("--------------------------------------------------")
print("-----------------------HASIL----------------------")
print("--------------------------------------------------")
print("Jawaban: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Tebakanmu: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print("SEMUA PERTANYAAN TELAH DIJAWAB")
print(f"TOTAL POINT YANG KAMU PEROLEH ADALAH {score}!")
