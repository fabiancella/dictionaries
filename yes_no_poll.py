from itertools import count

print("Welcome to the Yes or No Polling App")

voters = {}
issue = input("What is the yes or no issue you will be voting on today: ").title()
num_voters = int(input("How many people will be voting: "))
password = input("Enter a password for the polling result: ")


for num in range(num_voters):
    name = input("\nEnter your full name: ").title()
    print("Here is our issue:", issue)
    choice = input("What do you think, yes or no: ").lower()
    voters[name] = choice


print("\nThe following", num_voters, "people voted.")
for keys in voters.keys():
    print(keys)

print("\nOn the following issue:", issue)

yes_count = list(voters.values()).count("yes")
no_count = list(voters.values()).count("no")
value = voters.values()
if no_count < yes_count:
    print("Yes wins!", yes_count, "to", no_count)
elif no_count > yes_count:
    print("No wins!", no_count, "to", yes_count)
else:
    print("It's a tie!", yes_count, "to", no_count)

password_enter = input("\nPlease input password to see polling results: ")
if password in password_enter:
    for keys in voters.keys():
        print("voter:", keys, "\t\t\tVote: ", list(voters.values())) # this is wrong
else:
    print("BRUH HELL NAH")
