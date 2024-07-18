from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def madlib_completed():
    return render_template('madlib.html')

@app.route('/completed', methods=['GET','POST'])
def fill_in_black():
    if request.method == "POST":
        noun = request.form['noun']
        verb = request.form['verb']
        adverb = request.form['adverb']
        adjective = request.form['adjective']
        place = request.form['place']

        madlib_story = f"In a sleepy village called {place} nestled by a tranquil river, lived a curious cat named Whiskers. He loved to {verb} {adverb} through the place, chasing {noun}. One day, he discovered a {adjective} {noun} tucked beneath an old {noun}. With a {adjective}  {verb}, he {verb} it and {adverb} dashed home, where its {adjective} magic brought joy to everyone in the village"
        return render_template('completed.html', madlib_story=madlib_story)
    else:
        return ("Try again")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
