from flask import Flask, render_template
app = Flask(__name__, template_folder='./templates', static_folder='./static')


@app.route('/')
def render_the_map():
    return render_template('index.html')

@app.route('/dehradun')
def render_dehradun_map():
    return render_template('crime_mapping_dehradun.html')

@app.route('/haridwar')
def render_haridwar_map():
    return render_template('crime_mapping_haridwar.html')

@app.route('/nanital')
def render_nanital_map():
    return render_template('crime_mapping_nanital.html')

@app.route('/cluster')
def render_cluster_map():
    return render_template('crime_mapping_marker_cluster.html')

@app.route('/murder')
def render_murder_map():
    return render_template('crime_mapping_murder.html')

@app.route('/theft')
def render_theft_map():
    return render_template('crime_mapping_theft.html')

@app.route('/heatmap')
def render_heatmap_map():
    return render_template('heamap_time.html')

if __name__ == '__main__':
    app.run(debug=True)