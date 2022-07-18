# Check the given string is palindrom or not using Recursion --------------------
# Palindrom - MAPAM
# Not Palindrom - MAPZM
def palindrom(str):
  if str == '':
    return True
  if len(str) == 1:
    return True
  if str[0] == str[-1] and palindrom(str[1:-1]):
    return True
  else:
    return False
print(palindrom('MACCAM'))