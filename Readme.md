# Myers–Briggs Type Indicator (MBTI) Classification using text data extracted from Twitter
 **MBTI** is an acronym for **Myers Briggs Type Indicator**. This is a common technique for assisting people in understanding their own communication preferences and how they communicate with others. Knowing what MBTI stands for will help you adjust your interpersonal approach to various situations and audiences.

# DataSource
**(MBTI) Myers-Briggs Personality Type Dataset**:
This data was gathered from the **PersonalityCafe forum**, which has a significant number of individuals, their MBTI personality types, and what they have posted. This dataset contains over 8600 rows of data, on each row is a person’s Type (This persons 4 letter MBTI code/type) and a section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters)).
>  [Kaggle Link](https://www.kaggle.com/datasnaek/mbti-type)

## Why this project makes sense?
	•Meta programmers, which are habitual ways of inputting, sorting and filtering the information found in the world around us, are a vital factor in Neuro Linguistic Programming (NLP) .
	•The Myers–Briggs Type Indicator (MBTI) is currently considered as one of the most popular and reliable methods.
	•In this project, a new machine learning method has been developed for personality type prediction based on the MBTI and in comparison, to other existing methods and the results show better accuracy and reliability.
	•There is significant growing interest in automated personality prediction using social media among researchers in both the Natural Language Processing and Social Science fields.
	> In Respect to a person taking the text or providing twitter id:
		•Increase self-awareness
		•Discover how people differ in terms of energy sources, information gathering, decision-making, and lifestyle.
		•Develop a respect for each person's unique talents and abilities.
		•Learn how to improve your team's performance by using your own and others' skills.
		•Compile a list of areas or possibilities for personal or professional growth.

## Objectives

We want to provide a fast and effective way for analyzing the personality type using the text data extracted from social media platforms which could be either internal or external like Twitter, Facebook, Vimeo (internal social media used by many companies), etc.

## Ethics
As Dr Isabel Briggs Myers says,
>"It is up to each person to recognize his or her true preferences."

After having introspected from our end on the possible privacy breaches that can happen, which violate the ‘self-reporting’ aspect of the MBTI model.
The user should have complete control over whether his data is shared with the organization. The user could login with their social media handle and can run the assessment only on the account they have logged into (i.e., their own account). This would protect the user data.

## How to Run the code
The code here is to be run in Jupiter Notebook or Google Colab Notebook
## Installation
[Installing Jupyter Notebook](https://test-jupyter.readthedocs.io/en/latest/install.html)

## Running Jupyter Notebook
```bash
jupyter notebook
```
## Files
	> There are 7 files i.e 2 notebook document created in Jupyter Notebook, 3 python files and 2 html files which are present in the src folder.
	Jupyter Notebook: Model generation Pipeline
	 - MBTI_Modelling_Notebook.ipynb
	 - MBTI_Modelling_Results_Visualization.ipynb
	Python Files: Deployment Pipeline
	 - MBTI_Deployment_webapp.py
	 - MBTI_Deployment_predict.py
	 - MBTI_Deployment_twitterPull.py
	Webapp Files: 2 HTML templates
	 - questionnaire.html
	 - prediction.html
