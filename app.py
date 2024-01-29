from flask import Flask, request, render_template, redirect, url_for

from forms import RecordForm
from models import records

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/records/", methods=["GET", "POST"])
def record_list():
    form = RecordForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            records.create(form.data)
            records.save_all()
        return redirect(url_for("record_list"))

    return render_template("records.html", form=form, records=records.all(), error=error)


@app.route("/records/<int:id>/", methods=["GET", "POST"])
def record_details(id):
    record = records.get(id - 1)
    form = RecordForm(data=record)

    if request.method == "POST":
        if form.validate_on_submit():
            records.update(id - 1, form.data)
            records.save_all()
        return redirect(url_for("record_list"))
    return render_template("record.html", record=record, form=form, id=id)


if __name__ == "__main__":
    app.run(debug=True)