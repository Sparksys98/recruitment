def main():
	print("Welcome to the special recruitment program, please answer the following questions:")
	name=input("What's your name? ")
	age=int(input("How old are you? "))
	experience=int(input("How many years of experience do you have? "))

	skills=["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv={
	"name":name,
	"age": age,
	"year": experience,
	"skills": []
	}
	for num,let in enumerate(skills,1):
		print (num,let)
	choice1=int(input("Choose a skill from above by entering its number: "))
	choice2=int(input("Choose another skill from above by entering its number: "))
	cv["skills"].append(skills[choice1-1])
	cv["skills"].append(skills[choice2-1])
	print (cv["skills"])
	if(40 >cv["age"] > 25 and experience>5 and "Eating" in cv["skills"]):
		print("accepted")
	else:
		print("rejected")
if __name__ == '__main__':
	main()
