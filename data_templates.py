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

<!-- STATIC HEADER -->

<!-- START TABS CONTROLS-->
<section pica-tabs-section>
<ul class="pica-tab-controls" style="" data-tab-block="1">
    <li class="pica-tab-control" data-tab="1" data-tab-default="yes">Next matches</li>
    <li class="pica-tab-control" data-tab="2">Previous</li>
    <li class="pica-tab-control" data-tab="3">Podcasts</li>
</ul>
<!-- START TABS PANELS-->
<div class="pica-tab-panels" data-tab-block="1">
    <div class="pica-tab-panel" data-tab="1">
        <p><small>All times Eastern</small></p>
        <div class="pica-tab-panel_items" style="display: flex; flex-wrap: wrap; margin: 0 -10px 0 -10px;">
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">WEDNESDAY, JUNE 20</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331511/#match-liveblog?cid=go_boxpreview">Portugal 1, Morroco 0</a></p>
                <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/iCIlEbZWITI' frameborder='0' allowfullscreen></iframe></div>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331530/#match-liveblog?cid=go_boxpreview">Uruguay 1, Saudi Arabia 0</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331496/#match-liveblog?cid=go_boxpreview">Iran vs. Spain, 2 p.m.</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 21</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331518/#match-liveblog?cid=go_boxpreview">Denmark vs. Australia, 8 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331527/#match-liveblog?cid=go_boxpreview">France vs. Peru, 11 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331513/#match-liveblog?cid=go_boxpreview">Argentina vs. Croatia, 2 p.m.</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">FRIDAY, JUNE 22</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331540/#match-liveblog?cid=go_boxpreview">Brazil vs. Costa Rica, 8 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331497/#match-liveblog?cid=go_boxpreview">Nigeria vs. Iceland, 11 a.m.</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300340183/#match-liveblog?cid=go_boxpreview">Serbia vs. Switzerland, 2 p.m.</a></p>
            </div>
        </div>
    </div>
    <div class="pica-tab-panel" data-tab="2">
        <div class="pica-tab-panel_items" style="display: flex; flex-wrap: wrap; margin: 0 -10px 0 -10px;">
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">TUESDAY, JUNE 19</h3>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331550/#match-liveblog?cid=go_boxpreview">Colombia 1, Japan 2</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331545/#match-liveblog?cid=go_boxpreview">Poland 1, Senegal 2</a></p>
                <p><a href="https://www.fifa.com/worldcup/matches/match/300331495/#match-liveblog?cid=go_boxpreview">Russia 3, Egypt 1</a></p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">MONDAY, JUNE 18</h3>
                <p>Sweden 1, South Korea 0</p>
                <p>Belgium 3, Panama 0</p>
                <p>Tunisa 1, England 2</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SUNDAY, JUNE 17</h3>
                <p>Costa Rica 0, Serbia 1</p>
                <p>Germany 0, Mexico 1</p>
                <p>Brazil 1, Switzerland 1</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">SATURDAY, JUNE 16</h3>
                <p>France 2, Australia 1</p>
                <p>Argentina 1, Iceland 1</p>
                <p>Peru 0, Denmark 1</p>
                <p>Croatia 2, Nigeria 0</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">FRIDAY, JUNE 15</h3>
                <p>Egypt 0, Uruguay 1</p>
                <p>Morocco 0, Iran 1</p>
                <p>Portugal 3, Spain 3</p>
            </div>
            <div style="flex: 1; min-width: 240px; margin: 0 10px 0 10px; margin-bottom: 6px;">
                <h3 style="margin-top: 4px; margin-bottom: 2px;">THURSDAY, JUNE 14</h3>
                <p>Russia 5, Saudi Arabia 0</p>
            </div>
        </div>
    </div>
    <div class="pica-tab-panel" data-tab="3">
        <iframe id="multi_iframe" frameborder="0" scrolling="no" allowfullscreen="" src="https://www.podbean.com/media/player/multi?playlist=http%3A%2F%2Fplaylist.podbean.com%2F759247%2Fplaylist_multi.xml&vjs=1&kdsowie31j4k1jlf913=2eb7c0cf1e0b2b2d7e13516349a49cb12aec6af8&size=240&share=1&fonts=Helvetica&auto=0&download=0&rtl=0&skin=3" width="100%" height="430"></iframe>
    </div>
</div>
</section>
<!-- END TABS -->
<!-- END STATIC HEADER -->
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

function pica_tabs_handler(e){
  var tab_id = this.getAttribute('data-tab');
  var block_id = this.parentNode.getAttribute('data-tab-block');
  var panel_blocks = document.querySelectorAll('.pica-tab-panels[data-tab-block="' + block_id + '"] .pica-tab-panel');
  Array.prototype.forEach.call(panel_blocks, function(el, i){
     el.style.display = 'none'; 
  });
  var this_panel = document.querySelectorAll('.pica-tab-panels[data-tab-block="' + block_id + '"] .pica-tab-panel[data-tab="' + tab_id + '"]');
    Array.prototype.forEach.call(this_panel, function(el, i){
     el.style.display = 'block' 
  });
  var tab_controls = this.parentNode.querySelectorAll('li');
  Array.prototype.forEach.call(tab_controls, function(el, i){
    el.className = 'pica-tab-control';
  });
  this.className = 'pica-tab-control active';
}

var tab_controls = document.querySelectorAll('.pica-tab-control');
Array.prototype.forEach.call(tab_controls, function(el, i){
   el.addEventListener('click', pica_tabs_handler, false);
});
var defaults = document.querySelectorAll('li.pica-tab-control[data-tab-default="yes"]')
Array.prototype.forEach.call(defaults, function(el, i){
  el.click();
});

'''
