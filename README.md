Project final report is: DSCI551_proj_final_report_team#5.pdf

All the codes and files are in the 'code' folder, including: 
1. 
Data_pre_process.ipynb 
This is for data pre-process purpose. It fills up missing value, cleaned useless columns, generated three splitted datasets, and saved the cleaned raw dataset to ‘employment_dataset.csv’ 

2. 
Employment_dataset.csv
This is the updated raw dataset containing all entries with added top 10 skills with numerical values (0 if no, 1 if yes).
These are three cleaned datasets for model training:
	train_set.csv
	test_set.csv
	valid_set.csv

3.
Data_process.py This file contains important functions that help processing data.	
	Usage: from data_process import xxx

4. 
Exploratory_data_analysis.ipynb This file is where you do all the exploratory data analysis. 

5. 
There are 4 seperate ipynb files that are implementing machine learning methods to build predictive models. They are:
	decisionTree.ipynb   
	logisticRegression.ipynb
	XGBoost.ipynb
	randomForest.ipynb
	
6.
stackoverflow_full.csv
The original dataset.
