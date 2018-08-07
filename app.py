from flask import Flask, render_template, request, url_for, redirect
import model
import config as cfg
import fetch
import data

app = Flask(__name__)

# [ ROUTES ]----------


@app.route('/')
def index():
    return redirect(url_for('feed'))


@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if request.form['action'] == 'fetch':
        model.get_new_data()
    template_data = {"items": model.get_posts('published')}
    return render_template('feed.html', data=template_data)


@app.route('/db_drafts', methods=['GET', 'POST'])
def drafts():
    if request.method == 'POST':
        model.parse_form(request.form)
    template_data = {"items": model.get_posts('drafts')}
    # print("template data is:")
    # print(template_data)
    return render_template('db_drafts.html', data=template_data)


@app.route('/db_archives')
def archives():
    template_data = {"items": model.get_posts('archives')}
    return render_template('db_archives.html', data=template_data)


@app.route('/preview/<page_id>')
def preview(page_id):
    file_name = f'pages_{page_id}_preview.html'
    template_data = {"posts": model.get_posts('published')}
    return render_template(file_name, data=template_data)


@app.route('/about/<page_id>')
def about(page_id):
    file_name = f'pages_{page_id}_about.html'
    return render_template(file_name)


@app.route('/pages/<page_id>', methods=['GET', 'POST'])
def lineup(page_id):
    # get data
    file_name = f'pages_{page_id}_lineup.html'
    if request.method == 'POST':
        if request.form['action'] == 'save':
            model.parse_form(request.form)
        if request.form['action'] == 'deploy':
            model.parse_form(request.form)
            data.build_template()
            fetch.put_S3()  # sometimes tries to send before file above finished writing!!!!
            # StackOverflow: https://stackoverflow.com/questions/36274868/saving-an-image-to-bytes-and-uploading-to-boto3-returning-content-md5-mismatch
            # My answer was to create using ".filename" then:
            #   os.rename(filename.replace(".filename","filename"))
            # This ensured the file was done being created.
        if request.form['action'] == 'fetch':
            model.get_new_data()
    template_data = {"items": model.get_lineup('published')}
    return render_template(file_name, data=template_data, draft_check=False)


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
    return render_template('db_item.html', data=template_data[0])


# [MAIN]-----------------

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=50001, debug=True)
