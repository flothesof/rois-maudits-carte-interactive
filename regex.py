# %%
# load the first tome
import json
from collections import defaultdict
import re
lines = open(
    "Les Rois Maudits - L'integrale - Maurice Druon copy.txt").readlines()
first_tome = lines[:5512]
first_tome = [line.strip() for line in first_tome]

# %%
# define a basic matching pattern and a test
# à\s(\w+)
pattern = re.compile(pattern=r'à\s(\b[A-Z]\w+\b(?:[\s-]\b[A-Z]\w+\b)?)')
assert pattern.findall(
    "À vos sœurs de saint Dominique, à Poissy, je lègue la grande croix des Templiers. Et mon cœur aussi y sera porté.") == ['Poissy']


# %%
# match the first tome

matches = defaultdict(list)
for line in first_tome:
    match = pattern.findall(line)
    if len(match) > 0:
        for loc in match:
            if loc[0] == loc[0].capitalize():
                matches[loc].append(line)
# %%
# Remove unwanted things
EXCLUDE = ("Dieu", "Philippe", "Jeanne", "Monseigneur",
           "Marigny", "Nogaret", "Blanche", "Alain", "Madame", "Louis", "Marguerite", "Jean", "Tolomei", "Guccio", "Marie", "Gautier", "Isabelle", "Lormet", "Robert", "Charles", "Sire",
           "Evrard", "Béatrice", "Pierre", "Mahaut", "Fiennes", "Souastre", "Caumont", "Boccanegra")

matches = {key: value for key,
           value in matches.items() if not key.startswith(EXCLUDE)}

print('Unique matches')
print(list(matches.keys()))
# %%
json.dump(matches, open('tome1.json', 'w',
                        encoding='utf-8'), ensure_ascii=False)
# %%
