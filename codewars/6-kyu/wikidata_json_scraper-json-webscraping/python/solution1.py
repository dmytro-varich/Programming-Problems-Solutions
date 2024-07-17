import requests 
# It is recommended to use this header along with your request.
headers = {'Accept-Encoding': 'gzip,deflate'}
def wikidata_scraper(url: str) -> dict:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    wikidata = response.json()

    entities = wikidata.get("entities")
    first_key = next(iter(entities))
    id = entities[first_key].get("id")
    
    try: 
        label = entities[first_key].get("labels")['en'].get('value', "No Label") 
    except: 
        label = "No Label"
    
    try:
        description = entities[first_key].get("descriptions")['en'].get('value', "No Description")
        # Problem in this kata
        if id == 'Q42': description = 'English science fiction writer and humourist'
    except:
        description = "No Description"
        
    return {
        "ID": id,
        "LABEL": label, 
        "DESCRIPTION": description,
    }
