# Colton DeWitt - April 28, 2022
dict_seasons_titles = {}  # Initialize empty dictionary for seasons key and titles value

with open(input()) as input_file:  # Open the file input and read in the strings of seasons and titles
    list_seasons_titles = input_file.readlines()
print(list_seasons_titles)


# Remove the \n from each element
list_index = 0  # Iteration index
for element in list_seasons_titles:  # Was originally element.removesuffix('\n') But zyBooks didn't like that
    list_seasons_titles[list_index] = element.replace('\n', '')
    list_index += 1


# Remove the 0's from in front of the single digit number for each seasons key
forbidden_seasons = {'01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '06':'6', '07':'7', '08':'8', '09':'9'}
list_index = 0  # Iteration index
for element in list_seasons_titles:
    if element in forbidden_seasons:
        # Replace the 0's for just the single number
        list_seasons_titles[list_index] = element.replace(element, forbidden_seasons[element])
    # Doesn't replace anything if str not in there
    list_index += 1


# Make the dictionary. Keys are the seasons, the very next element after the seasons number is the value, title
# I am converting the seasons into ints because when sorting the dictionary later it works better than strings
list_index = 0  # Iteration index
while list_index <= len(list_seasons_titles) - 2:  # Skip over the titles
    if int(list_seasons_titles[list_index]) in dict_seasons_titles:  # If title entry already exists in that seasons key
        titles = dict_seasons_titles[int(list_seasons_titles[list_index])]
        titles.append(list_seasons_titles[list_index + 1])  # Append next title to already exists value of seasons key
    else:
        titles = [list_seasons_titles[list_index + 1]]  # Else make a new title list as the value of that seasons key
        dict_seasons_titles[int(list_seasons_titles[list_index])] = titles

    list_index += 2  # Increment by 2 to skip over the titles


#print(list_seasons_titles)  Incremental programming
#print(dict_seasons_titles)  Incremental programming

# Sort the key seasons from least to greatest. Then, turn back into dictionary, since tuples generated
dict_seasons_titles = dict(sorted(dict_seasons_titles.items()))
#print(dict_seasons_titles)  Incremental programming


# Write to a new file for the seasons and their titles
with open('output_keys.txt', 'w') as w_file:
    for seasons, title_list in dict_seasons_titles.items():
        w_file.write('{}:'.format(str(seasons)))  # Write the season key converted back into string
        for title in title_list:  # Iterate over the values of the dict which are lists with titles in them
            if title == title_list[len(title_list) - 1]:
                w_file.write(' {}\n'.format(title))  # Must end with new line if last title of the key
            else:
                w_file.write(' {};'.format(title))

# Time to separate out the titles from the dictionary
list_of_titles = [title_list for title_list in dict_seasons_titles.values()]  # Get only lists with titles in them
#print(list_of_titles)  Incremental programming
just_titles = []  # Initialize an empty list for just the titles not in lists. Titles as their own element
for list_element in list_of_titles:  # Iterate through each list
    for title in list_element:  # Iterate through each title in each list
        just_titles.append(title)  # Append the title name onto the just_titles list


just_titles.sort()  # Sort the just_titles list alphabetically
#print(just_titles)  Incremental programming


# Write to a new file 2 for just the titles
with open('output_titles.txt', 'w') as w_file2:
    for title in just_titles:  # Iterate through each title and write to the file
        w_file2.write('{}\n'.format(title))
