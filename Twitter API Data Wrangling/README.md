# Wrangling Twitter tweet data 

## Project Overview

Real-world data rarely comes clean. For this project, we gather data from a variety 
of sources and in a variety of formats, assess its quality and tidiness, then clean it. The dataset that 
we will be wrangling is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs 
is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost 
always have a denominator of 10. The numerators, though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. 
WeRateDogs has over 4 million followers and has received international media coverage.

WeRateDogs downloaded their Twitter archive and made it available for us to use. However, we must gather extra data from Twitter's API and join it to our database through the tweet ID:
  - Tweet image predictions (dog breed classifier) according to a neural network
  - Each tweet's retweet count and favorite count
  
### Environment

This project requires **Python 3.8** and the following Python libraries installed:

- [numpy](https://docs.scipy.org/doc/numpy-1.13.0/contents.html)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [requests](https://pypi.org/project/requests/)
- [tweepy](https://www.tweepy.org/)
- [json](https://docs.python.org/3/library/json.html)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html), 
in this project we use [Anaconda](https://www.continuum.io/downloads). 

### Index

1. `wrangle_act.ipynb`: code for gathering, assessing, cleaning, analyzing, and visualizing data
2. `wrangle_report.pdf`: documentation for data wrangling steps: gather, assess, and clean
3. `act_report.pdf`: documentation of analysis and insights into final data
4. `twitter_archive_enhanced.csv`: file as given
5. `image_predictions.tsv`: file downloaded programmatically
6. `tweet_json.txt`: file constructed via API
7. `twitter_archive_master.csv`: combined and cleaned data

