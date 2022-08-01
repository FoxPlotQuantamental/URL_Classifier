import pickle
from pprint import pprint


pickle_path = "./files/Computers.pickle"
objects = []
with (open(pickle_path, "rb")) as openfile:
  while True:
    try:
      objects.append(pickle.load(openfile))
    except EOFError:
      break

urls = []

for i in objects:
  for k,v in i.items():
    url = k + " \n"
    urls.append(url)

f = open("files/data.txt", "w")
f.writelines(urls)
f.close()

new_f = open("files/data.txt", "r")
print(new_f.read())
new_f.close()