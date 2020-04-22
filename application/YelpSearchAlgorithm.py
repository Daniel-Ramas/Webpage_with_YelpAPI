import json, requests, os

def pullDataFromYelpAPI(term, limit, radius, sort_by, location):
	#Variables for Yelp search request
	#API KEY stored in environment variables
	API_KEY = os.environ.get('YELP_API_KEY')
	radius = radius * 1609
	if (radius > 40000):
		radius = 40000
	ENDPOINT = "https://api.yelp.com/v3/businesses/search"
	HEADERS = {'Authorization' : 'bearer %s' % API_KEY}
	PARAMETERS = {'term':term,
              'limit':limit,
              'radius':radius,
              'sort_by':sort_by,
              'location': location,
	}
	#Make a request to the YELP API
	response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

	#save data from API response into JSON dictionary
	business_data = response.json()
	#we only want the business info, save into another dictionary
	businesses = business_data['businesses']
	return businesses


