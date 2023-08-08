from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    job_data = []  

    if request.method == 'POST':
        job_title = request.form['job_title']

        job_data = fetch_job_data(job_title)

    return render_template('index.html', job_data=job_data)

def fetch_job_data(job_title):
    
    url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"
    params = {
        "app_id": "4ee8094e", 
        "app_key": "4e11c1bf6e7c7fb81114bcbbdebf72f6",  
        "results_per_page": 20,
        "what": job_title,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        job_data = response.json()
        return job_data
    else:
        print("Error fetching job listings:", response.status_code)
        return []

if __name__ == '__main__':
    app.run(debug=True)
