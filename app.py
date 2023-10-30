from flask import Flask, render_template, request, flash
from yt_to_mp3 import downloader
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        link = request.form.get("link")
        # Process the 'link' variable, e.g., download the content.
        # Return the appropriate response here.
        downloader(link)
        return render_template('download.html',link=link)
    flash("Url Not Found")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
