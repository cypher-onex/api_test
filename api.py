import requests


url = "https://api.yelp.com/v3/businesses/search"
api_key = "L5MDbCmAuAejzpitCGdm5NBF4Kv6wFfAHAR8NQ5M58nqNb5Lo9AnnZ5AbbeeBigAAR9XDWC1DqyHoOaBDZjzXLUonalm7BXfyH9nVlLE0gH3T0i7qAd3oVH-AN-oYXYx"
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "Burger",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
print(businesses)
