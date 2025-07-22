from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    return render_template("index.html", name="John")
                  
@views.route('/profile')
def profile():
    args = request.args # Query parameters ?name=John
    name = args.get('name')
    return render_template("index.html", user=name)

@views.route('/json')
def get_json():    
    return jsonify({'name': 'Timmy', "age": "32", "city": "New York"})

@views.route('/go_home')
def go_home():
    return redirect(url_for('views.home'))  #Redirects 