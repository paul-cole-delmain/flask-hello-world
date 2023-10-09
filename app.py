app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        partner_name = request.form['partner_name']
        new_website = 'new_website' in request.form
        # You can now process the form data as required.
        # For demonstration, I'm just returning the data:
        return f'Partner Name: {partner_name}, New Website: {new_website}'

    return '''
        <form method="post">
            Partner Name: <input type="text" name="partner_name"><br>
            New Website: <input type="checkbox" name="new_website" value="true"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

