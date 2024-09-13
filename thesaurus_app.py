from random import random
import random
thesaurus = {
    "hot": ["balmy", "summery", "tropical", "boiling", "scorching"],
    "cold": ["chilly", "cool", "freezing", "fridge", "polar"],
    "happy": ["content", "cherry", "merry", "jovial", "jocular"],
    "sad": ["unhappy", "downcast", "miserable", "glum", "meloncoly"],
}

print("Welcome to the Thesaurus App")
print("\nChoose a word from the thesaurus and I'll give you a synonym")
print("\nHere are the words in the thesaurus ")
for key in thesaurus.keys():
    print("\t-" + key)

choice = input("\nWhat words would you like to a synonym for: ").lower()

if choice in thesaurus.keys():
    index = random.randint(0, 4)
    print("\nA synonym for", choice, "is " + str(thesaurus[choice][index]) + ".")
else:
    print("\nWord not found in thesaurus.")

    question = input("\nWould you like to see the entire thesaurus? (y/n): ").lower().strip()

    if "y" in question:
        for key, values in thesaurus.items():
            print("\n" + key.title() + " synonyms are: ")
            for value in values:
                print("\t-" + value)
    else:
        print("I hope you enjoyed the app")
