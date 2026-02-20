import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Contact Route (GET + POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now, just print to terminal
        print("New Contact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
