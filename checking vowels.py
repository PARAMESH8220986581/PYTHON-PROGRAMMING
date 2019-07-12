z=['a','e','i','o','u','A','E','I','O','U']
al=input()
if al.isalpha():
  if al in z:
    print('vowels')
  else:
    print('Consonants')
else:
  print('invalid')
