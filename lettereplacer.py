message = raw_input("\nEnter a message. ")
character_to_remove = raw_input('\nWhich character would you like to remove from this message (leave blank if you do not want to remove any characters)? ')
character_to_replace = raw_input('\nWhich character would you like to replace that character (leave blank if you do not want to replace that character or if you have not removed anything)? ')
def letter_replacer(string,N,M):
    removed = string
    for char1 in string:
        if char1.upper() == N:
            removed = removed.replace(char1,M.upper())
        elif char1.lower() == N:
            removed = removed.replace(char1,M.lower())
    return removed
if len(character_to_remove) <= 1 and len(character_to_replace) <= 1:
        print "\nThis is your new message:  " + letter_replacer(message,character_to_remove,character_to_replace) + ".\n"
else:
    print "\nYou have not satisfied the conditions.\n"
