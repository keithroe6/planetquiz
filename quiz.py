import math
print("Welcome to my computer quiz")

playing = input("Do you want to try the quiz? ")

if playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "yeah":
    print("Good! Let's try it!")
    
else:
    print("No problem! Another time then ;-) ")
    quit()

score = 0


print("Hint: All of the answers are planets.")
print("Good Luck!")

answer = input("What is the hottest planet in our solar system? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has the shortest year? ")
if answer.lower() == "mercury":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has life? ")
if answer.lower() == "earth":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("To which planet did NASA send the rover named Opportunity? ")
if answer.lower() == "mars":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has a moon named Titan? ")
if answer.lower() == "saturn":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has a huge storm called the Great Red Spot? ")
if answer.lower() == "jupiter":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has caused the most bad jokes? ")
if answer.lower() == "uranus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet was found by mathematical calculations? ")
if answer.lower() == "neptune":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is the smallest planet in our solar system? ")
if answer.lower() == "mercury":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which is the second smallest planet? ")
if answer.lower() == "mars":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is the brightest planet in Earth's night sky? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which is larger Neptune or Saturn? ")
if answer.lower() == "saturn":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Voyager 2 is the only spacecraft to flyby which planet? ")
if answer.lower() == "uranus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet have we sent the most robots to? ")
if answer.lower() == "mars":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet is closest in size to Earth? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet does the moon Phobos orbit? ")
if answer.lower() == "mars":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has the most moons? ")
if answer.lower() == "saturn":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has supersonic winds? ")
if answer.lower() == "neptune":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has the fastest rotation? ")
if answer.lower() == "jupiter":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is the densest planet in our solar system? ")
if answer.lower() == "earth":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet is known as the Morning Star? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet is known as the Evening Star? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet has the most volcanoes? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet spins backwards? ")
if answer.lower() == "venus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("What is our only ex-planet? ")
if answer.lower() == "pluto":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer = input("Which planet rotates on its side? ")
if answer.lower() == "uranus":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answerfav = input("What is your favorite planet? ")
print(f"Nice! {answerfav} is a great choice!")
score += 1

print("You got " + str(score) + " questions correct!")
print("You got " + str(round((score/27)* 100)) + " %")
