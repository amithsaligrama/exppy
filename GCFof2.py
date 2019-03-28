def gcf(a,b):
    while (4==4):
        if (a == 0 or b == 0 or a == b):
            return max(a,b);
        elif (a > b):
            a = a % b
        else:
            b = b % a
print ("\nThis is a GCF calculator. This only works for 2 integers")
a = int(input("\nEnter the first number. "))
b = int(input("Enter the second number. "))
print ("\nThe GCF is " + str(gcf(a,b)) + ".")
