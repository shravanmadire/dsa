def find_smallest(stack):
  # if the stack is empty, return None
  if not stack:
    return None

  # pop the top element from the stack
  top = stack.pop()

  # find the smallest element in the rest of the stack
  smallest = find_smallest(stack)

  # if the smallest element is smaller than the top element, push the top element back onto the stack
  if smallest and smallest < top:
    stack.append(top)
    return smallest
  # if the top element is smaller than the smallest element, or the stack was empty, return the top element
  else:
    return top

# test the function
stack = [5, 3, 7, 1, 9, 2]
print(find_smallest(stack))