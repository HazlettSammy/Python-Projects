print("Welcome to my video game quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What was the first videogame? ")
if answer.lower() == "pong":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is SEGA's mascot? ")
if answer.lower() == "sonic":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("When did the playstation come out? ")
if answer.lower() == "1995":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is the most sold videogame? ")
if answer.lower() == "minecraft":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")