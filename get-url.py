import json
import requests
import urllib.request

def gif (idx):
    gif_dict = {
        1: 'agree',
        2: 'applause',
        3: 'awww',
        4: 'dance',
        5: 'deal_with_it',
        6: 'do_not_want',
        7: 'eww',
        8: 'eye_roll',
        9: 'facepalm',
        10: 'fist_bump',
        11: 'good_luck',
        12: 'happy_dance',
        13: 'hearts',
        14: 'high_five',
        15: 'hug',
        16: 'idk',
        17: 'kiss',
        18: 'micdrop',
        19: 'no',
        20: 'omg',
        21: 'oh_snap',
        22: 'ok',
        23: 'oops',
        24: 'please',
        25: 'popcorn',
        26: 'smh',
        27: 'scared',
        28: 'seriously',
        29: 'shocked',
        30: 'shrug',
        31: 'sigh',
        32: 'slow_clap',
        33: 'sorry',
        34: 'thank_you',
        35: 'thumbs_down',
        36: 'thumbs_up',
        37: 'want',
        38: 'win',
        39: 'wink',
        40: 'yolo',
        41: 'yawn',
        42: 'yes',
        43: 'you_got_this'
    }
    return gif_dict[idx]

cat_url = {}

for i in range(1, 44):

    cat = gif(i)
    urls = []

    #tenor API
    tenorapikey = "KOBZBCHIOB9T" 
    lmt = 4
    search_term = cat
    tenor = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, tenorapikey, lmt))
    if tenor.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_gifs = json.loads(tenor.content)
    else:
        top_gifs = None
    # extract tenor GIF
    for GIFs in top_gifs['results']:
        urls.append(GIFs['media'][0]['tinygif']['url'])
    
    #giphy api
    cat_process = cat.replace(' ', '+')
    giphy_url = "http://api.giphy.com/v1/gifs/search?q=" + cat_process + "&api_key=g7oEHBRcYKzCSiDBGD5DcLuoB7jF7tW7&limit=4"
    giphy = json.loads(urllib.request.urlopen(giphy_url).read())
    # extract giphy GIF
    for GIFs in giphy['data']:
        urls.append(GIFs['images']['original']['url'])
    
    cat_url[cat] = urls

with open("gif-url.json", "w") as file:
    json.dump(cat_url, file, indent=2)

print("done")