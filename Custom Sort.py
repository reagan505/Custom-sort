def custom_sort(data, sort_key): #defined custom_sort

    sorted_list = sorted(data, key=lambda x: x[sort_key]) #returns a new sorted list
    return sorted_list # returns the sorted list of dictionaries.

# List of dictionaries
data = [
    {"name": "Alice", "age": 64},
    {"name": "Bob", "age": 28},
    {"name": "Charlie", "age": 35}
]

# Call the function and sort by 'age'
result = custom_sort(data, "age")

# Print the sorted result
print(result)
