page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>World Cup curator</title>
    <link rel="stylesheet" href="https://unpkg.com/tachyons@4.8.0/css/tachyons.min.css"/>
    <style type="text/css">
        $css
    </style>

</head>
    <body style="max-width: 800px;margin: auto;">
        $core
    </body>
</html
'''

core_template = '''\

{% macro show_post(item) %}
    <article class="pica-card pica-fade" style="margin-top: 18px;">
        {% if item['img_api'] != '' %}
        <div class="pica-card-image">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <div class="pica-image-wrapper" style="">
                    <img class="pica-image" style="" src="{{ item['img_api'] }}">
                </div>
            </a>
        </div>
        {% endif %}
        <div class="pica-card-text">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <h3 style="margin-top: 8px; margin-bottom: 6px;" class="">{{ item['title_api']|safe|replace("WORLD CUP:", "") }}</h3>
                <p class=""><small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<!--STATS HEADER START-->
<section id="stats_header" style="margin-bottom: 0.5rem;" class="mb2">

    <section style="padding-bottom: 0.8rem; border-bottom-style: solid; border-bottom-width: 1px; border-bottom-color: silver; font-family: -apple-system, BlinkMacSystemFont, avenir, \\\'helvetica neue\\\', helvetica, ubuntu, roboto, noto, arial, sans-serif;" class="">
      <div style="font-size: 0.9rem; float: left; margin: 0; font-weight: 800; padding-right: 0.25rem; text-transform: uppercase;" class="f6">Week 2 | </div>
      <div style="display: flex; flex-wrap: wrap;" class="">
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 21: SSK @ OTT, 7:30pm | </div>
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 22: WPG @ MTL, 7pm | </div>
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 23: CGY @ TOR, 7pm</div>
      </div>
    </section>
    <!--END 1 -->

    <section style="display: flex; flex-wrap: wrap; padding-top: 0.5rem; padding-bottom: 0.75rem; font-family: sans-serif;" class="bb b--black-10">

      <div style="padding-right: 0.8rem; border-right-style: solid; border-right-width: 1px; border-bottom-color: silver;" class="">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase; color: silver;" class="agate">last game</p>
        <p style="font-size: 1.25rem; font-weight: 200; margin-top: 0.25rem; margin-bottom: 0.25rem; display: flex; justify-content: space-between;" class="f4"><span style="padding-right: 0.25rem;" class="">Tiger-Cats</span><span>14</span></p>
        <p style="font-size: 1.25rem; font-weight: 200; margin-top: 0.25rem; margin-bottom: 0.25rem; display: flex; justify-content: space-between;" class="f4 justify-between"><span style="padding-right: 0.25rem;" class="">Stampeders</span><span>28</span></p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; margin-bottom: 0;" class="dn db-ns">June 16 @ Calgary</p>
      </div>

      <div style="padding-left: 0.8rem;" class="">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase;" class="agate">next game</p>
        <p style="font-size: 1.25rem; font-weight: 400; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="">Tiger-Cats <small>(0-1)</small></p>
        <p style="font-size: 1.25rem; font-weight: 400; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="">Eskimos <small>(1-0)</small></p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; margin-bottom: 0;" class="">June 22, 10pm @ Edmonton</p>
      </div>

      <div style="padding-left: 0.8rem;" class="dn db-ns">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase; color: silver;" class="agate">How they compare (per game)</p>
        <p style="font-size: 1.25rem; font-weight: 100; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="f4">14 pts, 56 rushing yards, 385 total yards</p>
        <p style="font-size: 1.25rem; font-weight: 100; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="f4">33 pts, 79 rushing yards, 481 total yards</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; margin-bottom: 0;" class="dn db-ns"></p>
      </div>

    </section>
    <!--END 2 -->

    </section>
    <!--STATS HEADER END-->
<hr>
<!-- CURATION LIST -->
<section class="pica-cards">
    {%- for item in data['posts'] -%}
        {{ show_post(item) }}
    {%- endfor %}
</section>
<!-- END CURATION LIST -->
'''

script_template = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;

'''
