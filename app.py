from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Havelock, NC',
    'salary': 'USD $130,000',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Havelock, NC',
    'salary': 'USD $140,000',
}, {
    'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Havelock, NC',
    'salary': 'USD $150,000',
}
}, {
    'id': 4,
    'title': 'BackEnd Engineer',
    'location': 'Havelock, NC',
    'salary': 'USD $120,000',
}]


@app.route("/")
def hello_world():
  return render_template("index.html", jobs=JOBS, company_name='Brovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
