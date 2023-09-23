import movie # importing movie.py
from flask import Flask, render_template, request, jsonify, redirect,url_for
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/recommend',methods=['GET','POST'])
def recommend():
    movie_df=movie.new_df
    movie_title=movie_df['title'].values
    return render_template('recommend.html',movie_title=movie_title)

@app.route('/recommended_movies' ,methods=['GET','POST'])
def product():
    if request.method=="POST":
        movies=request.form['movies']
        if movies == 'Select movie here':
            return redirect('/')
        else:
            poster,recommended_movies=movie.recommend(movies)
            return render_template('predict.html',movies=movies,recommended_movies=recommended_movies,poster=poster)
    else:
        return render_template('predict.html')


@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')


if __name__=="__main__":
    app.run(debug=True,port=8000)

