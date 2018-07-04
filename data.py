from jinja2 import Environment, FileSystemLoader
from string import Template
import htmlmin
import io
import data_templates as tmpl
import fetch
import model
import config as cfg

# Put <script src="https://picabot.s3.amazonaws.com/pagejs/ticats_spec.js"></script> in DNN footer
# put <div class="pica-results"></div> in DNN body


def minify_html(s_html):
    # returns string of minified html
    return htmlmin.minify(s_html, remove_comments=True, remove_empty_space=True)


def save_file_overwrite(s_contents, s_name):
    print("Now in save file module")
    build_directory = 'build'
    with io.open(f"{build_directory}/{s_name}", "w+", encoding='utf8') as file:
        file.write(s_contents)
    print(f"File saved in {build_directory}: {s_name}")
    return


def build_template():
    # NEED TO CREATE BUILD DIRECTORY IF IT DOESN'T EXIST!!!
    print("Building template for DNN")
    template_data = {"posts": model.get_lineup()}
    # using Jinja2 string was fun, but let's get back to includes and other good stuff
    # html = Environment().from_string(tmpl.core_template).render(data=template_data)
    j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
    html = j2_env.get_template('ext_core.html').render(data=template_data)
    html_minified = minify_html(html)
    css = fetch.fetch_css()
    script = Template(tmpl.script_template).substitute(css=css, minified=html_minified)
    script_name = f"{cfg.config['project_name']}_{cfg.config['name']}.js"
    save_file_overwrite(script, script_name)
    pass


if __name__ == "__main__":
    # call api, update database
    model.get_new_data()
    # build template
    build_template()
