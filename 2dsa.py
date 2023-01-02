def reverse_array_in_place(arr):
  # Get the length of the array
  n = len(arr)
  
  # Loop through the array, swapping the elements at the front and back
  for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

# Test the function
arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print(arr) # [5, 4, 3, 2, 1]