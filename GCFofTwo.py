def gcf(a,b):
    while (4==4):
        if (a == 0 or b == 0 or a == b):
            return max(a,b);
        elif (a > b):
            a = a % b
        else:
            b = b % a
print ("This is a GCF calculator. This only works for 2 integers")
a = int(input("Enter the first number. "))
b = int(input("Enter the second number. "))
print ("The GCF is " + str(gcf(a,b)) + ".")
