def first_non_repeated(string):
  # create a dictionary to store the count of each character
  char_count = {}

  # iterate over each character in the string
  for char in string:
    # if the character is not in the dictionary, add it and set the count to 1
    if char not in char_count:
      char_count[char] = 1
    # if the character is already in the dictionary, increment the count by 1
    else:
      char_count[char] += 1

  # iterate over each character in the string again
  for char in string:
    # if the count of the character is 1, return it
    if char_count[char] == 1:
      return char

  # if no non-repeated characters are found, return None
  return None

# test the function
print(first_non_repeated("abcdeffghijklmnopqrstuvwxyz"))
print(first_non_repeated("aabbccddeeffgg"))
print(first_non_repeated("abcdefg"))