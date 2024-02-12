import decimal
import requests
import requests_cache
import json

requests_cache.install_cache('image_cache', backend='sqlite')




# def get_pokemon_data(name):
#     """Fetch data for a given Pokémon by name from the Poke API."""
#     url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         image_url = data['sprites']['front_default']
#         return {
#             'name': name,
#             'image_url': image_url,
            
#         }
#     else:
#         return None  




def get_image(search):
    # 4 parts to every api
    # url required 
    # queries/parameters optional
    # headers/authorization optional
    # body/postin optional

    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
        "X-RapidAPI-Key": "d18640d5c3msh4b7d0dbe1530c4cp1f097fjsncbb8d6552706",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url

# def get_google_custom_search_image(search_term, api_key, cse_id):
#     
#     url = "https://www.googleapis.com/customsearch/v1"
    
#     
#     params = {
#         "q": "pokemon",  # The search term
#         "cx": "30cbfd08c3c8a4f30",      #  Custom Search Engine ID
#         "key": "AIzaSyDIUoLiqb4GCifcxDryMB3xkGdVaWUL7K4",    #  API key
#         "searchType": "image",  # Specify image search
#         "num": 1  # Number of results to return (1-10)
#     }
    
#     # Make the API request
#     response = requests.get(url, params=params)
    
#     
#     data = response.json()
    
#     
#     img_url = ""
#     if "items" in data and len(data["items"]) > 0:
#         img_url = data["items"][0]["link"]
    
#     return img_url

# image_url = get_google_custom_search_image("q", "key", 'cx')
# print(f"Image URL: {image_url}")





class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it

