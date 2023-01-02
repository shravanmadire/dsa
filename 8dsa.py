def check_brackets(code):
  # create a stack to store the open brackets
  stack = []

  # define a dictionary that maps open brackets to closed brackets
  brackets = {"(": ")", "[": "]", "{": "}"}

  # iterate over each character in the code
  for char in code:
    # if the character is an open bracket, push it onto the stack
    if char in brackets:
      stack.append(char)
    # if the character is a closed bracket, check if it matches the last open bracket on the stack
    elif char in brackets.values():
      # if the stack is empty or the brackets don't match, return False
      if not stack or char != brackets[stack.pop()]:
        return False

  # if the stack is empty, all the brackets have been matched, so return True
  return not stack

# test the function
print(check_brackets("(a + b) * c"))
print(check_brackets("(a + b * [c + d]}"))
print(check_brackets("{a + b * [c + d]}"))
print(check_brackets("a + b * c + d"))