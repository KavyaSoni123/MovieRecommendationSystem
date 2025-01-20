import streamlit as st
import pickle

def recommend_movie(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    L = []
    posters = []
    for i in movie_list:
        movie_id = i[0]
        L.append(movies_list.iloc[i[0]].title)
    return L

movies_list = pickle.load(open('./movies.pkl','rb'))
movies_title_list = movies_list['title'].values

similarity = pickle.load(open('./similarity.pkl','rb'))

st.title("Movie Recommender System")
movie_name = st.selectbox(
    "Please select your favourite movie",
    (movies_title_list),
)

if st.button("Recommend",type='primary'):
    recommended_movies = recommend_movie(movie_name)
    for i in recommended_movies:
        st.write(i)



