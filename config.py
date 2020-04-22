import os 

#obtain API Key from environment variables
class Config(object):
	API_KEY = os.environ.get('YELP_API_KEY')
	