from flask import Flask, render_template, request, url_for, redirect
import model
import arrow
import config as cfg
import fetch
import data

app = Flask(__name__)

# [ ROUTES ]----------


@app.route('/')
def index():
    return redirect(url_for('lineup'))


@app.route('/preview')
def preview():
    template_data = {"posts": model.get_lineup('published')}
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
            fetch.put_S3()  # somtimes tries to send before file above finished writing!!!!
            # StackOverflow: https://stackoverflow.com/questions/36274868/saving-an-image-to-bytes-and-uploading-to-boto3-returning-content-md5-mismatch
            # My answer was to create using ".filename" then:
            #   os.rename(filename.replace(".filename","filename"))
            # This ensured the file was done being created.
        if request.form['action'] == 'fetch':
            model.get_new_data()
    template_data = {"items": model.get_lineup('published')}
    return render_template('lineup.html', data=template_data, draft_check=False)


@app.route('/drafts', methods=['GET', 'POST'])
def drafts():
    if request.method == 'POST':
        model.parse_form(request.form)
    template_data = {"items": model.get_lineup('drafts')}
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
    app.run(host='127.0.0.1', port=50001, debug=True)
