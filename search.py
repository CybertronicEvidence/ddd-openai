import os
import openai
import config
# import configparser

# from dotenv import load_dotenv

# def configure():
#   load_dotenv()
  
openai.api_key = config.OPENAI_API_KEY
# os.getenv('OPENAI_API_KEY')

# def get_api_key():
#   config = configparser.ConfigParser()
#   config.read('config.ini')
#   return config[openai][OPENAI_API_KEY]

# openai.api_key = get_api_key()  

def generateBlogTopics(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="{}.".format(prompt1),
      temperature=0.7,
      max_tokens=3997,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
