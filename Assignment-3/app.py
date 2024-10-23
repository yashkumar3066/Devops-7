from flask import Flask, request, render_template_string, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a basic homepage
@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return "Hello, Docker! This is the homepage."

# Define a route for a user profile
@app.route('/profile/<username>')
def profile(username):
    app.logger.info(f'Profile page accessed for user: {username}')
    return f"Welcome to {username}'s profile!"

# Define a route for form submission
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Simulate processing form data
        data = request.form.to_dict()
        app.logger.info(f'Form submitted with data: {data}')
        return jsonify({"message": "Form submitted successfully!", "data": data})
    else:
        # Simple form for GET request
        form_html = '''
        <form method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br>
            <input type="submit" value="Submit">
        </form>
        '''
        return render_template_string(form_html)

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(f'404 error: {e}')
    return "This page does not exist. Please check the URL.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
