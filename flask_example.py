from flask import Flask, jsonify,request
import pandas as pd
from app.collaborative_filtering import CF
from app import popularity
import numpy as np

app = Flask(__name__)

r_cols = ['us'
          'er_id', 'item_id', 'rating', 'timestamp']
ratings = pd.read_csv('./data/recommendation_systems/ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')

i_cols = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
item = pd.read_csv('./data/recommendation_systems/ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')

Y_data = ratings.values
rs = CF(Y_data=Y_data, Item=item, k=2, uuCF=1)
rs.fit()
# id of users
users = Y_data[:, 0] + 1




@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/movie', methods=['GET'])
def recommend_movie():
    user_id = request.args.get('user_id', type=int)
    if user_id in users:
        res = rs.print_recommendation_one_user(user_id)
    else:
        res = popularity.recommend_population()
    return jsonify(res.to_dict('records'))


if __name__ == "__main__":
    app.run()
