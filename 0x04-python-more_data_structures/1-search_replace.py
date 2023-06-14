#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new = []

    # Iterate over each element in the input list
    for item in my_list:
        # Check if the element matches the search value
        if item == search:
            # Replace the element with the replace value
            new.append(replace)
        else:
            # Keep the element as is
            new.append(item)

    return new
