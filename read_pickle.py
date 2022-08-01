import pickle
from pprint import pprint


pickle_path = "./Computers_TreeRLFC_3_SEEDS_1_MAX_100_HUBS/Computers_crawl_history_TreeRLFC_3_SEEDS_1__MAX_100_HUBS_blockchain_bitcoin.pickle"
objects = []
with (open(pickle_path, "rb")) as openfile:
  while True:
    try:
      objects.append(pickle.load(openfile))
    except EOFError:
      break

urls = []

for i in objects:
  # for k,v in i.items():
  print(i)