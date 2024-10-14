import streamlit as st
import movie_query_api
st.set_page_config(page_title="Movie Query",layout='wide',page_icon="🎥")
st.title('Movie Query')

#Changes the font size of the metrics
st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 30px;
}
</style>
""",
    unsafe_allow_html=True,
)

movie_name_user = st.text_input('Please provide a movie title :')
if len(movie_name_user) == 0:
    st.warning('Please provide a movie title')
    left_co, cent_co,last_co = st.columns([3.5,3,3])
    with cent_co:
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm02d3ZoeHY3aHo2dWcxbWZtejVwMjBjZHZ1ZGI3Nmx4emgyaHBhOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CqunRZhzJkFoXt28c3/giphy.webp", width=500)

elif movie_query_api.load_query(movie_name_user) == {"False"}:
    st.error('Movie not found')
    left_co, cent_co,last_co = st.columns([3.5,3,3])
    with cent_co:
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWZ0NXd6dnVzeXR1NWVpNDMzOWw0MnYyanBobWMzamc0OGM4a3hjayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7SF5scGB2AFrgsXP63/giphy.webp", width = 500)
    

else:
    movie_name = movie_query_api.get_title(movie_name_user)
    st.header(movie_name)
    col1,col2,col3 = st.columns([2,2,1])
    with col1:
        with st.container(border=True):
            if movie_query_api.get_poster(movie_name) == 'N/A':
                st.write('image not found')
            else:
                left_co, cent_co,last_co = st.columns([1.5,3,1])
                with cent_co:
                    st.image(movie_query_api.get_poster(movie_name))
            cl1,cl2,cl3= st.columns([1,1,1])
            with cl1:
                st.metric(label=':red[Year]',value=movie_query_api.get_year_of_release(movie_name))
            with cl2:
                st.metric(label=':red[Rated]',value=movie_query_api.get_viewer_rating(movie_name))
            with cl3:
                st.metric(label=':red[Runtime]',value=movie_query_api.get_runtime(movie_name))
            st.caption(f"**{movie_query_api.get_plot(movie_name)}**")

    with col2:
        with st.container(height=350):
            st.subheader('Cast and Crew', divider="gray")
            st.metric(label = ':red[Director]', value = movie_query_api.get_director(movie_name))
            st.metric(label = ':red[Writers]', value = movie_query_api.get_writers(movie_name))
            st.metric(label = ':red[Actors]', value = movie_query_api.get_actors(movie_name))
        with st.container(border=True):
            st.subheader('Additional Information', divider="gray")
            st.metric(label = ':red[Genre]', value = movie_query_api.get_genre(movie_name))
            st.metric(label = ':red[Release Date]', value = movie_query_api.get_release_date(movie_name))
    with col3:
        with st.container(border=True):
            st.subheader('Ratings', divider="gray")
            #st.metric(label = ':red[IMDB]', value = omdb_api.get_imdb_rating(movie_name), delta = omdb_api.get_num_of_imdb_votes(movie_name)) 
            for rating_sites in movie_query_api.get_ratings(movie_name):
                st.metric(label=rating_sites['Source'], value=rating_sites['Value'])

        with st.container(border=True):
            st.subheader('Overall Opinion', divider="rainbow")
            imdb_rating = float(movie_query_api.get_imdb_rating(movie_name))
            if imdb_rating >= 7:
                st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNncwdDZvN2w1MnE5bmVmNmg0cjJpcnlpODgycDd5NXk4N2F4c3pvMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Od0QRnzwRBYmDU3eEO/giphy.webp")
            elif imdb_rating < 7 and imdb_rating >= 5.5:
                st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGIxYW56MGdtNWN1a3lucGxyaTNiZTM2d2szYWF1d3A3czV1cHYyeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TNO6mwK8s38vpHjh8Y/giphy.webp")
            else:
                st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWEwOWR0eTEzYWY1MDM1eWpiZ2JvZGJ1dHdkaWZweDVkemlvZjd2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TUQo7EfCWNi3UBxGxk/giphy.webp")
