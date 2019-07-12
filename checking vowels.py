z=['a','e','i','o','u','A','E','I','O','U']
al=input()
if al.isalpha():
  if al in z:
    print('vowel')
  else:
    print('Consonant')
else:
  print('Invalid')
