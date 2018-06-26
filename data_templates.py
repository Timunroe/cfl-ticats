page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>CFL-Ticats curator</title>
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
                <h3 style="margin-top: 8px; margin-bottom: 6px;" class="">{{ item['title_api']|safe }}</h3>
                <p class=""><small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<!--STATS HEADER START-->
<section id="stats_header" style="margin-bottom: 0.5rem;" class="mb2">

    <section style="padding-bottom: 0.8rem; border-bottom-style: solid; border-bottom-width: 1px; border-bottom-color: #99A3A4; font-family: -apple-system, BlinkMacSystemFont, avenir, \\\'helvetica neue\\\', helvetica, ubuntu, roboto, noto, arial, sans-serif;" class="">
      <div style="font-size: 0.9rem; float: left; margin: 0; font-weight: 800; padding-right: 0.25rem; text-transform: uppercase;" class="f6">Week 2 | </div>
      <div style="display: flex; flex-wrap: wrap;" class="">
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 21: SSK 17 @ OTT 40 | </div>
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 22: WPG 56, MTL 10 | </div>
        <div style="font-size: 0.9rem; margin: 0; padding-left: 0.25rem; padding-left: 0.25rem;" class="f6 bl-ns">June 23: CGY @ TOR, 7pm</div>
      </div>
    </section>
    <!--END 1 -->

    <section style="display: flex; flex-wrap: wrap; padding-top: 0.5rem; padding-bottom: 0.75rem; font-family: sans-serif;" class="bb b--black-10">

      <div style="padding-right: 0.8rem; border-right-style: solid; border-right-width: 1px; border-bottom-color: #99A3A4;" class="">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase; color: #99A3A4;" class="agate">last game</p>
        <p style="font-size: 1.25rem; font-weight: 200; margin-top: 0.25rem; margin-bottom: 0.25rem; display: flex; justify-content: space-between;" class="f4"><span style="padding-right: 0.25rem;" class="">Tiger-Cats</span><span>38</span></p>
        <p style="font-size: 1.25rem; font-weight: 200; margin-top: 0.25rem; margin-bottom: 0.25rem; display: flex; justify-content: space-between;" class="f4 justify-between"><span style="padding-right: 0.25rem;" class="">Eskimos</span><span>21</span></p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; margin-bottom: 0;" class="dn db-ns">June 22 @ Edmonton</p>
      </div>

      <div style="padding-left: 0.8rem;" class="">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase;" class="agate">next game</p>
        <p style="font-size: 1.25rem; font-weight: 400; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="">Bombers <small>(1-1)</small></p>
        <p style="font-size: 1.25rem; font-weight: 400; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="">Tiger-Cats <small>(1-1)</small></p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem; margin-bottom: 0;" class="">June 29, 7pm @ Hamilton</p>
      </div>

      <div style="padding-left: 0.8rem;" class="dn db-ns">
        <p style="font-weight: bold; margin-top: 0.25rem; margin-bottom: 0.25rem; text-transform: uppercase; color: #99A3A4;" class="agate">How they compare (per game)</p>
        <p style="font-size: 1.25rem; font-weight: 100; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="f4">43 pts, 191 rushing yards, 451.5 total yards</p>
        <p style="font-size: 1.25rem; font-weight: 100; margin-top: 0.25rem; margin-bottom: 0.25rem;" class="f4">26 pts, 126 rushing yards, 464 total yards</p>
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

<!-- START STANDINGS LIST -->
 <section id="pica-standings" style="" class="w-100 order-1-ns w-25-ns pl3-ns">
      <h3 class="agate b mv1 ttu silver sans-serif">Standings</h3>
      <div class="flex flex-wrap">
        <table class="tg w-100 tl sans-serif">
          <tr>
            <th class="tg-yw4l">East</th>
            <th class="tg-yw4l">W</th>
            <th class="tg-yw4l">L</th>
            <th class="tg-yw4l">T</th>
          </tr>
          <tr>
            <td class="tg-yw4l">Redblacks</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Ticats</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Argonauts</td>
            <td class="tg-yw4l">0</td>
            <td class="tg-yw4l">2</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Alouettes</td>
            <td class="tg-yw4l">0</td>
            <td class="tg-yw4l">2</td>
            <td class="tg-yw4l">0</td>
          </tr>
        </table>
        <table class="tg w-100 tl sans-serif">
          <tr>
            <th class="tg-yw4l">West</th>
            <th class="tg-yw4l">W</th>
            <th class="tg-yw4l">L</th>
            <th class="tg-yw4l">T</th>
          </tr>
          <tr>
            <td class="tg-yw4l">Stampeders</td>
            <td class="tg-yw4l">2</td>
            <td class="tg-yw4l">0</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Lions</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Eskimos</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Riders</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
          </tr>
          <tr>
            <td class="tg-yw4l">Bombers</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">1</td>
            <td class="tg-yw4l">0</td>
          </tr>

        </table>
      </div>
    </section>
<!--END STANDINGS-->

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

var ids_to_hide = ["div1702", "div1703", "div3404", "div3495"];
var selectors_to_hide = ["#div1195 div section", "#div1195 div p", "#div3472 div section", "#div3472 div p"];
var el;

for (item in ids_to_hide) {
  try {
    el = document.getElementById(ids_to_hide[item]);
    el.style.display = 'none';
  }
  catch(err) {
  }
}
for (item in selectors_to_hide) {
  try {
    el = document.querySelector(selectors_to_hide[item]);
    el.style.display = 'none';
  }
  catch(err) {
  }
}

function pica_tabs_handler(e) {
	// deal with tab-controls
  var tab_id = this.getAttribute('data-tab');
  // reset all tab controls of specific block to default class 
  var tab_controls = this.parentNode.querySelectorAll('.pica-tab-control');
  Array.prototype.forEach.call(tab_controls, function(el, i) {
    el.className = 'pica-tab-control'; // set tab controls to base class
  });
  // set class of selected tab control in specific block to active
  this.className = 'pica-tab-control active';
  // deal with tab-panels
  // select all panels in the data-block with this data-tab number
  var panel_block = this.parentNode.parentNode.querySelector('.pica-tab-panels');
  // hide them
  Array.prototype.forEach.call(panel_block.querySelectorAll('.pica-tab-panel'), function(el, i) {
    el.style.display = 'none'; 
  });
  // unhide the panel whose data-tab number is same as clicked control
  var this_panel = panel_block.querySelector('[data-tab="' + tab_id + '"]');
  // var this_panel = these_panels.querySelector('[data-tab-panel="' + tab_id + '"]');
  this_panel.style.display = 'block';
}

// start by applying listeners to tab controls
var tab_controls = document.querySelectorAll('.pica-tab-controls .pica-tab-control');
Array.prototype.forEach.call(tab_controls, function(el, i) {
  el.addEventListener('click', pica_tabs_handler, false);
});
// select default tab
var defaults = document.querySelectorAll('.pica-tab-control[data-tab-default="yes"]')
Array.prototype.forEach.call(defaults, function(el, i) {
  el.click();
});

'''
