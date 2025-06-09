from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
<<<<<<< HEAD
    return '<h1> This is King Virat </h1><br><p>Thank you for reading this. hope you enjoyed it, follow for more content around Devops.</p> '
=======
    return '<h1> This is King Virat </h1><br><p>Thank you for reading. I hope you enjoyed it, follow for more content around Devops.</p> '
>>>>>>> 320538a07ab71cb77dc580492d5040ef943dac21

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
# test trigger
