from constants import targetList
import re
listOne = [['lab 1', 'lab 2 (3%)', 'assignment 4', 'test',]]

# Initialize an empty list to store the modified sublists.
newList = []
# Create a regular expression pattern that matches any word in the targetList.
pattern = re.compile(r'\b(:' + '|'.join(map(re.escape, targetList.targetList)) + r')', re.IGNORECASE)
# Iterate through each sublist in the input list.
for i in range(len(listOne)):
    # Initialize an empty list to store modified words in the current sublist.
    modifiedSublist = []
    # Iterate through each word in the current sublist.
    for j in range(len(listOne[i])):
        # Split the current word into a list of words.
        # words = listOne[i][j].split()
        # Filter out words that are not in the targetList.
        # modifiedWords = [word for word in words if word.strip().lower() in targetList.targetList]
        # Join the modified words back into a string and append to the modifiedSublist.
        # modifiedSublist.append(' '.join(modifiedWords))
        # Find all occurrences of the pattern in the current word.
        matches = pattern.findall(listOne[i][j])
        # Append the matches to the modifiedSublist.
        modifiedSublist.extend(matches)
        print(modifiedSublist)