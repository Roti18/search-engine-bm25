from flask import Flask, render_template, request

app = Flask(__name__)

def tambah(a, b):
    return a + b

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        angka1 = int(request.form['angka1'])
        angka2 = int(request.form['angka2'])
        hasil = tambah(angka1, angka2)
    return render_template('index.html', hasil=hasil)


if __name__ == "__main__":
  app.run(debug=True)