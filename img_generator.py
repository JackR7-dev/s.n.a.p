import os
import config
from PIL import Image

output_path = "E:\Files\Programming\Projects\S.N.A.P. (Smart Neural Art Poster)\OUTPUT"
# getting the list of elements inside OUTPUT folder
dir_list = os.listdir(output_path)

# function that generate images based on prompt parameter. It cycle the image list directory so it can delete previuous generated images.
# Then it run a command line to generate images and save it in the OUTPUT folder
# CONTROLLARE L'ELIMINAZIONE DELLE IMMAGINI

def generate_images(prompt):
    for img in dir_list:
        os.remove(output_path + "\\" + img)
    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{config.bing_api}"'
    os.system(command)
    return os.listdir("OUTPUT")
    
# function that check if the generated images is corrupted or can't be opened
def verify_images(dir_list):
    for img in dir_list:
        try:
            img_check = Image.open(output_path + "\\" + img)
            img_check.verify()
        except:
            os.remove(output_path + "\\" + img)
    return True