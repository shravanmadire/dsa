def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False

  s1s1 = s1 + s1
  return s2 in s1s1

# Test the function
print(is_rotation("waterbottle", "erbottlewat")) # True
print(is_rotation("abcde", "cdeab")) # True
print(is_rotation("abcde", "abced")) # False
print(is_rotation("abc", "bca")) # True
print(is_rotation("a", "a")) # True