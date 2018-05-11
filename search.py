import re

def generate_pattern(pat):
    # Split each word when encounter space
    pat_split = (pat.lower()).split(" ")
    pattern = ""

    # Add all between words
    for i in range(len(pat_split)):
        pattern += (".*" + pat_split[i])
    pattern += ".*"

    # Compile pattern into regex pattern
    regex = re.compile(pattern)
    
    return regex

# Input the keyword
keyword = input('Input the keyword to be searched in goal.com\n')
# Read from heading.txt line by line
lines = [line.rstrip('\n') for line in open('heading.txt')]
# Seperate the header with it's content
contents = [line.split(' ||| ') for line in lines]
# Variable that keep the SEO's value
value = 0
# Variable that keep keyword's appearance in header
counter = 0

# Compile regex with keyword
regex = generate_pattern(keyword)
for content in contents:
    if regex.match(content[1].lower()):
        print(content)
        counter += 1
        if content[0] == 'h1':
            value += 10
        if content[0] == 'h2':
            value += 5
        if content[0] == 'h3':
            value += 2
    

print(keyword + '\'s appearance is ' + str(counter))
print("Value of this page is " + str(value))
