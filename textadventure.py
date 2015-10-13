import sys
def dividetwonumbers(num1,num2):
	num3 = num1/num2
	return num3
def heighttocm(i):
	c = 2.54 * i 
	return c
def cakecalculation(people):
	flour = ((12 * people)/3) + 7
	return flour
def temptoF(Celcius):
	t = 9/5 * Celcius + 32
	return t
def main():
	fo = open("text1.txt","r")
	premise = fo.readline()
	print(premise)
	decision = input("Are you going to go the house? ")
	if decision == "no" or decision == "No" or decision == "Nope" or decision == "Nah":
		print("Okay...") 
		print("You decide to check the weather for tomorrow but being foriegn and just moving into Canada you need to change the units to fahrenheit")
		print("It being 55 degrees in celcius you look up a conversion on google and enter that number in.")
		Celcius = 1
		t =temptoF(55)
		print("Noticing that",t,"is way too hot to do anything you start regretting not going to the house.")
		sad = "Now you are at home all by your self and bored."
		print(sad)
		contimplate = input("Are you sure you don't want to go to the house? ")
		if contimplate == "no" or contimplate == "No" or contimplate == "Nope" or contimplate == "Nah":
			print("Okay then be that way..") 
		if contimplate == "yes" or contimplate == "Yes" or contimplate == "Yessir" or contimplate == "Why not" or contimplate == "Why not?":
			print("Too Late.")
		print("Yet you sit on your computer and realize that you are very hungry.")
		print("You decide to make a cake but you don't know how many cups of flower to add. Luckily your calculator has a cake to flour converter.")
		people = 1
		p = float(input("How many cakes are you making? "))
		flour = cakecalculation(p)
		print("Now that you know you need", flour,"cups of flour for your cakes you can continue your pathetic existince.")
	elif decision == "Yes" or decision == "yes" or decision == "Why not" or decision == "Why not?":
		print("Your friend is very exited and you and her proceed to walk in")
		print("As soon as you enter the house your friend gets scared and says,")
		quote = "I'm actually kinda scared I'm going inside, wanna play a game instead?"
		print(quote)
		import random
		number = random.randint(0,10)
		guess = int(input("Reluctantly agreeing you guess a number between 0 and 10: ")) 
		numFound = False 
		guesses = 1
		while guess != number and guesses < 10:  
			if guess > number:
				shesays1 = "You guessed too high"
				print(shesays1)
				guess = int(input("Guess again: "))
			else:
				print("You guessed too low")
				guess = int(input("Guess again: "))

			guesses = guesses + 1
		print("That's it. The number was",number)
		
		fo2 = open("text2.txt","r")
		premise2 = fo2.readline()
		print(premise2)
		
		answer1 = input("Do you want to play? ")
		
		if answer1 == "Yes" or answer1 == "yes" or answer1 == "Sure":
			fo3 = open("text3.txt","r")
			premise3 = fo3.readline()
			print(premise3)
			fo5 = open("text5.txt","r")
			premise5 = fo5.readline()
			print(premise5)
			riddleanswer = input("You answer: ")
			if riddleanswer == "Counterfit money" or riddleanswer == "counterfit money" or riddleanswer == "fake money":
				print('"Interesting... but let us try another one..."')
				fo6 = open("text6.txt","r")
				premise6 = fo6.readline()
				print(premise6)
				riddleanswer2 = input("You exclaim: ")
				while riddleanswer2 == "shoe" or riddleanswer2 == "Shoe" or riddleanswer2 == "boot" or riddleanswer2 == "kicks":
					print('"Alright, you win... you can have your friend back."')
					print("You and your friend decide to not stay and walk out happily ever after")
					sys.exit(0)
				else:
					while riddleanswer2 != "shoe" or riddleanswer2 != "Shoe" or riddleanswer2 != "boot" or riddleanswer2 != "kicks":
						print('"WRONG! HAHA... wanna try again"')
						tryagain2 = input("You angrily respond: ")
			while riddleanswer != "Counterfit money" or riddleanswer != "counterfit money" or riddleanswer != "fake money":
				print('"Wrong but try again."')
				tryagain = input("You say the answer is: ")
		elif answer1 == "no" or answer1 == "No" or answer1 == "Nope":
			fo4 = open("text4.txt","r")
			premise4 = fo4.readline()
			print(premise4)
			caviate = "Luckily you have a calculator with a function specifically for converting measurements"
			print(caviate)
			i = 1
			m = float(input("Your calculator asks for your height in inches: "))
			c = heighttocm(m)
			print("You exclaim", c,"cm in the air.")
			print('As soon as you star questioning why the voice asked you for your height he interupts saying: "Now give me your two favorite numbers and divide them"')
			print("Still questioning the logic you pull out your calculator and")
			num1 = int(input("Enter one of your favorite numbers: "))
			num2 = int(input("Enter one of your other favorite numbers: "))
			num3 = dividetwonumbers(num1,num2)
			print('You respond, I do not understand why you ask but my favorite numbers are', num1, 'and', num2, 'thus dividing them equals:', num3)
			print('He responds, "Cool! now I finished my taxes! You can have your friend back!"')
			print("You and your friend decide to not stay and walk out happily ever after but very confused.")
main()
		
	
