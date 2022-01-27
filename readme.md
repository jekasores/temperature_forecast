## Table of Contents
* [1) Instalation](#installation)
* [2) Project Motivation](#motivation)
* [3) File Descriptions](#file)
* [4) Results](#results)
* [5) Licesing, Authors, Acknowledgements](#licesing)

## 1) Instalation <a class="anchor" id="installation"></a>

This project was developed in Python 3 using Jupyter Notebook 6.1.6 and Python libraries installed with Anaconda 4.8.3 for Windows.

## 2) Project Motivation <a class="anchor" id="motivation"></a>

The main goal of this project is to perform an exploratory analysis to get some valuable insights from the dataset [Bias correction of numerical prediction model temperature forecast Data Set from UCI](https://archive.ics.uci.edu/ml/datasets/Bias+correction+of+numerical+prediction+model+temperature+forecast#) that has data from Seoul South Korea summer from 2013 to 2017. In addition, the maximum temperature Next_Tmax should be predicted.

## 3) File Descriptions <a class="anchor" id="file"></a>

* **temperature_forecast.ipynb:** Jupyter notebook that contains the project description,exploratory data analysis, and model
* **eda_functions.py:** It has functions to help in the exploratory analysis process in the temperature_forecast.ipynb notebook.
* **dataset:** Folder with the dataset
	* **Bias_correction_ucl.csv:** Data from Seoul South Korea summer from 2013 to 2017

## 4) Results <a class="anchor" id="results"></a>

* It is possible to predict the temperature for this dataset using a simple machine learning model as linear regression;
* Factors as latitude, longitude, slope, month of the year, and clouds have a direct impact the temperature;
* August is the month with the highest temperature historically, however in 2017 July was the hottest month;
* It is possible to envision some next steps for this project, as:
    * Try different validation methods. The [paper](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2019EA000740) mentions hindcast validation leave-one-station-out cross validation. I would use cross-validation to start ;
    * Compare my classification method with the ones used in the paper (Random forest (RF), support vector regression (SVR), artificial network (ANN), and multi-model ensemble (MME));
    * Use more metrics to evalueate the model;
    * Plot a map with slop information using a library as geopandas;
    * It is a possibility to predict the temperature by station and also set up some ranges of temperature as classes to notify the local goverment which ones can be dangerous for the population.

## 5) Licesing, Authors, Acknowledgements <a class="anchor" id="licesing"></a>
* Dataset: [Bias correction of numerical prediction model temperature forecast Data Set](https://archive.ics.uci.edu/ml/datasets/Bias+correction+of+numerical+prediction+model+temperature+forecast#)
* Paper: [Cho, D., Yoo, C., Im, J., & Cha, D. (2020). Comparative assessment of various machine learning-based bias correction methods for numerical weather prediction model forecasts of extreme air temperatures in urban areas. Earth and Space Science.](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2019EA000740) 
