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
