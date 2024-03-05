from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]


# variables to store data
liked_movies = []
disliked_movies = []
unrated_movies = []


# method to fetch data from database
def assign_value():
  m_data = {
        "original_title": all_movies.iloc[0,0],
        "poster_link": all_movies.iloc[0,1],
        "release_date": all_movies.iloc[0,2] or "N/A",
        "duration": all_movies.iloc[0,3],
        "rating":all_movies.iloc[0,4]/2
    }
  return m_data

# /movies api
@app.route("/movies")
def get_movie():
  movie_data = assign_value()

  return jsonify({
    "data":movie_data,
    "status": "success"
  })

# /like api
@app.route("/likes")
def like_movie():
  global all_movies
  movie_data = assign_value()
  liked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status": "success"
  })

# /dislike api
@app.route("/dislikes")
def dislike_movie():
  global all_movies
  movie_data = assign_value()
  disliked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status" : "success"
  })

# /watched but unrated movies  api
@app.route("/unrated")
def unrated_movie():
  global all_movies
  movie_data = assign_value()
  unrated_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status" : "success"
  })

if __name__ == "__main__":
  app.run()