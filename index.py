import pickle
import streamlit as st
import requests
import streamlit.components.v1 as components

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

def fetch_overview(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    listofdic = list(dictionaries)
    vkey = "overview"
    lvalues = [item[vkey] for item in dictionaries]
    return lvalues[movie_id]

def fetch_name(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'title'
    lvalues = [item[n] for item in dit]
    return lvalues[movie_id]

def pop_mov_poster(ind):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    pop_mov = s_data['results']
    mov = list(pop_mov)
    pop_path = 'poster_path'
    full_path = "https://image.tmdb.org/t/p/w500/"
    lvalues = [item[pop_path] for item in pop_mov]
    final_poster = full_path + lvalues[ind]
    return final_poster

# st.image('images/s6.jpg')

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="C:/Users/Fatima/Desktop/ML _project/Updated/R_e_c_F_l_i_x/images/s1.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="s2.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="s3.jpg" alt="Third slide">
    </div>
  </div>
</div>
    """,
    height=200,
)
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
import base64

"""### gif from local file"""
file_ = open("C:/Users/Fatima/Desktop/ML _project/Updated/R_e_c_F_l_i_x/images/s1.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/jpg;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)


# header  = '<p style="font-family:Fantasy;background-color:grey; color:red;text-align: center;font-size: 40px;">R_e_c_F_l_i_x</p>'
# st.markdown(header, unsafe_allow_html=True)

st.header("Popular Movies")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(pop_mov_poster(0))

    with st.expander(fetch_name(0)):
        st.write(fetch_overview(0))

with col2:
    st.image(pop_mov_poster(1))
    with st.expander(fetch_name(1)):
        st.write(fetch_overview(1))

with col3:
    st.image(pop_mov_poster(7))
    with st.expander(fetch_name(7)):
        st.write(fetch_overview(7))
with col4:
    st.image(pop_mov_poster(6))
    with st.expander(fetch_name(6)):
        st.write(fetch_overview(6))


st.select_slider("Displayed values:", ["Normalized", "Absolute"])
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)


#Treading movies
st.header("Trending Movies")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")

    with st.expander(fetch_name(0)):
        st.write(fetch_overview(0))

with col2:
    st.image("https://imdb-api.com/images/original/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_Ratio0.7273_AL_.jpg'")
    with st.expander(fetch_name(1)):
        st.write(fetch_overview(1))

with col3:
    st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
    with st.expander(fetch_name(2)):
        st.write(fetch_overview(2))
with col4:
    st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
    with st.expander(fetch_name(3)):
        st.write(fetch_overview(3))


# #Tv shows
# st.header("Upcoming Movies")
# col1, col2, col3, col4 = st.beta_columns(4)
# with col1:
#     st.caption("A cat")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
#
# with col2:
#     st.caption("A dog")
#     st.image("https://imdb-api.com/images/original/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_Ratio0.7273_AL_.jpg'")
#
# with col3:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
# with col4:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
#
# #Tv shows
# st.header("Popular Tv Shows")
# col1, col2, col3, col4 = st.beta_columns(4)
# with col1:
#     st.caption("A cat")
#     st.image(fetch_overview(1))
#
# with col2:
#     st.caption("A dog")
#     st.image("https://imdb-api.com/images/original/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_Ratio0.7273_AL_.jpg'")
#
# with col3:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
# with col4:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
#
# #Tv shows
# st.header("Top Rated")
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     st.caption("A cat")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
#
# with col2:
#     st.caption("A dog")
#     st.image("https://imdb-api.com/images/original/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_Ratio0.7273_AL_.jpg'")
#
# with col3:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
# with col4:
#     st.caption("An owl")
#     st.image("https://imdb-api.com/images/original/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_Ratio0.7273_AL_.jpg")
#
#

movies = pickle.load(open('Data/movie_list.pkl','rb'))
similarity = pickle.load(open('Data/similarity.pkl','rb'))



st.sidebar.header('Search here...')
movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox(
    "",
    movie_list
)

s_button = st.sidebar.button('Rec Me')

if s_button:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col2:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col2:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
