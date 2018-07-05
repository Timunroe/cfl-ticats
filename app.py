from flask import Flask, render_template, request, url_for, redirect
import model
import arrow
import config as cfg
import fetch
import data

app = Flask(__name__)

#[ ROUTES ]----------

@app.route('/')
def index():
    return redirect(url_for('lineup'))

@app.route('/preview')
def preview():
    template_data = {"posts": model.get_lineup()}
    return render_template('preview.html', data=template_data)

@app.route('/lineup', methods=['GET', 'POST'])
def lineup():
    # get data
    if request.method == 'POST':
        if request.form['action'] == 'save':
            model.parse_form(request.form)
        if request.form['action'] == 'deploy':
            model.parse_form(request.form)
            data.build_template()
            fetch.put_S3()
        if request.form['action'] == 'fetch':
            model.get_new_data()
    template_data = {"items": model.get_lineup()}
    return render_template('lineup.html', data=template_data, draft_check=False)


@app.route('/drafts', methods=['GET', 'POST'])
def drafts():
    if request.method == 'POST':
        model.parse_form(request.form)
    template_data = {"items": model.get_drafts()}
    # print("template data is:")
    # print(template_data)
    return render_template('drafts.html', data=template_data)


@app.route('/view/<record_id>', methods=['GET', 'POST'])
def view_entry(record_id):
    if request.method == 'POST':
        if request.form['action'] == 'save':
            # print("+++++++++++\nWe're in post method of drafts page")
            model.parse_form(request.form, "item")
        if request.form['action'] == 'cancel':
            return redirect(url_for('lineup'))
    template_data = model.get_record(s_id=record_id)
    # print(template_data)
    # template_data['modDate'] = (arrow.get(template_data['modDate'])).to('US/Eastern').format('YYYY-MM-DD h:mm a')
    # print(template_data)
    return render_template('item.html', data=template_data[0])


@app.route('/about')
def about():
    return render_template('about.html')

# [MAIN]-----------------

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)