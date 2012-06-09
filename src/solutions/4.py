# Generate a list of all products of two 3-digit positive integers
products=[x*y for x in range(100, 1000) for y in range(100, 1000)]

# Get the palindromic subset
palindromic=[n for n in products if str(n)==str(n)[::-1]]

# Print the largest
print sorted(palindromic)[-1]
