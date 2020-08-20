import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

##Step 1: Load the dataset to pandas data frame and Read the contents from CSV File 

df=pd.read_csv("movie_dataset.csv")
print(df.columns)

##Step 2: Select Features We just select
features=['keywords','cast','genres','director']

##Step 3: Create a column in DataFrame which combines all selected features
for feature in features:
	df[feature]=df[feature].fillna('')
#replace null valus with null string
def combine_features(row):
	try:
		return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
	except:
		print("Error:",row)
#method to use to apply function to all rows in the dataframe
df["combined_features"]=df.apply(combine_features,axis=1)
#print("Combined Features:\n",df["combined_features"].head())


##Step 4: Create count matrix from this new combined column
cv=CountVectorizer()
count_matrix=cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix

cosine_sim=cosine_similarity(count_matrix)
movie_user_likes = input("Enter the movie:")

## Step 6: Get index of this movie from its title

movie_index= get_index_from_title(movie_user_likes)
similar_movies=list(enumerate(cosine_sim[movie_index]))



## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
i=0
for movie in sorted_similar_movies:
	print(get_title_from_index(movie[0]))
	i=i+1
	if i>50:
		break

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text=["London Paris London","Paris Paris London"]
cv=CountVectorizer()
count_matrix=cv.fit_transform(text)
#print(count_matrix.toarray())
similarity_scores=cosine_similarity(count_matrix)
#print(similarity_scores)
