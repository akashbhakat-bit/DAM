import os
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import requests
from requests.exceptions import HTTPError

# Set page configuration
st.set_page_config(page_title="Personalized Songs",
                   layout="wide",
                   page_icon="🎵")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('BeatBlend',

                           ['Home',
                            'Activity Based Suggestions',
                            'Metric Based Suggestions'],
                           menu_icon='hospital-fill',
                           icons=['home', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Home':

    # Custom CSS for styling
    custom_css = """
        <style>
            .header {
                color: #1DB954;
                text-align: center;
                margin-bottom: 30px;
                font-size: 48px;
                font-weight: bold;
            }
            .container {
                max-width: 800px;
                margin: auto;
            }
            .intro-text {
                font-size: 20px;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            .highlight {
                color: #1DB954;
                font-weight: bold;
            }
            .highlight2 {
                color: #FC2E20;
                font-weight: bold;
            }
            .quote {
                font-style: italic;
                color: #25C0C0;
                margin-bottom: 30px;
                font-size: 24px;
                text-align: center;
            }
            .features {
                margin-bottom: 30px;
                font-size: 18px;
                line-height: 1.6;
            }
            .footer {
                color: #777;
                text-align: center;
                margin-top: 50px;
                font-size: 16px;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Page layout
    st.markdown("<h1 class='header'>BeatBlend: Your Personalized Playlist Mixer</h1>", unsafe_allow_html=True)
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<p class='intro-text'>Welcome to <span class='highlight'>BeatBlend</span>, where music meets your mood!</p>", unsafe_allow_html=True)
    st.markdown("<p class='quote'>\"Life is a playlist, let's make it custom!\"</p>", unsafe_allow_html=True)
    st.markdown("<p class='intro-text'>Tired of generic playlists? Whether you're in the mood to groove, grind at the gym, or cruise on the highway, we've got you covered.</p>", unsafe_allow_html=True)
    st.markdown("<p class='features'>Choose your vibe - whether it's <span class='highlight2'>DJ, Gym, Slow, Driving,</span> or customize to <span class='highlight2'>BPMs, Artists, Mode, Danceability, Valence, Energy, Acousticness, Instrumentalness, Liveness, Speechiness,</span> and we'll curate a playlist just for you.</p>", unsafe_allow_html=True)
    st.markdown("<p class='intro-text'>Let's tune into your rhythm and set the stage for your perfect playlist experience!</p>", unsafe_allow_html=True)
    st.markdown("<span class ='highlight2'>Try it now</span></div>", unsafe_allow_html=True)

   

    # Footer
    st.markdown("<p class='footer'>Developed with ❤️ for LBS, by LBS-MAM2024 GRP 7</p>", unsafe_allow_html=True)

if selected == 'Activity Based Suggestions':

    st.title("Activity Based Playlist Creation")

    st.write("Create a customized playlist tailored to your activity!")

    # Activity selection
    activity = st.radio("Select Activity:", ["Gaming", "Road Trip", "Nostalgic Comforting", "Relaxing - Coffee", 'Club - DJ'])

    # Time range input
    song_range = st.number_input("Enter Number of Songs :", min_value=1, max_value=120, value=10)
    # Button to generate playlist
    if st.button("Generate Playlist"):
        url = 'https://a529-185-36-251-58.ngrok-free.app/get_songs_activity'
        data = {
            'genre': activity,
            'max_songs': song_range
            }
        response = requests.post(url, json=data)
        #print("#######################################")
        #print(response.json())
        #print("#######################################")
        df = pd.DataFrame(response.json())
        df['S.No'] = df.index + 1
        df = df[['S.No', 'track_name', 'artist(s)_name', 'released_year', 'bpm', 'key_mode_combined' ]]
        df.columns = ['S.No', 'Track Name', 'Artist', 'Year of Release', 'Beats Per Minute', "Key Modes"]
        st.write(f"Playlist for {activity} activity ", unsafe_allow_html=True)
        st.write(f"Number of Songs : {df.shape[0]}",unsafe_allow_html=True)
        # Display DataFrame as table
        st.write(df.to_html(index=False), unsafe_allow_html=True)

if selected == "Metric Based Suggestions":
    st.title("Metric Based Playlist Creation")

    st.write("Create a customized playlist based on various metrics!")
    slider_mapping = {
        "Very Low": -2,
        "Low": -1,
        "Normal": 0,
        "High": 1,
        "Very High": 2
    }

    
    # Song range input
    song_range = st.number_input("Enter Number of Songs :", min_value=1, max_value=120, value=10)
    # BPM range input
    bpm_range = st.slider("Enter max  BPM preferred:", min_value=1, max_value=200, value=120)
    
    # Mode selection
    mode = st.radio("Select Mode:", ["Major", "Minor"])

    # Danceability input
    danceability_label = st.select_slider("Enter Danceability:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    danceability = slider_mapping[danceability_label]
    
    # Valence input
    valence_label = st.select_slider("Enter Valence:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    valence = slider_mapping[valence_label]
    
    # Energy input
    energy_label = st.select_slider("Enter Energy:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    energy = slider_mapping[valence_label]
    
    # Acousticness input
    acousticness_label = st.select_slider("Enter Acousticness:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    acousticness = slider_mapping[acousticness_label]
    
    # Instrumentalness input
    instrumentalness_label = st.select_slider("Enter Instrumentalness:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    instrumentalness = slider_mapping[instrumentalness_label]
    
    # Liveness input
    liveness_label = st.select_slider("Enter Liveness:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    liveness = slider_mapping[liveness_label]
    
    # Speechiness input
    speechiness_label = st.select_slider("Enter Speechiness:", options=list(slider_mapping.keys()), format_func=lambda x: x)
    # Retrieve the corresponding value
    speechiness = slider_mapping[speechiness_label]
    
    # Button to generate playlist
    if st.button("Generate Playlist"):
        # Call function to generate playlist based on selected metrics
        #generate_playlist_metic(song_range, bpm_range, mode, danceability, valence, energy, acousticness, instrumentalness, liveness, speechiness)
        url = 'https://a529-185-36-251-58.ngrok-free.app/get_songs_metric'
        #print("###########################")
        #print("bpm range =", bpm_range)
        data = {
            'max_songs': song_range,
            'danceability':danceability,
            'valence':valence,
            'energy':energy,
            'bpm_range':bpm_range,
            'liveness':liveness,
            'instrumentalness':instrumentalness,
            'acousticness':acousticness,
            'speechiness' : speechiness
            }
        try:
            response = requests.post(url, json=data)
            #print(response)
            if(response.status_code != 200):
                #print("!@#$%^&(*&^%$#)")
                st.markdown("""
                <style>
                .error-message {
                    background-color: rgba(255, 230, 230, 0.6);
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 18px;
                    text-align: center;
                }
                </style>
                <div class="error-message">No Optimal Playlist could be Created. Please try again with different combinations of Metrics</div>
                """, unsafe_allow_html=True)
            else:
                df = pd.DataFrame(response.json())
                df['S.No'] = df.index + 1
                df = df[['S.No', 'track_name', 'artist(s)_name', 'released_year', 'bpm', 'key_mode_combined' ]]
                df.columns = ['S.No', 'Track Name', 'Artist', 'Year of Release', 'Beats Per Minute', "Key Modes"]
                st.write(f"Custom Playlist Created !! Enjoy your Day !!", unsafe_allow_html=True)
                st.write(f"Number of Songs : {df.shape[0]}",unsafe_allow_html=True)
                # Display DataFrame as table
                st.write(df.to_html(index=False), unsafe_allow_html=True)
        except HTTPError as e:
            st.markdown("""
                <style>
                .error-message {
                    background-color: rgba(255, 230, 230, 0.6);
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 18px;
                    text-align: center;
                }
                </style>
                <div class="error-message">An error occurred. Please refresh and try again </div>
                """, unsafe_allow_html=True)
