from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here you would typically check the username and password against your database
        if username == 'admin' and password == 'password':  # Example check
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home or another page after login
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')  # Render the login page

@app.route('/')
def home():
    return render_template('index.html')  # Your main page
@app.route('/')
def index():
        recipe_list = []
        if request.method == 'POST':
            search_query = request.form['query'].lower()
            recipe_list = recipes.get(search_query, ["No recipes found."])
        return render_template('index.html')


recipes = {
    'chicken': [
        "Grilled Chicken with Lemon",
        "Chicken Curry",
        "BBQ Chicken Wings"
    ],
    'ice cream': [
        "Vanilla Ice Cream",
        "Chocolate Ice Cream",
    ]
}
recipes = {
    1: {
        'name': 'Southern Fried Chicken',
        'image_url': 'https://www.thecountrycook.net/wp-content/uploads/2021/02/thumbnail-Southern-Fried-Chicken-scaled.jpg',
        'ingredients': 'Chicken, Flour, Spices',
        'instructions': 'Fry the chicken until golden brown.'
    },
    # Add more recipes here
}
@app.route('/recipe_detail/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = recipes.get(recipe_id)
    if recipe:
        return render_template('recipe_detail.html', recipe=recipe)
    else:
        return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True)