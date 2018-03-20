def convert_to_base(num,base):
    if num == 0:
        return '0'
    nums = []
    while num:
        num, r = divmod(num, base)
        nums.append(str(r))
    return ''.join(reversed(nums))
base_x = int(raw_input("\nWhat integer base do you want to have your result in? "))
base_10_num = int(raw_input("\nWhat integer from base 10 do you want to put into base " + str(base_x) + "? "))
if base_x <= 0:
  print "You cannot have a base that is not positive."
elif base_10_num
print "\nThis is " + str(base_10_num) + " in base " + str(base_x) + ": " + str(convert_to_base(base_10_num,base_x)) + "\n."
