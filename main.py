import tweepy
import schedule
import time
import os
import random
import config
import twitter_auth
import img_generator
import img_upload
import prompt_reader
from PIL import Image

file_path = prompt_reader.file_path
dir_list = img_generator.dir_list

prompt_reader.load_template(file_path)
prompt = prompt_reader.generate_random_prompt(prompt_reader.categories)
modified_prompt = prompt_reader.modify_random_prompt(prompt)
# img_generator.generate_images(prompt)
img_generator.verify_images(dir_list)
media_id = img_upload.upload_img_and_return_id()

# creating the tweet and passing the media id as a list even if it's only one string. 
# The function create_tweet require a list when passing a media_ids parameter
twitter_auth.client.create_tweet(text=modified_prompt, media_ids=[media_id])

print("Tweeted")