def reverse_stack(stack):
  # if the stack is empty, return it as is
  if not stack:
    return stack

  # pop the top element from the stack
  top = stack.pop()

  # reverse the rest of the stack
  reverse_stack(stack)

  # insert the top element at the bottom of the stack
  insert_at_bottom(stack, top)

def insert_at_bottom(stack, element):
  # if the stack is empty, push the element onto it
  if not stack:
    stack.append(element)
    return

  # pop the top element from the stack
  top = stack.pop()

  # insert the top element at the bottom of the stack
  insert_at_bottom(stack, element)

  # push the top element back onto the stack
  stack.append(top)

# test the function
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)