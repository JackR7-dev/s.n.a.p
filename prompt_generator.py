import random

file_path = 'E:\Files\Programming\Projects\S.N.A.P. (Smart Neural Art Poster)\prompt_generator.txt'
category_list_names = []
hashtag_symbol = '#'
categories = {}
random_prompt = ''

# loading the file for the prompt generation
def load_template(file_path):   
    current_category = None
    with open(file_path, 'r') as file_template:
        for line in file_template:
                if line.startswith('# '):
                     current_category = line[2:len(line)-1]
                     categories[current_category] = []
                elif line != '\n':
                    if current_category: 
                        categories[current_category].append(line[:len(line)-1])                   

# function that generate a random prompt using the file prompt_generator.txt
def generate_random_prompt(categories):
    #random_prompt = 'ok. water'
    random_prompt = random.choice(list(categories.get('Scenes'))) + " there is " + random.choice(list(categories.get('Objects'))) + ". " + random.choice(categories.get('Styles')) + " " + random.choice(list(categories.get('Colors')))
    return random_prompt

# function that return a string already formatted for the text of the tweet. After a dot it will capitalize the next char and add a new paragraph.
def modify_random_prompt(random_prompt):
    modified_prompt = []
    capitalize_next = True
    index = 0
    
    for char in random_prompt:
        if  char == " " and random_prompt[index-1] == ".":
             modified_prompt.append('\n')
             capitalize_next = True
             index += 1

        if char == '\n':
             capitalize_next = True
        if capitalize_next and char.isalpha():
              modified_prompt.append(char.upper())
              capitalize_next = False
              index += 1
        else: 
            modified_prompt.append(char)
            index += 1
    return ''.join(modified_prompt + list("."))