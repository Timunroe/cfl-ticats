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
                <h3 style="margin-top: 8px; margin-bottom: 6px; color: black; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif; font-weight: 500;" class="">{{ item['title_api']|safe|replace("WORLD CUP:", "") }}</h3>
                <p class=""><small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<!--STATS HEADER START-->
<section id="stats_header" style="margin-bottom: 0.5rem;" class="mb2">

    <section id="1" style="padding-bottom: 0.75rem; border" class="pb3 bb b--black-10 sans-serif">
      <div style="floate: left; margin: 0; font-weight: bold; padding-right: 0.23 rem; text-transform: uppercase;" class="fl f6 ma0 b pr2 ttu">Week 2</div>
      <div style="display: flex; flex-wrap: wrap;" class="flex flex-wrap">
        <div style="margin: 0; padding-left: 0.25 rem; padding-left: 0.25 rem;" class="f6 ma0 ph2 bl-ns">June 21: SSK @ OTT, 7:30pm</div>
        <div style="margin: 0; padding-left: 0.25 rem; padding-left: 0.25 rem;" class="f6 ma0 ph2 bl-ns">June 22: WPG @ MTL, 7pm</div>
        <!-- <div class="f6 ma0 ph2 bl-ns">June 16: HAM @ CGY, 7pm</div> -->
        <div style="margin: 0; padding-left: 0.25 rem; padding-left: 0.25 rem;" class="f6 ma0 ph2 bl-ns">June 23: CGY @ TOR, 7pm</div>
      </div>
    </section>
    <!--END 1 -->

    <section id="2" class="flex flex-wrap pt2 pb3 bb b--black-10 sans-serif">

      <div class="br-ns b--black-20 pr3">
        <p class="agate b mv1 ttu silver">last game</p>
        <p class="f4 fw2 mv1 flex justify-between"><span class="pr1">Tiger-Cats</span><span>14</span></p>
        <p class="f4 fw2 mv1 flex justify-between"><span class="pr1">Stampeders</span><span>28</span></p>
        <p class="f6 mt2 mb0 dn db-ns">June 16 @ Calgary</p>
      </div>

      <div class="pl3">
        <p class="agate b mv1 ttu">next game</p>
        <p class="f4 mv1">Tiger-Cats <small>(0-1)</small></p>
        <p class="f4 mv1">Eskimos <small>(1-0)</small></p>
        <p class="f6 mt2 mb0">June 22, 10pm @ Edmonton</p>
      </div>

      <div class="pl3 dn db-ns">
        <p class="agate b mv1 ttu silver">How they compare (per game)</p>
        <p class="f4 fw1 mv1 mt1">14 pts, 56 rushing yards, 385 total yards</p>
        <p class="f4 fw1 mv1">33 pts, 79 rushing yards, 481 total yards</p>
        <p class="f6 mt2 mb0 dn db-ns"></p>
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
