# **Movie-recomdation-system**

The recommendation system plays a large role in the  streaming services and shopping sites.
There are several ways to do it chief among them are ways to do it chief among them are </br>
    1. Based on Popularity </br>
    2. Based on Content user viewed </br>
    3. Based on behaviour of similar user </br>
For creating the following model we use Dataset called MovieRecomendation from kaggle, link for which is given below  </br>
https://www.kaggle.com/rounakbanik/the-movies-dataset
## **Based on Popularity** ##
In this method we simply recommend top20 most popular movies at time of the usage of the application, In the dataset which I used i did it by organizing the popularity in Decsending order. </br>
</br>
</br>
![](image/Screenshot%20(44).png)</br>

The above image shows the code for doing the recomendation based on popularity I have used pandas for importing data and manupilating,All the code up to line 35 is to clean the data rest of the code is for displaying the data </br>

![](image/Screenshot%20(47).png)</br>

The above image shows the result for most popular movies in the above dataset</br>
</br>

## **Based on the Content user viewed** ##
In this technique the recommendation based on the type of movie, for example if an user based on the type of the movie, like action,crime etc.</br>

![](image/Screenshot%20(49).png)</br>

First step would be merging all the important data into one sentence, which is subject to natural language processing. This is Done using CountVectorizer from scikit learn and NLTK

![](image/Screenshot%20(49).png)</br>

![](image/Screenshot%20(53).png)</br>
![](image/Screenshot%20(54).png)</br>
![](image/Screenshot%20(55).png)</br>

The above screenshots shows how to use various libraries and also the output result for the movie 'Toy Story' is shown</br>

## ** Based on similar users ** ##
This is the last technique i am going to display for movie recommendation system, it is based on the similarity of two users, for this end we are going to use K-nearest neighbors technique for this purpose, we use ratings.csv of the dataset, first we need to convert the dataset into a matrix of rating and user, and training a model using this data </br>
![](image/Screenshot%20(60).png)</br>
The above diagram shows how the dataframe is converted to matrix using pivot function.</br>
![](image/Screenshot%20(61).png)</br>
The KNN is initialized and data is fit</br>
![](image/Screenshot%20(62).png)</br>
The recomender is a function which takes the name of the movie and gives the list of movies similar user see.
![](image/Screenshot%20(63).png)</br>
The picture shows the result for the movie batman, there low accuracy in this result due to the small dataset i used due limitatio on my PC


    

