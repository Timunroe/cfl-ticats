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

  // manipulate content already on page

  // items to hide: 
  var ids_to_hide = ["div1702", "div1703", "div3404", "div3495"];
  var selectors_to_hide = ["#div1195 > div > section", "#div1195 > div > p", "#div1785 > div > p:nth-child(1)", "#div3472 > div > section", "#div3511 > div > p:nth-child(1)"];

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

    // insert logo
  var logo = document.createElement('img'); 
  logo.style.width = '50px'; 
  logo.style.cssFloat = 'left'; 
  logo.style.marginRight = '10px';
  logo.src = 'data:image/png;base64,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';
  parent = document.querySelector('#div1195 > div');
  parent.insertBefore(logo, parent.firstChild);
  // parent = document.querySelector('#div3472 > div');
  // parent.insertBefore(logo, parent.firstChild);


  // tabs handler

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
