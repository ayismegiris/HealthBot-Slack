import random
import time
import requests
import json
import csv
import os
from random import shuffle
import pickle
import os.path
import datetime

from User import User

# Environment variables must be set with your tokens
USER_TOKEN_STRING =  os.environ['SLACK_USER_TOKEN_STRING']
URL_TOKEN_STRING =  os.environ['SLACK_URL_TOKEN_STRING']

def main():
    bot = Bot()