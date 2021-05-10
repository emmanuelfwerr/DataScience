# Analyzing A/B Test Results 

## Project Overview
A/B tests are very commonly performed by data analysts and data scientists. For this project, we will work to understand the results of an A/B test run by an e-commerce website. The company has developed a new web page in order to try and increase the number of users who "convert," meaning the number of users who decide to pay for the company's product. Our goal is to work through this notebook to help the company understand if they should implement the new page, keep the old page, or perhaps run the experiment longer to make their decision. We will be provided a dataset containing recorded data from an experiment and will use statistical techniques to answer questions about the data and report our conclusions and recommendations.

This project's template features a quiz-like design and was provided by Udacity.

### Environment

This project requires **Python 3.8** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)

We will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html), in this project we use [Anaconda](https://www.continuum.io/downloads). 

### Index

1. `report.ipynb`: Jupyter NB containing analysis of dataset and project report
2. `ab_data.csv`: The dataset in .csv format
3. `couuntries.csv`: A complementary dataset in .csv format that contains user's country information

### Overview
The project is divided into three main parts:
#### Part I - Probability
We begin by computing statistics to find out the probability of converting users regardless of what page they interact with. These statistics are used to determine if any one of the pages led to more conversions.
#### Part II - A/B Test
Hypothesis testing was conducted. We assume the old page is better unless the new page proves to be better by staying below a Type I error threshold rate of 5%. The data was bootstrapped and sampling distributions were determined for both pages. Conclusions were drawn on conversions for both pages by calculating p-values.
#### Part III - Regression
Logistic regression was performed to confirm the results of previous steps. Null and alternative hypotheses associated with the regression model were stated and verified using the statsmodel library and its methods.

### Results
The results of our statistical tests point to an equal chance of converting users by both pages. Given these results, we fail to reject the null hypothesis at the 5% threshold. My recommendation is that the e-commerce company should keep the old page. This will save them time and money, and will perform as well as a new page would.

