import csv
total_duration = 0

with open('movie_list.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) >= 5:
            time_str = data[4]
            try:
                hours, minutes = map(int, time_str.split(':'))
                movie_duration = hours * 60 + minutes 
                total_duration += movie_duration
            except ValueError:
                pass

print(f'Total Duration of all Movies (in mins): {total_duration} min')

import csv
file = csv.reader( open("movie_list.txt"))
movies = [i for i in file]
time = [i[-1].split(":") for i in movies]
minutes = []
for i in time:
    minutes.append(int(i[0]) * 60 + int(i[1]))
max_movie = [i[2] for i in movies if max(minutes)//60 == int(i[-1].split(":")[0]) and max(minutes)%60 == int(i[-1].split(":")[1])]
min_movie = [i[2] for i in movies if min(minutes)//60 == int(i[-1].split(":")[0]) and min(minutes)%60 == int(i[-1].split(":")[1])]
special_date = [[i[2],i[-2]] for i in movies if i[-2] > "14.10.2022"]
special_time = [i[2] for i in movies if i[-1] > "1:30"]
special_release = [[i[2],i[-2]] for i in movies if i[-2].split(".")[2] == "2021"]


print(sum(minutes)//60,"hours", sum(minutes)%60,"minutes")
max_movie = ", ".join(max_movie)
min_movie = ", ".join(min_movie)
print(f"Longest movie: {max_movie}")
print("---------------------------------------------------------")
print(f"Shortest movie: {min_movie}")
print("---------------------------------------------------------")
print(f"Special date: {special_date}")
print("---------------------------------------------------------")
print(f"Special time: {special_time}")
print("---------------------------------------------------------")
print(f"Special release: {special_release}")
print("---------------------------------------------------------")
print("Average of all movies:")
print(int((sum(minutes)/len(minutes)))//60, ":", int((sum(minutes)/len(minutes))%60 ))