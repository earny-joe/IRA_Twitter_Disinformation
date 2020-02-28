import pandas as pd
import streamlit as st
from pathlib import Path
import os
from fastai.text import *
import time

os.environ['KMP_DUPLICATE_LIB_OK']="True"

def create_path():
    """
    Creates path to primary directory.
    """
    return Path(os.getcwd())

@st.cache
def load_dataframe():
    """
    Loads in data.
    """
    path = create_path()
    df = pd.read_pickle(path/"data/testset_sm_02122020.pkl")[["TWEET", "LABEL"]]
    df["LABEL"] = df["LABEL"].astype(str)
    return df, df.sample(n=15)

def count_string(sampledf):
    """
    Outputs string showing how many verified/IRA tweets there are.
    """
    counts = sampledf["LABEL"].value_counts()
    verified = counts["verified"]
    ira = counts["ira"]
    return f"""There are {verified} tweets from verified users and {ira} tweets linked to the IRA in the sample (n=15) we gathered from unseen test data. Can the model guess which is which?""".replace("\n", " ")

def main():
    st.sidebar.title("About")
    st.sidebar.info("This is a proof-of-concept for an application that utilizes a deep learning model trained with Fastai to classify tweets from either Verified Twitter users or those that were linked to accounts run by the Internet Research Agency.")
    st.title("_Internet Research Agency_: Fastai Tweet Classifier")
    st.write("Pick a tweet from the sidebar on the left.\nWhen you are ready, hit the **Predict** button.") 
    # create directory path
    path = create_path()
    # gather data and a sample then store Tweets available to pick from
    df, sample = load_dataframe()
    # create count string show how many verified/IRA tweets there are
    st.subheader(count_string(sample))
    # create list of tweets
    tweet_list = [tweet for tweet in sample["TWEET"]]
    # create selectbox in sidebar
    tweet_select = st.sidebar.selectbox("Pick a Tweet.", tweet_list)
    # output how many verified/IRA tweets there are
    if st.sidebar.button("Predict"):
        st.subheader(f"You selected the following Tweet to classify:\n_{tweet_select}_")
        with st.spinner("Analyzing ..."):
            time.sleep(5)
        
        # load model and make prediction
        model = load_learner(path, "biclas_feb2020.pkl")
        predict = model.predict(tweet_select)
        st.subheader("Results")
        st.write(f"Model's prediction for the tweet above: **{str(predict[0]).upper()}**")
        st.write(f"Proabability that it is Verified tweet: **{round(float(predict[2][1]), 6) * 100}%**")
        st.write(f"Proabability that it is a IRA tweet: **{round(float(predict[2][0]), 6) * 100}%**")
        #st.write(sample[sample["TWEET"] == tweet_select]["LABEL"].iloc[0])
        correct = str(predict[0]) == sample[sample["TWEET"] == tweet_select]["LABEL"].iloc[0]
        st.write(f"Was the model's prediction correct? **{correct}**")
        
if __name__ == "__main__":
    main()
    

