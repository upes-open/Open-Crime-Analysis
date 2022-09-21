from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_the_map():
    return render_template('crime_mapping_sf.html')

@app.route('/dehradun')
def render_dehradun_map():
    return render_template('crime_mapping_dehradun.html')

@app.route('/haridwar')
def render_dehradun_map():
    return render_template('crime_mapping_haridwar.html')

@app.route('/nanital')
def render_dehradun_map():
    return render_template('crime_mapping_nanital.html')

@app.route('/cluster')
def render_dehradun_map():
    return render_template('crime_mapping_marker_cluster.html')

@app.route('/murder')
def render_dehradun_map():
    return render_template('crime_mapping_murder.html')

@app.route('/theft')
def render_dehradun_map():
    return render_template('crime_mapping_theft.html')

@app.route('/heatmap')
def render_dehradun_map():
    return render_template('heatmap_time.html')

if __name__ == '__main__':
    app.run(debug=True)