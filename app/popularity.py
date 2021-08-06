import pandas as pd
# reading user file
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('./data/recommendation_systems/ml-100k/u.user',
                    sep='|', names=u_cols, encoding='latin-1')

# reading ratings file
r_cols = ['user_id', 'movid_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('./data/recommendation_systems/ml-100k/ua.base',
                           sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('./data/recommendation_systems/ml-100k/ua.test',
                           sep='\t', names=r_cols, encoding='latin-1')

rate_train = ratings_base.values
rate_test = ratings_test.values


# reading items file
i_cols = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

items = pd.read_csv('./data/recommendation_systems/ml-100k/u.item',
                    sep='|', names=i_cols, encoding='latin-1')

rate_train = pd.DataFrame(rate_train, columns=r_cols)

items = pd.DataFrame(items, columns=i_cols)
items = items.rename({'movie id': 'movid_id'}, axis='columns')


rate_train = rate_train.merge(items, on='movid_id')
# tinh so star trung tinh va so luong rating tuong movid
average_star_on_movie = rate_train[['movid_id', 'rating']].groupby(by=['movid_id']).agg(['mean', 'count'])

mean_rating = average_star_on_movie['rating']['count'].mean()
mean_count = average_star_on_movie['rating']['mean'].mean()

# tinh count quantitle
m = average_star_on_movie['rating']['count'].quantile(0.9)

# loai cac ban ghi ra nho hon count quantitle

average_star_on_movie = average_star_on_movie.loc[average_star_on_movie['rating']['count'] >= m]

# tinh lai count va mean
mean_rating = average_star_on_movie['rating']['count'].mean()
mean_count = average_star_on_movie['rating']['mean'].mean()

# tinh score cho film
def weight_rating(x, m=mean_count, C=mean_rating):
    v = x['rating']['count']
    R = x['rating']['mean']
    return (v/(v+m) * R) + (m/(m+v) * C)

average_star_on_movie['score'] = average_star_on_movie.apply(weight_rating, axis='columns')
average_star_on_movie = average_star_on_movie.sort_values('score', ascending=False)

def get_index_by_name(average_star_on_movie):
    index = []
    for i in average_star_on_movie.iterrows():
        index.append(i[0])
    return index

def recommend_population():

    index = get_index_by_name(average_star_on_movie.iloc[:10])
    return items[['movid_id', 'movie title', 'IMDb URL']].iloc[index]

# print(average_star_on_movie.iloc[0])
#
# print(average_star_on_movie.iloc[0].name)

# print(average_star_on_movie['movid_id'])

# items = items.merge(average_star_on_movie, on='movid_id')

# if __name__ == "__main__":
#     print(recommend_population())