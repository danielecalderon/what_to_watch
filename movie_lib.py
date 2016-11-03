import csv


# Step 1
# class Movie():
#
# class User():
#
# class Rating():

# Find all ratings for a movie by id
# Find the average rating for a movie by id
# Find the name of a movie by id
# Find all ratings for a user



#ed to be able to load in movie and rating data.
# Using the csv module, write a module that will load in the
# the user data from u.user, the movie data from u.item,
# and the rating data from u.data.

with open('ml-100k/u.data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


#
# The easiest way to recommend movies is to recommend the most popular movies.
# Write a program to show the top X movies by average rating with their rating.
# You need to be able to state a minimum number of ratings for a movie to be considered.
#
# Now, create the ability to find the top X movies by average rating that a
# specific user has not rated. This allows you to suggest popular movies for a
# specific user.
