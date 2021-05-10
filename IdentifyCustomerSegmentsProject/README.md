# Identify Customer Segments - an Unsupervised Learning ML Project

## Project Overview

In this project we apply unsupervised learning techniques on product spending data collected for customers of a wholesale distributor in Lisbon, Portugal to identify customer segments hidden in the data. We first explore the data by selecting a small subset to sample and determine if any product categories highly correlate with one another. Afterwards, we preprocess the data by scaling each product category and then identifying (and removing) unwanted outliers. With the good, clean customer spending data, we apply PCA transformations to the data and implement clustering algorithms to segment the transformed customer data. Finally, we compare the segmentation found with an additional labeling and consider ways this information could assist the wholesale distributor with future service changes.

### Environment

This project requires **Python 3.8** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

We will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html), in this project we use [Anaconda](http://continuum.io/downloads).

### Index

1. `customer_segments.ipynb`: Jupyter NB containing analysis of dataset and project report
2. `customers.csv`: The dataset in .csv format
3. `visuals.py`: Functions to visualize the data

## Data

The customer segments data is included as a selection of 440 data points collected on data found from clients of a wholesale distributor in Lisbon, Portugal. More information can be found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers).

Note (m.u.) is shorthand for *monetary units*.

**Features**
1) `Fresh`: annual spending (m.u.) on fresh products (Continuous); 
2) `Milk`: annual spending (m.u.) on milk products (Continuous); 
3) `Grocery`: annual spending (m.u.) on grocery products (Continuous); 
4) `Frozen`: annual spending (m.u.) on frozen products (Continuous);
5) `Detergents_Paper`: annual spending (m.u.) on detergents and paper products (Continuous);
6) `Delicatessen`: annual spending (m.u.) on and delicatessen products (Continuous); 
7) `Channel`: {Hotel/Restaurant/Cafe - 1, Retail - 2} (Nominal)
8) `Region`: {Lisbon - 1, Oporto - 2, or Other - 3} (Nominal) 
