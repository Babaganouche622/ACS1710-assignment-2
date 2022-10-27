from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal?<br/>
        <input type="text" name="animal"><br/>
        What is your favorite city?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')
    return f"Wow, I didn't know {users_favorite_color} {users_favorite_animal}s lived in {users_favorite_city}!"

@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        What is your secret message? <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    users_message = request.form.get('message')
    return sort_letters(users_message)

@app.route('/calculator')
def calculator():
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    number1 = int(request.args.get('operand1'))
    number2 = int(request.args.get('operand2'))
    operator = request.args.get('operation')

    if operator == 'multiply':
        answer = (number1 * number2)
    elif operator == 'divide':
        answer = (number1 / number2)
    elif operator == 'add':
        answer = (number1 + number2)
    elif operator == 'subtract':
        answer = (number1 - number2)

    # phrase =f"You chose to {operator} {number1} and {number2}. Your result is: {answer}"

    context = {
        'number1': number1,
        'number2': number2,
        'operator': operator,
        'answer': answer,
    }

    return render_template('/calculator_results.html', **context)
    # f"You chose to {operator} {number1} and {number2}. Your result is: {answer}"
    # 

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')
    users_name = request.args.get('users_name')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    for horoscope in HOROSCOPE_PERSONALITIES:
        if horoscope == horoscope_sign:
            users_personality = HOROSCOPE_PERSONALITIES[horoscope]

    # TODO: Generate a random number from 1 to 99
    lucky_number = randint(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        'users_name': users_name
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
