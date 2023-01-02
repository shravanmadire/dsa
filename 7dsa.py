def prefix_to_infix(expression):
  # create a stack to store the operands and intermediate results
  stack = []

  # iterate over the characters in the expression in reverse order
  for char in reversed(expression):
    # if the character is an operand, push it onto the stack
    if char.isalpha():
      stack.append(char)
    # if the character is an operator, pop two operands from the stack and
    # create a new string with the operands and operator, and push it back onto the stack
    else:
      op1 = stack.pop()
      op2 = stack.pop()
      result = "(" + op1 + char + op2 + ")"
      stack.append(result)

  # the result should be the only element on the stack, so return it
  return stack[0]

# test the function
print(prefix_to_infix("+A*BC"))
print(prefix_to_infix("+*+A*BCDEF*G"))
print(prefix_to_infix("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))