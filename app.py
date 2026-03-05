import streamlit as st
import pickle

animes = pickle.load(open('animes.pkl', 'rb'))
anime_list = animes['title'].values
simil = pickle.load(open('simil.pkl', 'rb'))

if 'first_five' not in st.session_state:
    st.session_state.first_five = []
if 'next_five' not in st.session_state:
    st.session_state.next_five = []
    
def recommend(anime):
    anime_idx = animes[animes['title'] == anime].index[0]
    dist = simil[anime_idx]
    anime_list = sorted(list(enumerate(dist)), key = lambda x: x[1], reverse=True)[1:6]
    ls = []
    for i in anime_list:
        ls.append(animes.iloc[i[0]].title)
    return ls

def recommend_more(anime):
    anime_idx = animes[animes['title'] == anime].index[0]
    dist = simil[anime_idx]
    anime_list = sorted(list(enumerate(dist)), key = lambda x: x[1], reverse=True)[6:11]
    ls = []
    for i in anime_list:
        ls.append(animes.iloc[i[0]].title)
    return ls
        
st.title('Anime Recommendation System')

anime_selected = st.selectbox(
    "Select an anime:",
    anime_list,
)

if 'show_more' not in st.session_state:
    st.session_state.show_more = False

st.write("You selected:", anime_selected)

if st.button("Recommend", type="primary"):
    st.session_state.first_five = recommend(anime_selected)
    st.session_state.next_five = []

if st.session_state.first_five:
    for i in st.session_state.first_five:
        st.write(i)
    
    if not st.session_state.next_five:
        if st.button("See more...", type="secondary"):
            st.session_state.next_five = recommend_more(anime_selected)
            st.rerun()

if st.session_state.next_five:
    for i in st.session_state.next_five:
        st.write(i)