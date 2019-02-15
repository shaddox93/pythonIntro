# acronym.py
# a program that comes up with an acronym for a phrase
# CS160-1PM - Victor Stasek

# The acronym(modPhrase) function takes a string and converts it to an acronym
def acronym(modPhrase):
    # Create an empty list called acronym
    acronym = []
    # For each iteration through loop:
    # 1. Assign the first letter of each word in the phrase (i[0]) to firstLetter
    # 2. Append firstLetter to empty list acronym
    for i in modPhrase.upper().split():
        firstLetter = i[0]
        acronym.append(firstLetter)
    # Join the contents of the list acronym into one string
    acronym = "".join(acronym)
    return acronym


def main():
    phrase = input("Enter phrase: ")
    phrase = acronym(phrase)
    print(phrase)
    
main()
