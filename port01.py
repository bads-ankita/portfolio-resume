import streamlit as st
from streamlit_option_menu import option_menu
import requests
from  streamlit_lottie import  st_lottie
from PIL import Image


st.set_page_config(page_title='My World',layout='wide')
st.subheader('Hii there......!! :smile:')
st.title('Welcome to my Portfolio Website.. :wave:')

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_3rwasyjy.json')
lottie_contact=load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_dhcsd5b5.json')
image1 = Image.open(r"C:\Users\ANKITA GHOSH\Downloads\heart-disease.png")
image2 = Image.open(r"C:\Users\ANKITA GHOSH\Downloads\wineglass.png")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
if selected == 'About':
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.write('##')
            st.subheader(' My name is Ankita Ghosh ')
            st.write('Experienced and results-oriented professional with a robust background in mathematics and a strong commitment to utilizing data-driven approaches to inform business strategies. Actively pursuing an MBA in Business Analytics and Data Science to deepen proficiency in deriving actionable insights from intricate datasets. An enthusiastic contributor poised to bring strategic acumen and advanced quantitative analysis capabilities to collaborative environments focused on leveraging data for informed decision-making in dynamic industries.')

        with col2:
            st_lottie(lottie_coding)

    st.write('---')

    with st.container():
        col3,col4=st.columns(2)
        with col3:
            st.subheader('''
            Education
            - Bengal institute of Business Studies ( Vidyasagar university )[ BIBS >](https://www.bibs.co.in/ )
                - persuing MBA ( Business analytics & Data science )
                - percentage - 79%
            - St. Thomas College , Bhilai ( Durg university )  [STC>](https://www.stthomascollegebhilai.in/)
                - M.Sc Mathematics - 86%
            - Asutosh college ( University of Calcutta )[ A.C >](https://asutoshcollege.in/new-web/)
                - B.Sc Mathematics - 50%  
            - Inda Krishnalal Shikshaniketan ( W.B.C.H.S.E. )
                - Higher Secondary education - 89%
            - Inda Balika Vidyalaya ( W.B.B.S.E ) 
                - Secondary education - 88%      
            ''')
        with col4:
            st.subheader('''
            Experience
            - Internship
                - Business Analyst intern @ Alcircle pvt ltd. 
                - Data Science intern @ Videodubber.AI
                - Certifications from IBM & IIT Kanpur
                -Attend Winter Training Program @ IIT Kanpur
            - Tutor
                - I love to teach maths.. 
                - I do tuitions for pocket money.... :smile: 
            - Content Creator
                - Me & my mom , we have a YouTube channel : [ Home Cuisine >](https://www.youtube.com/@homecuisine5273/ )
                - Here she makes sweet,simple & easy recipes......
                - Do LIKE , SHARE & of course SUBSCRIBE ....
            ''')

if selected == 'Projects':
    with st.container():
        st.header('My projects')
        st.write('##')
        col5,col6=st.columns((1,2))
        with col5:
            st.image(image1)
            st.image(image2)
        with col6:
            st.subheader('heart disease prediction')
            st.write(' i always wonder why people die having heart attack suddenly !')
            st.write('so i tried to build a machine learning model to predict if someone is likely or not likely have a heart disease ')
            st.markdown('[visit my github repositary: coming soon ]')
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('##')
            st.subheader('Wine Quality prediction')
            st.write(' Although i have not tried wine yet..')
            st.write('still i tried to build a machine learning model to predict the quality of a wine ! ')
            st.markdown('[visit my github repositary: coming soon ]')


if selected == 'Contact':
    with st.container():
        st.header('Nice to meet you ! :smile: ' )
        st.write('##')
        col7,col8=st.columns(2)
        with col7:
            st_lottie(lottie_contact)
        with col8:
            st.subheader(' \U0001F4E7 Email ')
            st.write('ankita.kgp.1997@gmail.com ')
            st.write('ankita.ghosh22-24@bibs.co.in')
            st.subheader(' \U0001F4F1 Phone & WhatsApp ')
            st.write(' 9903531585 ')
            st.subheader(" \U0001F310 LinkedIn")
            st.write(
                "[LinkedIn Profile](https://www.linkedin.com/ankita-ghosh25051997) ")

            st.header("Feedback & Review")

            # # Message input
            feedback = st.text_area("Enter your message:")
            rating = st.slider("Rate your experience", min_value=1, max_value=5)


            def save_feedback(feedback, rating):
                print("Feedback:", feedback)
                print("Rating:", rating)

            if st.button("Submit"):
                if feedback:
                    save_feedback(feedback, rating)
                    st.success("Thank you for your feedback!")
                else:
                    st.warning("Please enter your feedback.")









