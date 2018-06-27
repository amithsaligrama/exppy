base_y = raw_input("\nWhat integer base do you want to have your result in? Base ")
base_x = raw_input("\nWhat integer base do you want to have your start number be before I turn it into base " + str(base_y) + "? Base ")
base_x_num = raw_input("\nWhat integer in base " + str(base_x) + " do you want to convert to base " + str(base_y) + "? ")
def convert_from_base(num,base):
  return int(num, base)
def convert_to_base(num,base):
    if num == 0:
        return '0'
    nums = []
    while num:
        num, r = divmod(num, base)
        nums.append(str(r))
    return ''.join(reversed(nums))
base_10_of_x = convert_from_base(base_x_num, int(base_x))
print "\n%s in base %s is %s in base %s which is %s in base 10\n" % (base_x_num, base_x, convert_to_base(base_10_of_x, int(base_y)), base_y, base_10_of_x)
