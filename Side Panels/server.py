from flask import Flask, render_template
app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/India-link/')
def my_link():
  return render_template('crime_mapping_sf.html')

if __name__ == '__main__':
  app.run(debug=True)