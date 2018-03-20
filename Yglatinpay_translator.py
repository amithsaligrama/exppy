pyg = 'ay'
original = raw_input('\nEnter a word to translate into pyglatin: ')
word = original.lower()
first = word[0]
new_word = word + first + pyg
Pyglatin = new_word[1:len(new_word)]
if len(original) > 0 and original.isalpha():
  print '\nThis is your word in pyglatin (or iglatinpay): %s' % (Pyglatin)
else:
  print '\nNot a word\n'
