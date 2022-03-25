# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data

data = pd.read_csv('metacritic2.csv')
#print(data)

# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)

mario = data[data.Game.str.contains('Mario')]
#print(mario)


# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)

sor = mario.sort_values("Release Year", axis = 0, ascending = False)
#print(sor)

# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?

group = data.groupby("Release Year").count()
#print(group)

# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?

group1 = data.groupby("Platform")
#print(group1.count())
#print(group1.mean())
#print(group1.median())

# 7. Create a new dataframe from the HunterAMC.csv file.

amc = pd.read_csv('HunterAMC.csv', sep = "\t")

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.

amc10 = amc[amc['contest'] == 0]
amc12 = amc[amc['contest'] == 2]
print(amc10)
print(amc12)

# 9. Find the average scores for each contest.

print(amc10.mean())
print(amc12.mean())

# 10. For each column, count how often each answer choice was selected.
