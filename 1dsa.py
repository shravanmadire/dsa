def find_pairs(arr, target_sum):
  # Create a set to store the pairs
  pairs = set()

  # Loop through each element in the array
  for i in range(len(arr)):
    # Get the difference between the target sum and the current element
    diff = target_sum - arr[i]

    # If the difference is in the array and is not the current element, add it to the pairs set
    if diff in arr and diff != arr[i]:
      pairs.add((arr[i], diff))

  # Return the pairs
  return pairs

# Test the function
print(find_pairs([1, 2, 3, 4, 5], 5))  # should print {(2, 3)}
print(find_pairs([1, 2, 3, 4, 5], 6))  # should print {(1, 5), (2, 4)}
print(find_pairs([1, 2, 3, 4, 5], 7))  # should print {(2, 5), (3, 4)}
print(find_pairs([1, 2, 3, 4, 5], 8))  # should print {(3, 5)}