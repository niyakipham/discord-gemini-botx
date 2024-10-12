import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DISCORD_SDK = config['DEFAULT']['discord_sdk']
