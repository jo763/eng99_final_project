from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import csv

app = Flask(__name__)

PORT=5000

@app.route("/")
def base():

    return render_template("new_homepage.html")


@app.route("/meet_team")
def meet_team():
    return render_template("meet_team.html")


@app.route("/data", methods=['GET'])
def data():
    # /usr/src/app/Downloads
    with open('Downloads/ItJobsWatchTop30.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        jobs = []
        no1job = []
        no2job = []
        no3job = []
        counter = 1
        for row in data:
            # Skip the headers in the CSV file
            if counter == 1:
                counter += 1
                continue
            # Prepare 1st, 2nd and 3rd top results
            elif counter == 2:
                no1job.append({
                    "role": row[0],
                    "rank": row[1],
                    "rank_move": row[2],
                    "median_salary": row[3],
                    "median_percentage:": row[4],
                    "hist_ads": row[5],
                    "live_ads": row[6],
                })
                counter += 1
                continue
            elif counter == 3:
                no2job.append({
                    "role": row[0],
                    "rank": row[1],
                    "rank_move": row[2],
                    "median_salary": row[3],
                    "median_percentage:": row[4],
                    "hist_ads": row[5],
                    "live_ads": row[6],
                })
                counter += 1
                continue
            elif counter == 4:
                no3job.append({
                    "role": row[0],
                    "rank": row[1],
                    "rank_move": row[2],
                    "median_salary": row[3],
                    "median_percentage:": row[4],
                    "hist_ads": row[5],
                    "live_ads": row[6],
                })
                counter += 1
                continue

            jobs.append({
                "role": row[0],
                "rank": row[1],
                "rank_move": row[2],
                "median_salary": row[3],
                "median_percentage:": row[4],
                "hist_ads": row[5],
                "live_ads": row[6],
            })

    return render_template("datapage.html",
                           jobs=jobs, jobs1=no1job, jobs2=no2job, jobs3=no3job)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly (so this will only respond to the 404 error)
    return render_template("404page.html"), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=PORT)
