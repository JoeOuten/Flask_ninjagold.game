from flask import Flask, render_template, session, redirect, request
import time
import random
app = Flask(__name__)
app.secret_key = "jtrsghtshsrhgfseryhjuku"
messages = []


@app.route('/')
def index():
    if session.get('YourGold'):
        pass
    else:
        session['YourGold'] = 0
    return render_template('index.html', messages=messages)


@app.route('/process_money', methods=['POST'])
def gold():
    if request.form['process'] == 'farm':
        value = random.randrange(9, 21)
        session['YourGold'] += value
        messages.insert(0, ("You earned " + str(value) + " gold from the farm! " +
                        str(time.strftime("%d/%m/%Y %I:%M %p"))))

    elif request.form['process'] == 'cave':
        value = random.randrange(4, 11)
        session['YourGold'] += value
        messages.insert(0, ("You earned " + str(value) + " gold from the cave! " +
                        str(time.strftime("%d/%m/%Y %I:%M %p"))))

    elif request.form['process'] == 'house':
        value = random.randrange(2, 6)
        session['YourGold'] += value
        messages.insert(0, ("You earned " + str(value) + " gold from the house! " +
                        str(time.strftime("%d/%m/%Y %I:%M %p"))))

    elif request.form['process'] == 'casino':
        value = random.randrange(-50, 51)
        session['YourGold'] += value
        if value > 0:
            messages.insert(0, ("You earned" + str(value) + " gold from the farm! " +
                            str(time.strftime("%d/%m/%Y %I:%M %p"))))
        else:
            messages.insert(0, ("You entered a casino and lost " + str(value) +
                            " gold...better luck next time" + str(time.strftime("%d/%m/%Y %I:%M %p"))))

    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('YourGold')

    for i in range(0, len(messages)):
        messages.pop()

    return redirect('/')


app.run(debug=True)
