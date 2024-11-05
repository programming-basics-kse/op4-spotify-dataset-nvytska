# with open('top_50_2023.csv', 'r') as csvfile:
#     header = next(csvfile)
#     data = []
#     for line in csvfile:
#         line = line[:-1].split(',')
#         data.append(line)
#
# print(data[0])

#2 variant
import csv
import ast
from turtledemo.clock import datum

with open('top_50_2023.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)

GENRE = header.index('genres')
for row in rows:
    row[GENRE] = ast.literal_eval(row[GENRE])
print(rows[0])

# average danceability
def is_valid(num:str) -> bool:
    try:
        num = float(num)
        if -1<=num <= 1:
            return True
        return False
    except ValueError:
        return False

DANCEABILITY = header.index('danceability')
sum_dance = 0
counter = 0
for row in rows:
    if is_valid(row[DANCEABILITY]):
        counter +=1
        sum_dance += float(row[DANCEABILITY])
print('Average is:', sum_dance/counter)

EXPLICIT = header.index('is_explicit')
counter_explicit = 0
for row in rows:
   if row[EXPLICIT] == 'True':
       counter_explicit +=1

print(f"There are {counter_explicit} explicit songs")


GENRES = 4
genres_counts = {}
for row in rows:
    for genre in row[GENRE]:
        if genre in genres_counts:
            genres_counts[genre] +=1
        else:
            genres_counts[genre] = 1

top_3 = sorted(genres_counts.items(), key=lambda x:x[1], reverse=True,)[:3]
print(top_3)


# Average Liveliness with Energy Criteria
ENERGY = 7
sum_energy = 0
counter = 0
for row in rows:
    if is_valid(row[ENERGY]):
        counter +=1
        sum_energy += float(row[ENERGY])
print('Average Liveliness is:', sum_energy/counter)

#The most popular artist

ARTIST = 0
artist_counter = {}
for row in rows:
    artist = row[ARTIST]
    if artist in artist_counter:
        artist_counter[artist] +=1
    else:
        artist_counter[artist] = 1

top_artist = sorted(artist_counter.items(), key=lambda x:x[1], reverse=True,)[0]
print("The most popular artist:", top_artist)

#The most popular year
DATE = header.index('album_release_date')
year_counts = {}
for row in rows:
    year = row[DATE][:4]
    if year in year_counts:
        year_counts[year] +=1
    else:
        year_counts[year] = 1
top_year = sorted(year_counts.items(), key=lambda x:x[1], reverse=True,)[0]

print("The most popular year is",top_year)







