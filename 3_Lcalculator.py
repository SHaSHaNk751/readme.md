print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_name=name1+name2
lower_case=combined_name.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
true=str(t+r+u+e)
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
love=str(l+o+v+e)
Sum=int(true+love)
if Sum<10 or Sum>90:
    print(f"Your score is {Sum}, you go together like coke and mentos.")
elif Sum>=40 and Sum<=50:
    print(f"Your score is {Sum}, you are alright together.")
else:
    print(f"Your score is {Sum}.")