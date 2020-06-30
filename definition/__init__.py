import os
import requests
from bs4 import BeautifulSoup
import json
# from functools import lru_cache

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(word):
    json_path = os.path.join(ROOT_DIR, "cache.json")
    try:
        with open(json_path, "r") as fin:
            data = json.load(fin)
        text = data[word]
    except Exception as ex:
        text = ""
    return text

def add_data(word, text):
    json_path = os.path.join(ROOT_DIR, "cache.json")
    try:
        with open(json_path, "r") as fin:
            data = json.load(fin)
        data[word] = text
        with open(json_path, "w") as fout:
            json.dump(data, fout, indent=4, sort_keys=False)
    except Exception as ex:
        print(ex)
        pass
    return text

        
def definition(w, max_type_count = 2 , max_def_count = 2, force=False):

    if not force:
        return_text = get_data(w)
        if len(return_text):
            return return_text
    return_text = "Definition for {}\n".format(w)
    raw = requests.get('https://www.dictionary.com/browse/' + w).content
    soup = BeautifulSoup(raw, 'lxml')
    target_div = soup.find('div', {'class': 'css-1urpfgu e16867sm0'})

    all_types = target_div.find_all('span', {'class': 'luna-pos'})
    all_contents = target_div.find_all('div', {'class': 'css-1o58fj8 e1hk9ate4'})

    if not all_types:
        # print('no results found for ' + w)
        return_text = 'no results found for ' + w
        return return_text

    n = min(max_type_count, len(all_types))
    for t in range(n):
        type = all_types[t].text if all_types[t].text[-1] != ',' else all_types[t].text[:-1]
        content = all_contents[t]
        defs = content.find_all('div', value=True)

        # print(type)
        return_text += "\n"+str(type)
        for d in range(min(max_def_count, len(defs))):
            # print(str(d + 1) + '. ' + defs[d].find('span').text)
            return_text += "\n" + str(d + 1) + '. ' + defs[d].find('span').text

        if t < n-1:
            # print('')
            return_text += " \n"
    # add the word in cache
    add_data(w, return_text)
    return return_text

