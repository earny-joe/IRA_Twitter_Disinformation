# **_Internet Research Agency: Fastai Tweet Classifier_**

![Gif of Streamlit app](https://media.giphy.com/media/gKTFFrCEVlM3ujCkVx/giphy.gif)

## _Is it the Russians?_ 

It is becoming increasingly evident that [information operations](https://en.wikipedia.org/wiki/Information_warfare) are being heavily utilized, by both state and non-state actors, on a range of social media platforms in an attempt to sway public opinion. Perhaps the most infamous outfit that conducts in these online influence operations is the [Internet Research Agency](https://en.wikipedia.org/wiki/Internet_Research_Agency) (_Russian: Агентство интернет-исследований_).

Linked to Russian oligarch [Yevgeny Prigozhin](https://en.wikipedia.org/wiki/Yevgeny_Prigozhin), who himself has close ties with Russian President Vladimir Putin, the "Trolls from Olgino," has been described as a **troll farm** by the [U.S. Intelligence Community](https://en.wikipedia.org/wiki/Assessing_Russian_Activities_and_Intentions_in_Recent_US_Elections). While the exact impact can be hard to measure, there is no doubt that the IRA played a significant role in trying to sway the 2016 U.S. presidential election.

November 2020, the next U.S. presidential election, is just around the corner. And unfortunately, it appears we're ill-prepared for what will almost assuredly be another round of influence operations conducted by organizations like the IRA.
Because of this, I wanted to see if it would be possible to create an IRA Tweet classifier that could separate "real" tweets from those with ulterior motives.

## _What was the data?_

The first step to generating a deep learning (or machine learning) model is gathering data. We began by gathering Twitter data from verified accounts, i.e., accounts who have the blue check next to their name and was done via the [`twint`](https://github.com/twintproject/twint) Python library. Additionally, the user's backgrounds varied widely, from professional athletes and movie stars to politicians and media outlets. The reason for this was that the diversity of tweet content could (at least in theory) lend to a more robust data set. In the coming days, I will post a full list of the verified accounts that were included in the data set.

The data for the IRA was gathered via [Twitter's Elections integrity data archive](https://about.twitter.com/en_us/values/elections-integrity.html#data). If interested, click this [link](https://transparency.twitter.com/en/information-operations.html) to go to the page where Twitter has made publicly available archives of tweets and media from state-backed information operations on their platform. The data set I used was released in October 2018 and includes tweet information from 3,613 accounts linked to the Internet Research Agency. For this project, and to decrease initial complexity, we decided to only include tweets from this dataset that were in English. While it did cut into the total number of observations available to us, it still left us with nearly ~600k IRA-linked tweets.

My tactic for splitting data into training (which includes validation) and test sets was not to merely randomly split observations. We have to remember that tweets are not standalone; they are often indicative of current events happening at a particular time. So while not a traditional time-series problem (like say predicting stock price from market data), time plays a significant role when it comes to tweets. After reading [this article](https://www.fast.ai/2017/11/13/validation-sets/) by [Rachel Thomas](https://www.fast.ai/about/#rachel), a co-founder of Fast.ai, on how to create a good validation set, I confirmed that dividing the data based on time was the way to go.

The data was split according to the year it was created. Since 2016 was when the election took place, I felt that it was a great point to split the data on. So, the training data included all tweets before and up to the end of 2016. The total number of observations was ~1.24M, with the distribution of tweets being ~62.19% `verified` and ~37.81% `ira`. The test set included all tweets from the years 2017 and 2018, which amounted to ~437k tweets with a distribution of ~70.68% `verified` and ~29.32% `ira`. However, I would like to point out that the test data included in this repository is a 5,000 observation sample of that more extensive test set.

## _Fast.ai_ 

The training was conducted via Google Colab and utilized [Fast.ai's Deep Learning text/NLP library](https://www.fast.ai/2019/07/08/fastai-nlp/) to produce a model that could classify Tweets as either `verified` (i.e., came from a verified user) or `ira` (i.e., tweet came from IRA-linked user).

## _How to Use the Streamlit App_

In addition to developing the model, we also put together an app using [Streamlit](https://www.streamlit.io/), which is an open-source app framework for ML/DS teams to create data apps in pure Python. To put it to the test, follow along with the instructions below:
1. Clone this repository
2. Run `pip install -r requirements.txt `to install necessary Python libraries
3. Run `python download_model.py`, which downloads the fast.ai model in pickle format (I couldn't host it on GitHub due to their 100MB file limit). (FYI - don't be surprised if a random Chrome browser opens upon running this script! It uses a Selenium web driver to open the URL of the data's location, download it, and subsequently close the driver. The process should only take ~20 seconds or so.)
4. Run `streamlit run app.py`!