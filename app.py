import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return  recommended_movies
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommended System')
selected_movie_name = st.selectbox(
'How would you like to be connected?',
    movies['title'].values
)
if st.button('Recommended'):
    recommendation= recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
