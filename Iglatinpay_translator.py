pyg = 'ay'
original = raw_input('\nEnter a word to translate into Pyglatin: ')
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
if len(original) > 0 and original.isalpha():
  print '\nThis is your word in pyglatin (or iglatinpay): \n' + str(new_word) + '.\n'
else:
  print '\nNot a word\n'
