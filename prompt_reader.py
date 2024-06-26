import random
import os

file_path = 'E:\Files\Programming\Projects\S.N.A.P. (Smart Neural Art Poster)\prompt_generator.txt'
category_list = []
category_search = '#'

# loading the file for the prompt generation
def load_template(file_path):
    with open(file_path, 'r') as file_template:
        for line in file_template:
            if category_search in line:
                category_list.append(line[2:len(line)-1])
 
load_template(file_path)
print(category_list)