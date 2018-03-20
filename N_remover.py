word = raw_input("\nEnter a message. ")
def N_remover(string):
    removed = string
    N = ['n','N']
    for char1 in string:
        for char2 in N:
            if char1 == char2:
                removed = removed.replace(char1,"")
    return removed
print "\nThis is how you would have to say or write this message in China: \n" + N_remover(word) + ".\n"
