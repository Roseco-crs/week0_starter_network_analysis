#  SlackDataLoader class
import os
import pandas as pd
from src.loader import SlackDataLoader
import src.utils as utils
#import src.loader as loader
import sys

# Add parent directory to path to import modules from src
rpath = os.path.abspath('../data/anonymized/')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

print(rpath)

pathh = os.getcwd()
print(pathh)


# # create an instance of SlackDataLoader
# data_loader = SlackDataLoader(rpath)
# print(data_loader)
# # Load data from a Slack channel
# # slack_data_user = data_loader.get_users()
# # slack_data_channel = data_loader.get_channels()
# # slack_data_usermap = data_loader.get_user_map()
# #print(slack_data_channel)


