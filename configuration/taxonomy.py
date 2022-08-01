## Change this taxonomy modifying the example below ##
## Use your domain name (e.g. Hardware) as the key of the dict
## Use zeros for dict values as in the example below.

taxonomy = {

	# Example
    "Computers": [
        # Here: Keywords
        {
            "bitcoin": 0,
            "btc": 0,
            "crypto": 0,
            "BTC": 0,
            "Bitcoin": 0,
            "cryptocurrency": 0,
            "cryptocurrencies": 0,
        },
        # Here: Keyphrases
        {
            "bitcoin increase": 0,
            "bitcoin decrease": 0,
            "btc increase": 0,
            "btc decrease": 0,
            "BTC increase": 0,
            "BTC decrease": 0,
            "Bitcoin increase": 0,
            "Bitcoin decrease": 0,
        }
    ]

}


## Ignore this part ##

from .config import *
from utils.hyperparameters import *
import pickle

path = "./files/"

print(path + 'new_keywords_' + domain + '.pickle')

taxonomy_keywords = taxonomy[domain][0]
taxonomy_phrases = taxonomy[domain][1]

try:
    with open(path + 'new_keywords_' + domain + '.pickle', 'rb') as handle:
        new_keywords = pickle.load(handle)
except: new_keywords = {}

print(new_keywords)
