import requests
import json

import streamlit as st

API_KEY = st.secrets['API_KEY']
API_URL = f'http://www.omdbapi.com/?apikey={API_KEY}&'

def define_type(type:str = 'movie'):
    response = (f'{API_URL}type={type}')
    return response

def load_query(query:str):
        response = requests.get(f'{define_type()}&s={query}')
        data = json.loads(response.content)
        if 'Search' in data:
            return data['Search']
        else:
            return {"False"}

def get_title(query):
    query_title = load_query(query)
    movie_titles = []
    for title in query_title:
        movie_titles.append(title['Title'])
    return movie_titles[0]

def get_poster(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Poster']

def get_year_of_release(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Year']

def get_viewer_rating(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Rated']

def get_release_date(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Released']

def get_runtime(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Runtime']

def get_genre(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Genre']

def get_director(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Director']

def get_writers(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Writer']

def get_actors(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Actors']

def get_plot(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Plot']

def get_language(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Language']

def get_awards(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Awards']

def get_imdb_rating(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    ratings = response.json()['imdbRating']
    return ratings

def get_box_office_revenue(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['BoxOffice']

def get_num_of_imdb_votes(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['imdbVotes']

def get_ratings(movie_name):
    response = requests.get(f'{define_type()}&t={get_title(movie_name)}')
    return response.json()['Ratings']