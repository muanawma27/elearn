import pandas as pd
# import os
import sqlite3 as sql
# import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# %%
# ds = pd.read_csv("./sample-data.csv")
conn = sql.connect('db.sqlite3')
ds =pd.read_sql('SELECT id,title FROM  contents_post;', conn)

# %%
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['title'])


# %%
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}


# %%
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

    results[row['id']] = similar_items[1:]


# %%
def item(id):
    return ds.loc[ds['id'] == id]['title'].tolist()[0].split(' - ')[0]


# %%
def recommend(item_id, num):
    print("Recommending " + str(num) + " title similar to " + item(item_id) + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        return item(rec[1])


# %%
# recommend(item_id=11, num=5)
