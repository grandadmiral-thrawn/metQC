---
layout: post
title: "Sample From Craigs Data"
date: 2015-08-02T14:23:04-07:00
---


We want to make sure the inputs from Craig's stange adjustments are A-OK. I was worried since this code was written quite some time ago. However, despite it being pretty ugly code, it appears to be "getting the job done".

Here's an example of the smoothing from the adjustment. Ugly or not, it works. Now to just dress it up into a nice interface. It makes me wonder, if I keep coding, what I will say 5 years from now!

<html>
<head>

<meta charset="utf-8" />
<title>Notebook</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    .clearfix{*zoom:1}.clearfix:before,.clearfix:after{display:table;content:"";line-height:0}
.clearfix:after{clear:both}
.hide-text{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}
.input-block-level{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}
article,aside,details,figcaption,figure,footer,header,hgroup,nav,section{display:block}
audio,canvas,video{display:inline-block;*display:inline;*zoom:1}
audio:not([controls]){display:none}
html{font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}
a:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
a:hover,a:active{outline:0}
sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}
sup{top:-0.5em}
sub{bottom:-0.25em}
img{max-width:100%;width:auto\9;height:auto;vertical-align:middle;border:0;-ms-interpolation-mode:bicubic}
#map_canvas img,.google-maps img{max-width:none}
button,input,select,textarea{margin:0;font-size:100%;vertical-align:middle}
button,input{*overflow:visible;line-height:normal}
button::-moz-focus-inner,input::-moz-focus-inner{padding:0;border:0}
button,html input[type="button"],input[type="reset"],input[type="submit"]{-webkit-appearance:button;cursor:pointer}
label,select,button,input[type="button"],input[type="reset"],input[type="submit"],input[type="radio"],input[type="checkbox"]{cursor:pointer}
input[type="search"]{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;-webkit-appearance:textfield}
input[type="search"]::-webkit-search-decoration,input[type="search"]::-webkit-search-cancel-button{-webkit-appearance:none}
textarea{overflow:auto;vertical-align:top}
@media print{*{text-shadow:none !important;color:#000 !important;background:transparent !important;box-shadow:none !important} a,a:visited{text-decoration:underline} a[href]:after{content:" (" attr(href) ")"} abbr[title]:after{content:" (" attr(title) ")"} .ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""} pre,blockquote{border:1px solid #999;page-break-inside:avoid} thead{display:table-header-group} tr,img{page-break-inside:avoid} img{max-width:100% !important} @page {margin:.5cm}p,h2,h3{orphans:3;widows:3} h2,h3{page-break-after:avoid}}body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;line-height:20px;color:#000;background-color:#fff}
a{color:#08c;text-decoration:none}
a:hover,a:focus{color:#005580;text-decoration:underline}
.img-rounded{border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.img-polaroid{padding:4px;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.1);-moz-box-shadow:0 1px 3px rgba(0,0,0,0.1);box-shadow:0 1px 3px rgba(0,0,0,0.1)}
.img-circle{border-radius:500px;-webkit-border-radius:500px;-moz-border-radius:500px;border-radius:500px}
.row{margin-left:-20px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0}
.row:after{clear:both}
[class*="span"]{float:left;min-height:1px;margin-left:20px}
.container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:940px}
.span12{width:940px}
.span11{width:860px}
.span10{width:780px}
.span9{width:700px}
.span8{width:620px}
.span7{width:540px}
.span6{width:460px}
.span5{width:380px}
.span4{width:300px}
.span3{width:220px}
.span2{width:140px}
.span1{width:60px}
.offset12{margin-left:980px}
.offset11{margin-left:900px}
.offset10{margin-left:820px}
.offset9{margin-left:740px}
.offset8{margin-left:660px}
.offset7{margin-left:580px}
.offset6{margin-left:500px}
.offset5{margin-left:420px}
.offset4{margin-left:340px}
.offset3{margin-left:260px}
.offset2{margin-left:180px}
.offset1{margin-left:100px}
.row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0}
.row-fluid:after{clear:both}
.row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.127659574468085%;*margin-left:2.074468085106383%}
.row-fluid [class*="span"]:first-child{margin-left:0}
.row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.127659574468085%}
.row-fluid .span12{width:100%;*width:99.94680851063829%}
.row-fluid .span11{width:91.48936170212765%;*width:91.43617021276594%}
.row-fluid .span10{width:82.97872340425532%;*width:82.92553191489361%}
.row-fluid .span9{width:74.46808510638297%;*width:74.41489361702126%}
.row-fluid .span8{width:65.95744680851064%;*width:65.90425531914893%}
.row-fluid .span7{width:57.44680851063829%;*width:57.39361702127659%}
.row-fluid .span6{width:48.93617021276595%;*width:48.88297872340425%}
.row-fluid .span5{width:40.42553191489362%;*width:40.37234042553192%}
.row-fluid .span4{width:31.914893617021278%;*width:31.861702127659576%}
.row-fluid .span3{width:23.404255319148934%;*width:23.351063829787233%}
.row-fluid .span2{width:14.893617021276595%;*width:14.840425531914894%}
.row-fluid .span1{width:6.382978723404255%;*width:6.329787234042553%}
.row-fluid .offset12{margin-left:104.25531914893617%;*margin-left:104.14893617021275%}
.row-fluid .offset12:first-child{margin-left:102.12765957446808%;*margin-left:102.02127659574467%}
.row-fluid .offset11{margin-left:95.74468085106382%;*margin-left:95.6382978723404%}
.row-fluid .offset11:first-child{margin-left:93.61702127659574%;*margin-left:93.51063829787232%}
.row-fluid .offset10{margin-left:87.23404255319149%;*margin-left:87.12765957446807%}
.row-fluid .offset10:first-child{margin-left:85.1063829787234%;*margin-left:84.99999999999999%}
.row-fluid .offset9{margin-left:78.72340425531914%;*margin-left:78.61702127659572%}
.row-fluid .offset9:first-child{margin-left:76.59574468085106%;*margin-left:76.48936170212764%}
.row-fluid .offset8{margin-left:70.2127659574468%;*margin-left:70.10638297872339%}
.row-fluid .offset8:first-child{margin-left:68.08510638297872%;*margin-left:67.9787234042553%}
.row-fluid .offset7{margin-left:61.70212765957446%;*margin-left:61.59574468085106%}
.row-fluid .offset7:first-child{margin-left:59.574468085106375%;*margin-left:59.46808510638297%}
.row-fluid .offset6{margin-left:53.191489361702125%;*margin-left:53.085106382978715%}
.row-fluid .offset6:first-child{margin-left:51.063829787234035%;*margin-left:50.95744680851063%}
.row-fluid .offset5{margin-left:44.68085106382979%;*margin-left:44.57446808510638%}
.row-fluid .offset5:first-child{margin-left:42.5531914893617%;*margin-left:42.4468085106383%}
.row-fluid .offset4{margin-left:36.170212765957444%;*margin-left:36.06382978723405%}
.row-fluid .offset4:first-child{margin-left:34.04255319148936%;*margin-left:33.93617021276596%}
.row-fluid .offset3{margin-left:27.659574468085104%;*margin-left:27.5531914893617%}
.row-fluid .offset3:first-child{margin-left:25.53191489361702%;*margin-left:25.425531914893618%}
.row-fluid .offset2{margin-left:19.148936170212764%;*margin-left:19.04255319148936%}
.row-fluid .offset2:first-child{margin-left:17.02127659574468%;*margin-left:16.914893617021278%}
.row-fluid .offset1{margin-left:10.638297872340425%;*margin-left:10.53191489361702%}
.row-fluid .offset1:first-child{margin-left:8.51063829787234%;*margin-left:8.404255319148938%}
[class*="span"].hide,.row-fluid [class*="span"].hide{display:none}
[class*="span"].pull-right,.row-fluid [class*="span"].pull-right{float:right}
.container{margin-right:auto;margin-left:auto;*zoom:1}.container:before,.container:after{display:table;content:"";line-height:0}
.container:after{clear:both}
.container-fluid{padding-right:20px;padding-left:20px;*zoom:1}.container-fluid:before,.container-fluid:after{display:table;content:"";line-height:0}
.container-fluid:after{clear:both}
p{margin:0 0 10px}
.lead{margin-bottom:20px;font-size:19.5px;font-weight:200;line-height:30px}
small{font-size:85%}
strong{font-weight:bold}
em{font-style:italic}
cite{font-style:normal}
.muted{color:#999}
a.muted:hover,a.muted:focus{color:#808080}
.text-warning{color:#c09853}
a.text-warning:hover,a.text-warning:focus{color:#a47e3c}
.text-error{color:#b94a48}
a.text-error:hover,a.text-error:focus{color:#953b39}
.text-info{color:#3a87ad}
a.text-info:hover,a.text-info:focus{color:#2d6987}
.text-success{color:#468847}
a.text-success:hover,a.text-success:focus{color:#356635}
.text-left{text-align:left}
.text-right{text-align:right}
.text-center{text-align:center}
h1,h2,h3,h4,h5,h6{margin:10px 0;font-family:inherit;font-weight:bold;line-height:20px;color:inherit;text-rendering:optimizelegibility}h1 small,h2 small,h3 small,h4 small,h5 small,h6 small{font-weight:normal;line-height:1;color:#999}
h1,h2,h3{line-height:40px}
h1{font-size:35.75px}
h2{font-size:29.25px}
h3{font-size:22.75px}
h4{font-size:16.25px}
h5{font-size:13px}
h6{font-size:11.049999999999999px}
h1 small{font-size:22.75px}
h2 small{font-size:16.25px}
h3 small{font-size:13px}
h4 small{font-size:13px}
.page-header{padding-bottom:9px;margin:20px 0 30px;border-bottom:1px solid #eee}
ul,ol{padding:0;margin:0 0 10px 25px}
ul ul,ul ol,ol ol,ol ul{margin-bottom:0}
li{line-height:20px}
ul.unstyled,ol.unstyled{margin-left:0;list-style:none}
ul.inline,ol.inline{margin-left:0;list-style:none}ul.inline>li,ol.inline>li{display:inline-block;*display:inline;*zoom:1;padding-left:5px;padding-right:5px}
dl{margin-bottom:20px}
dt,dd{line-height:20px}
dt{font-weight:bold}
dd{margin-left:10px}
.dl-horizontal{*zoom:1}.dl-horizontal:before,.dl-horizontal:after{display:table;content:"";line-height:0}
.dl-horizontal:after{clear:both}
.dl-horizontal dt{float:left;width:160px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dl-horizontal dd{margin-left:180px}
hr{margin:20px 0;border:0;border-top:1px solid #eee;border-bottom:1px solid #fff}
abbr[title],abbr[data-original-title]{cursor:help;border-bottom:1px dotted #999}
abbr.initialism{font-size:90%;text-transform:uppercase}
blockquote{padding:0 0 0 15px;margin:0 0 20px;border-left:5px solid #eee}blockquote p{margin-bottom:0;font-size:16.25px;font-weight:300;line-height:1.25}
blockquote small{display:block;line-height:20px;color:#999}blockquote small:before{content:'\2014 \00A0'}
blockquote.pull-right{float:right;padding-right:15px;padding-left:0;border-right:5px solid #eee;border-left:0}blockquote.pull-right p,blockquote.pull-right small{text-align:right}
blockquote.pull-right small:before{content:''}
blockquote.pull-right small:after{content:'\00A0 \2014'}
q:before,q:after,blockquote:before,blockquote:after{content:""}
address{display:block;margin-bottom:20px;font-style:normal;line-height:20px}
code,pre{padding:0 3px 2px;font-family:monospace;font-size:11px;color:#333;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
code{padding:2px 4px;color:#d14;background-color:#f7f7f9;border:1px solid #e1e1e8;white-space:nowrap}
pre{display:block;padding:9.5px;margin:0 0 10px;font-size:12px;line-height:20px;word-break:break-all;word-wrap:break-word;white-space:pre;white-space:pre-wrap;background-color:#f5f5f5;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.15);border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}pre.prettyprint{margin-bottom:20px}
pre code{padding:0;color:inherit;white-space:pre;white-space:pre-wrap;background-color:transparent;border:0}
.pre-scrollable{max-height:340px;overflow-y:scroll}
form{margin:0 0 20px}
fieldset{padding:0;margin:0;border:0}
legend{display:block;width:100%;padding:0;margin-bottom:20px;font-size:19.5px;line-height:40px;color:#333;border:0;border-bottom:1px solid #e5e5e5}legend small{font-size:15px;color:#999}
label,input,button,select,textarea{font-size:13px;font-weight:normal;line-height:20px}
input,button,select,textarea{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
label{display:block;margin-bottom:5px}
select,textarea,input[type="text"],input[type="password"],input[type="datetime"],input[type="datetime-local"],input[type="date"],input[type="month"],input[type="time"],input[type="week"],input[type="number"],input[type="email"],input[type="url"],input[type="search"],input[type="tel"],input[type="color"],.uneditable-input{display:inline-block;height:20px;padding:4px 6px;margin-bottom:10px;font-size:13px;line-height:20px;color:#555;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;vertical-align:middle}
input,textarea,.uneditable-input{width:206px}
textarea{height:auto}
textarea,input[type="text"],input[type="password"],input[type="datetime"],input[type="datetime-local"],input[type="date"],input[type="month"],input[type="time"],input[type="week"],input[type="number"],input[type="email"],input[type="url"],input[type="search"],input[type="tel"],input[type="color"],.uneditable-input{background-color:#fff;border:1px solid #ccc;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-webkit-transition:border linear .2s, box-shadow linear .2s;-moz-transition:border linear .2s, box-shadow linear .2s;-o-transition:border linear .2s, box-shadow linear .2s;transition:border linear .2s, box-shadow linear .2s}textarea:focus,input[type="text"]:focus,input[type="password"]:focus,input[type="datetime"]:focus,input[type="datetime-local"]:focus,input[type="date"]:focus,input[type="month"]:focus,input[type="time"]:focus,input[type="week"]:focus,input[type="number"]:focus,input[type="email"]:focus,input[type="url"]:focus,input[type="search"]:focus,input[type="tel"]:focus,input[type="color"]:focus,.uneditable-input:focus{border-color:rgba(82,168,236,0.8);outline:0;outline:thin dotted \9;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6)}
input[type="radio"],input[type="checkbox"]{margin:4px 0 0;*margin-top:0;margin-top:1px \9;line-height:normal}
input[type="file"],input[type="image"],input[type="submit"],input[type="reset"],input[type="button"],input[type="radio"],input[type="checkbox"]{width:auto}
select,input[type="file"]{height:30px;*margin-top:4px;line-height:30px}
select{width:220px;border:1px solid #ccc;background-color:#fff}
select[multiple],select[size]{height:auto}
select:focus,input[type="file"]:focus,input[type="radio"]:focus,input[type="checkbox"]:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
.uneditable-input,.uneditable-textarea{color:#999;background-color:#fcfcfc;border-color:#ccc;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);cursor:not-allowed}
.uneditable-input{overflow:hidden;white-space:nowrap}
.uneditable-textarea{width:auto;height:auto}
input:-moz-placeholder,textarea:-moz-placeholder{color:#999}
input:-ms-input-placeholder,textarea:-ms-input-placeholder{color:#999}
input::-webkit-input-placeholder,textarea::-webkit-input-placeholder{color:#999}
.radio,.checkbox{min-height:20px;padding-left:20px}
.radio input[type="radio"],.checkbox input[type="checkbox"]{float:left;margin-left:-20px}
.controls>.radio:first-child,.controls>.checkbox:first-child{padding-top:5px}
.radio.inline,.checkbox.inline{display:inline-block;padding-top:5px;margin-bottom:0;vertical-align:middle}
.radio.inline+.radio.inline,.checkbox.inline+.checkbox.inline{margin-left:10px}
.input-mini{width:60px}
.input-small{width:90px}
.input-medium{width:150px}
.input-large{width:210px}
.input-xlarge{width:270px}
.input-xxlarge{width:530px}
input[class*="span"],select[class*="span"],textarea[class*="span"],.uneditable-input[class*="span"],.row-fluid input[class*="span"],.row-fluid select[class*="span"],.row-fluid textarea[class*="span"],.row-fluid .uneditable-input[class*="span"]{float:none;margin-left:0}
.input-append input[class*="span"],.input-append .uneditable-input[class*="span"],.input-prepend input[class*="span"],.input-prepend .uneditable-input[class*="span"],.row-fluid input[class*="span"],.row-fluid select[class*="span"],.row-fluid textarea[class*="span"],.row-fluid .uneditable-input[class*="span"],.row-fluid .input-prepend [class*="span"],.row-fluid .input-append [class*="span"]{display:inline-block}
input,textarea,.uneditable-input{margin-left:0}
.controls-row [class*="span"]+[class*="span"]{margin-left:20px}
input.span12,textarea.span12,.uneditable-input.span12{width:926px}
input.span11,textarea.span11,.uneditable-input.span11{width:846px}
input.span10,textarea.span10,.uneditable-input.span10{width:766px}
input.span9,textarea.span9,.uneditable-input.span9{width:686px}
input.span8,textarea.span8,.uneditable-input.span8{width:606px}
input.span7,textarea.span7,.uneditable-input.span7{width:526px}
input.span6,textarea.span6,.uneditable-input.span6{width:446px}
input.span5,textarea.span5,.uneditable-input.span5{width:366px}
input.span4,textarea.span4,.uneditable-input.span4{width:286px}
input.span3,textarea.span3,.uneditable-input.span3{width:206px}
input.span2,textarea.span2,.uneditable-input.span2{width:126px}
input.span1,textarea.span1,.uneditable-input.span1{width:46px}
.controls-row{*zoom:1}.controls-row:before,.controls-row:after{display:table;content:"";line-height:0}
.controls-row:after{clear:both}
.controls-row [class*="span"],.row-fluid .controls-row [class*="span"]{float:left}
.controls-row .checkbox[class*="span"],.controls-row .radio[class*="span"]{padding-top:5px}
input[disabled],select[disabled],textarea[disabled],input[readonly],select[readonly],textarea[readonly]{cursor:not-allowed;background-color:#eee}
input[type="radio"][disabled],input[type="checkbox"][disabled],input[type="radio"][readonly],input[type="checkbox"][readonly]{background-color:transparent}
.control-group.warning .control-label,.control-group.warning .help-block,.control-group.warning .help-inline{color:#c09853}
.control-group.warning .checkbox,.control-group.warning .radio,.control-group.warning input,.control-group.warning select,.control-group.warning textarea{color:#c09853}
.control-group.warning input,.control-group.warning select,.control-group.warning textarea{border-color:#c09853;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.warning input:focus,.control-group.warning select:focus,.control-group.warning textarea:focus{border-color:#a47e3c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e}
.control-group.warning .input-prepend .add-on,.control-group.warning .input-append .add-on{color:#c09853;background-color:#fcf8e3;border-color:#c09853}
.control-group.error .control-label,.control-group.error .help-block,.control-group.error .help-inline{color:#b94a48}
.control-group.error .checkbox,.control-group.error .radio,.control-group.error input,.control-group.error select,.control-group.error textarea{color:#b94a48}
.control-group.error input,.control-group.error select,.control-group.error textarea{border-color:#b94a48;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.error input:focus,.control-group.error select:focus,.control-group.error textarea:focus{border-color:#953b39;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392}
.control-group.error .input-prepend .add-on,.control-group.error .input-append .add-on{color:#b94a48;background-color:#f2dede;border-color:#b94a48}
.control-group.success .control-label,.control-group.success .help-block,.control-group.success .help-inline{color:#468847}
.control-group.success .checkbox,.control-group.success .radio,.control-group.success input,.control-group.success select,.control-group.success textarea{color:#468847}
.control-group.success input,.control-group.success select,.control-group.success textarea{border-color:#468847;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.success input:focus,.control-group.success select:focus,.control-group.success textarea:focus{border-color:#356635;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b}
.control-group.success .input-prepend .add-on,.control-group.success .input-append .add-on{color:#468847;background-color:#dff0d8;border-color:#468847}
.control-group.info .control-label,.control-group.info .help-block,.control-group.info .help-inline{color:#3a87ad}
.control-group.info .checkbox,.control-group.info .radio,.control-group.info input,.control-group.info select,.control-group.info textarea{color:#3a87ad}
.control-group.info input,.control-group.info select,.control-group.info textarea{border-color:#3a87ad;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.info input:focus,.control-group.info select:focus,.control-group.info textarea:focus{border-color:#2d6987;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3}
.control-group.info .input-prepend .add-on,.control-group.info .input-append .add-on{color:#3a87ad;background-color:#d9edf7;border-color:#3a87ad}
input:focus:invalid,textarea:focus:invalid,select:focus:invalid{color:#b94a48;border-color:#ee5f5b}input:focus:invalid:focus,textarea:focus:invalid:focus,select:focus:invalid:focus{border-color:#e9322d;-webkit-box-shadow:0 0 6px #f8b9b7;-moz-box-shadow:0 0 6px #f8b9b7;box-shadow:0 0 6px #f8b9b7}
.form-actions{padding:19px 20px 20px;margin-top:20px;margin-bottom:20px;background-color:#f5f5f5;border-top:1px solid #e5e5e5;*zoom:1}.form-actions:before,.form-actions:after{display:table;content:"";line-height:0}
.form-actions:after{clear:both}
.help-block,.help-inline{color:#262626}
.help-block{display:block;margin-bottom:10px}
.help-inline{display:inline-block;*display:inline;*zoom:1;vertical-align:middle;padding-left:5px}
.input-append,.input-prepend{display:inline-block;margin-bottom:10px;vertical-align:middle;font-size:0;white-space:nowrap}.input-append input,.input-prepend input,.input-append select,.input-prepend select,.input-append .uneditable-input,.input-prepend .uneditable-input,.input-append .dropdown-menu,.input-prepend .dropdown-menu,.input-append .popover,.input-prepend .popover{font-size:13px}
.input-append input,.input-prepend input,.input-append select,.input-prepend select,.input-append .uneditable-input,.input-prepend .uneditable-input{position:relative;margin-bottom:0;*margin-left:0;vertical-align:top;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}.input-append input:focus,.input-prepend input:focus,.input-append select:focus,.input-prepend select:focus,.input-append .uneditable-input:focus,.input-prepend .uneditable-input:focus{z-index:2}
.input-append .add-on,.input-prepend .add-on{display:inline-block;width:auto;height:20px;min-width:16px;padding:4px 5px;font-size:13px;font-weight:normal;line-height:20px;text-align:center;text-shadow:0 1px 0 #fff;background-color:#eee;border:1px solid #ccc}
.input-append .add-on,.input-prepend .add-on,.input-append .btn,.input-prepend .btn,.input-append .btn-group>.dropdown-toggle,.input-prepend .btn-group>.dropdown-toggle{vertical-align:top;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.input-append .active,.input-prepend .active{background-color:#a9dba9;border-color:#46a546}
.input-prepend .add-on,.input-prepend .btn{margin-right:-1px}
.input-prepend .add-on:first-child,.input-prepend .btn:first-child{border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.input-append input,.input-append select,.input-append .uneditable-input{border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}.input-append input+.btn-group .btn:last-child,.input-append select+.btn-group .btn:last-child,.input-append .uneditable-input+.btn-group .btn:last-child{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-append .add-on,.input-append .btn,.input-append .btn-group{margin-left:-1px}
.input-append .add-on:last-child,.input-append .btn:last-child,.input-append .btn-group:last-child>.dropdown-toggle{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append input,.input-prepend.input-append select,.input-prepend.input-append .uneditable-input{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}.input-prepend.input-append input+.btn-group .btn,.input-prepend.input-append select+.btn-group .btn,.input-prepend.input-append .uneditable-input+.btn-group .btn{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append .add-on:first-child,.input-prepend.input-append .btn:first-child{margin-right:-1px;border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.input-prepend.input-append .add-on:last-child,.input-prepend.input-append .btn:last-child{margin-left:-1px;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append .btn-group:first-child{margin-left:0}
input.search-query{padding-right:14px;padding-right:4px \9;padding-left:14px;padding-left:4px \9;margin-bottom:0;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.form-search .input-append .search-query,.form-search .input-prepend .search-query{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.form-search .input-append .search-query{border-radius:14px 0 0 14px;-webkit-border-radius:14px 0 0 14px;-moz-border-radius:14px 0 0 14px;border-radius:14px 0 0 14px}
.form-search .input-append .btn{border-radius:0 14px 14px 0;-webkit-border-radius:0 14px 14px 0;-moz-border-radius:0 14px 14px 0;border-radius:0 14px 14px 0}
.form-search .input-prepend .search-query{border-radius:0 14px 14px 0;-webkit-border-radius:0 14px 14px 0;-moz-border-radius:0 14px 14px 0;border-radius:0 14px 14px 0}
.form-search .input-prepend .btn{border-radius:14px 0 0 14px;-webkit-border-radius:14px 0 0 14px;-moz-border-radius:14px 0 0 14px;border-radius:14px 0 0 14px}
.form-search input,.form-inline input,.form-horizontal input,.form-search textarea,.form-inline textarea,.form-horizontal textarea,.form-search select,.form-inline select,.form-horizontal select,.form-search .help-inline,.form-inline .help-inline,.form-horizontal .help-inline,.form-search .uneditable-input,.form-inline .uneditable-input,.form-horizontal .uneditable-input,.form-search .input-prepend,.form-inline .input-prepend,.form-horizontal .input-prepend,.form-search .input-append,.form-inline .input-append,.form-horizontal .input-append{display:inline-block;*display:inline;*zoom:1;margin-bottom:0;vertical-align:middle}
.form-search .hide,.form-inline .hide,.form-horizontal .hide{display:none}
.form-search label,.form-inline label,.form-search .btn-group,.form-inline .btn-group{display:inline-block}
.form-search .input-append,.form-inline .input-append,.form-search .input-prepend,.form-inline .input-prepend{margin-bottom:0}
.form-search .radio,.form-search .checkbox,.form-inline .radio,.form-inline .checkbox{padding-left:0;margin-bottom:0;vertical-align:middle}
.form-search .radio input[type="radio"],.form-search .checkbox input[type="checkbox"],.form-inline .radio input[type="radio"],.form-inline .checkbox input[type="checkbox"]{float:left;margin-right:3px;margin-left:0}
.control-group{margin-bottom:10px}
legend+.control-group{margin-top:20px;-webkit-margin-top-collapse:separate}
.form-horizontal .control-group{margin-bottom:20px;*zoom:1}.form-horizontal .control-group:before,.form-horizontal .control-group:after{display:table;content:"";line-height:0}
.form-horizontal .control-group:after{clear:both}
.form-horizontal .control-label{float:left;width:160px;padding-top:5px;text-align:right}
.form-horizontal .controls{*display:inline-block;*padding-left:20px;margin-left:180px;*margin-left:0}.form-horizontal .controls:first-child{*padding-left:180px}
.form-horizontal .help-block{margin-bottom:0}
.form-horizontal input+.help-block,.form-horizontal select+.help-block,.form-horizontal textarea+.help-block,.form-horizontal .uneditable-input+.help-block,.form-horizontal .input-prepend+.help-block,.form-horizontal .input-append+.help-block{margin-top:10px}
.form-horizontal .form-actions{padding-left:180px}
table{max-width:100%;background-color:transparent;border-collapse:collapse;border-spacing:0}
.table{width:100%;margin-bottom:20px}.table th,.table td{padding:8px;line-height:20px;text-align:left;vertical-align:top;border-top:1px solid #ddd}
.table th{font-weight:bold}
.table thead th{vertical-align:bottom}
.table caption+thead tr:first-child th,.table caption+thead tr:first-child td,.table colgroup+thead tr:first-child th,.table colgroup+thead tr:first-child td,.table thead:first-child tr:first-child th,.table thead:first-child tr:first-child td{border-top:0}
.table tbody+tbody{border-top:2px solid #ddd}
.table .table{background-color:#fff}
.table-condensed th,.table-condensed td{padding:4px 5px}
.table-bordered{border:1px solid #ddd;border-collapse:separate;*border-collapse:collapse;border-left:0;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}.table-bordered th,.table-bordered td{border-left:1px solid #ddd}
.table-bordered caption+thead tr:first-child th,.table-bordered caption+tbody tr:first-child th,.table-bordered caption+tbody tr:first-child td,.table-bordered colgroup+thead tr:first-child th,.table-bordered colgroup+tbody tr:first-child th,.table-bordered colgroup+tbody tr:first-child td,.table-bordered thead:first-child tr:first-child th,.table-bordered tbody:first-child tr:first-child th,.table-bordered tbody:first-child tr:first-child td{border-top:0}
.table-bordered thead:first-child tr:first-child>th:first-child,.table-bordered tbody:first-child tr:first-child>td:first-child,.table-bordered tbody:first-child tr:first-child>th:first-child{-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.table-bordered thead:first-child tr:first-child>th:last-child,.table-bordered tbody:first-child tr:first-child>td:last-child,.table-bordered tbody:first-child tr:first-child>th:last-child{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px}
.table-bordered thead:last-child tr:last-child>th:first-child,.table-bordered tbody:last-child tr:last-child>td:first-child,.table-bordered tbody:last-child tr:last-child>th:first-child,.table-bordered tfoot:last-child tr:last-child>td:first-child,.table-bordered tfoot:last-child tr:last-child>th:first-child{-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.table-bordered thead:last-child tr:last-child>th:last-child,.table-bordered tbody:last-child tr:last-child>td:last-child,.table-bordered tbody:last-child tr:last-child>th:last-child,.table-bordered tfoot:last-child tr:last-child>td:last-child,.table-bordered tfoot:last-child tr:last-child>th:last-child{-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.table-bordered tfoot+tbody:last-child tr:last-child td:first-child{-webkit-border-bottom-left-radius:0;-moz-border-radius-bottomleft:0;border-bottom-left-radius:0}
.table-bordered tfoot+tbody:last-child tr:last-child td:last-child{-webkit-border-bottom-right-radius:0;-moz-border-radius-bottomright:0;border-bottom-right-radius:0}
.table-bordered caption+thead tr:first-child th:first-child,.table-bordered caption+tbody tr:first-child td:first-child,.table-bordered colgroup+thead tr:first-child th:first-child,.table-bordered colgroup+tbody tr:first-child td:first-child{-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.table-bordered caption+thead tr:first-child th:last-child,.table-bordered caption+tbody tr:first-child td:last-child,.table-bordered colgroup+thead tr:first-child th:last-child,.table-bordered colgroup+tbody tr:first-child td:last-child{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px}
.table-striped tbody>tr:nth-child(odd)>td,.table-striped tbody>tr:nth-child(odd)>th{background-color:#f9f9f9}
.table-hover tbody tr:hover>td,.table-hover tbody tr:hover>th{background-color:#f5f5f5}
table td[class*="span"],table th[class*="span"],.row-fluid table td[class*="span"],.row-fluid table th[class*="span"]{display:table-cell;float:none;margin-left:0}
.table td.span1,.table th.span1{float:none;width:44px;margin-left:0}
.table td.span2,.table th.span2{float:none;width:124px;margin-left:0}
.table td.span3,.table th.span3{float:none;width:204px;margin-left:0}
.table td.span4,.table th.span4{float:none;width:284px;margin-left:0}
.table td.span5,.table th.span5{float:none;width:364px;margin-left:0}
.table td.span6,.table th.span6{float:none;width:444px;margin-left:0}
.table td.span7,.table th.span7{float:none;width:524px;margin-left:0}
.table td.span8,.table th.span8{float:none;width:604px;margin-left:0}
.table td.span9,.table th.span9{float:none;width:684px;margin-left:0}
.table td.span10,.table th.span10{float:none;width:764px;margin-left:0}
.table td.span11,.table th.span11{float:none;width:844px;margin-left:0}
.table td.span12,.table th.span12{float:none;width:924px;margin-left:0}
.table tbody tr.success>td{background-color:#dff0d8}
.table tbody tr.error>td{background-color:#f2dede}
.table tbody tr.warning>td{background-color:#fcf8e3}
.table tbody tr.info>td{background-color:#d9edf7}
.table-hover tbody tr.success:hover>td{background-color:#d0e9c6}
.table-hover tbody tr.error:hover>td{background-color:#ebcccc}
.table-hover tbody tr.warning:hover>td{background-color:#faf2cc}
.table-hover tbody tr.info:hover>td{background-color:#c4e3f3}
[class^="icon-"],[class*=" icon-"]{display:inline-block;width:14px;height:14px;*margin-right:.3em;line-height:14px;vertical-align:text-top;background-image:url("../img/glyphicons-halflings.png");background-position:14px 14px;background-repeat:no-repeat;margin-top:1px}
.icon-white,.nav-pills>.active>a>[class^="icon-"],.nav-pills>.active>a>[class*=" icon-"],.nav-list>.active>a>[class^="icon-"],.nav-list>.active>a>[class*=" icon-"],.navbar-inverse .nav>.active>a>[class^="icon-"],.navbar-inverse .nav>.active>a>[class*=" icon-"],.dropdown-menu>li>a:hover>[class^="icon-"],.dropdown-menu>li>a:focus>[class^="icon-"],.dropdown-menu>li>a:hover>[class*=" icon-"],.dropdown-menu>li>a:focus>[class*=" icon-"],.dropdown-menu>.active>a>[class^="icon-"],.dropdown-menu>.active>a>[class*=" icon-"],.dropdown-submenu:hover>a>[class^="icon-"],.dropdown-submenu:focus>a>[class^="icon-"],.dropdown-submenu:hover>a>[class*=" icon-"],.dropdown-submenu:focus>a>[class*=" icon-"]{background-image:url("../img/glyphicons-halflings-white.png")}
.icon-glass{background-position:0 0}
.icon-music{background-position:-24px 0}
.icon-search{background-position:-48px 0}
.icon-envelope{background-position:-72px 0}
.icon-heart{background-position:-96px 0}
.icon-star{background-position:-120px 0}
.icon-star-empty{background-position:-144px 0}
.icon-user{background-position:-168px 0}
.icon-film{background-position:-192px 0}
.icon-th-large{background-position:-216px 0}
.icon-th{background-position:-240px 0}
.icon-th-list{background-position:-264px 0}
.icon-ok{background-position:-288px 0}
.icon-remove{background-position:-312px 0}
.icon-zoom-in{background-position:-336px 0}
.icon-zoom-out{background-position:-360px 0}
.icon-off{background-position:-384px 0}
.icon-signal{background-position:-408px 0}
.icon-cog{background-position:-432px 0}
.icon-trash{background-position:-456px 0}
.icon-home{background-position:0 -24px}
.icon-file{background-position:-24px -24px}
.icon-time{background-position:-48px -24px}
.icon-road{background-position:-72px -24px}
.icon-download-alt{background-position:-96px -24px}
.icon-download{background-position:-120px -24px}
.icon-upload{background-position:-144px -24px}
.icon-inbox{background-position:-168px -24px}
.icon-play-circle{background-position:-192px -24px}
.icon-repeat{background-position:-216px -24px}
.icon-refresh{background-position:-240px -24px}
.icon-list-alt{background-position:-264px -24px}
.icon-lock{background-position:-287px -24px}
.icon-flag{background-position:-312px -24px}
.icon-headphones{background-position:-336px -24px}
.icon-volume-off{background-position:-360px -24px}
.icon-volume-down{background-position:-384px -24px}
.icon-volume-up{background-position:-408px -24px}
.icon-qrcode{background-position:-432px -24px}
.icon-barcode{background-position:-456px -24px}
.icon-tag{background-position:0 -48px}
.icon-tags{background-position:-25px -48px}
.icon-book{background-position:-48px -48px}
.icon-bookmark{background-position:-72px -48px}
.icon-print{background-position:-96px -48px}
.icon-camera{background-position:-120px -48px}
.icon-font{background-position:-144px -48px}
.icon-bold{background-position:-167px -48px}
.icon-italic{background-position:-192px -48px}
.icon-text-height{background-position:-216px -48px}
.icon-text-width{background-position:-240px -48px}
.icon-align-left{background-position:-264px -48px}
.icon-align-center{background-position:-288px -48px}
.icon-align-right{background-position:-312px -48px}
.icon-align-justify{background-position:-336px -48px}
.icon-list{background-position:-360px -48px}
.icon-indent-left{background-position:-384px -48px}
.icon-indent-right{background-position:-408px -48px}
.icon-facetime-video{background-position:-432px -48px}
.icon-picture{background-position:-456px -48px}
.icon-pencil{background-position:0 -72px}
.icon-map-marker{background-position:-24px -72px}
.icon-adjust{background-position:-48px -72px}
.icon-tint{background-position:-72px -72px}
.icon-edit{background-position:-96px -72px}
.icon-share{background-position:-120px -72px}
.icon-check{background-position:-144px -72px}
.icon-move{background-position:-168px -72px}
.icon-step-backward{background-position:-192px -72px}
.icon-fast-backward{background-position:-216px -72px}
.icon-backward{background-position:-240px -72px}
.icon-play{background-position:-264px -72px}
.icon-pause{background-position:-288px -72px}
.icon-stop{background-position:-312px -72px}
.icon-forward{background-position:-336px -72px}
.icon-fast-forward{background-position:-360px -72px}
.icon-step-forward{background-position:-384px -72px}
.icon-eject{background-position:-408px -72px}
.icon-chevron-left{background-position:-432px -72px}
.icon-chevron-right{background-position:-456px -72px}
.icon-plus-sign{background-position:0 -96px}
.icon-minus-sign{background-position:-24px -96px}
.icon-remove-sign{background-position:-48px -96px}
.icon-ok-sign{background-position:-72px -96px}
.icon-question-sign{background-position:-96px -96px}
.icon-info-sign{background-position:-120px -96px}
.icon-screenshot{background-position:-144px -96px}
.icon-remove-circle{background-position:-168px -96px}
.icon-ok-circle{background-position:-192px -96px}
.icon-ban-circle{background-position:-216px -96px}
.icon-arrow-left{background-position:-240px -96px}
.icon-arrow-right{background-position:-264px -96px}
.icon-arrow-up{background-position:-289px -96px}
.icon-arrow-down{background-position:-312px -96px}
.icon-share-alt{background-position:-336px -96px}
.icon-resize-full{background-position:-360px -96px}
.icon-resize-small{background-position:-384px -96px}
.icon-plus{background-position:-408px -96px}
.icon-minus{background-position:-433px -96px}
.icon-asterisk{background-position:-456px -96px}
.icon-exclamation-sign{background-position:0 -120px}
.icon-gift{background-position:-24px -120px}
.icon-leaf{background-position:-48px -120px}
.icon-fire{background-position:-72px -120px}
.icon-eye-open{background-position:-96px -120px}
.icon-eye-close{background-position:-120px -120px}
.icon-warning-sign{background-position:-144px -120px}
.icon-plane{background-position:-168px -120px}
.icon-calendar{background-position:-192px -120px}
.icon-random{background-position:-216px -120px;width:16px}
.icon-comment{background-position:-240px -120px}
.icon-magnet{background-position:-264px -120px}
.icon-chevron-up{background-position:-288px -120px}
.icon-chevron-down{background-position:-313px -119px}
.icon-retweet{background-position:-336px -120px}
.icon-shopping-cart{background-position:-360px -120px}
.icon-folder-close{background-position:-384px -120px;width:16px}
.icon-folder-open{background-position:-408px -120px;width:16px}
.icon-resize-vertical{background-position:-432px -119px}
.icon-resize-horizontal{background-position:-456px -118px}
.icon-hdd{background-position:0 -144px}
.icon-bullhorn{background-position:-24px -144px}
.icon-bell{background-position:-48px -144px}
.icon-certificate{background-position:-72px -144px}
.icon-thumbs-up{background-position:-96px -144px}
.icon-thumbs-down{background-position:-120px -144px}
.icon-hand-right{background-position:-144px -144px}
.icon-hand-left{background-position:-168px -144px}
.icon-hand-up{background-position:-192px -144px}
.icon-hand-down{background-position:-216px -144px}
.icon-circle-arrow-right{background-position:-240px -144px}
.icon-circle-arrow-left{background-position:-264px -144px}
.icon-circle-arrow-up{background-position:-288px -144px}
.icon-circle-arrow-down{background-position:-312px -144px}
.icon-globe{background-position:-336px -144px}
.icon-wrench{background-position:-360px -144px}
.icon-tasks{background-position:-384px -144px}
.icon-filter{background-position:-408px -144px}
.icon-briefcase{background-position:-432px -144px}
.icon-fullscreen{background-position:-456px -144px}
.dropup,.dropdown{position:relative}
.dropdown-toggle{*margin-bottom:-3px}
.dropdown-toggle:active,.open .dropdown-toggle{outline:0}
.caret{display:inline-block;width:0;height:0;vertical-align:top;border-top:4px solid #000;border-right:4px solid transparent;border-left:4px solid transparent;content:""}
.dropdown .caret{margin-top:8px;margin-left:2px}
.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:160px;padding:5px 0;margin:2px 0 0;list-style:none;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);*border-right-width:2px;*border-bottom-width:2px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,0.2);-moz-box-shadow:0 5px 10px rgba(0,0,0,0.2);box-shadow:0 5px 10px rgba(0,0,0,0.2);-webkit-background-clip:padding-box;-moz-background-clip:padding;background-clip:padding-box}.dropdown-menu.pull-right{right:0;left:auto}
.dropdown-menu .divider{*width:100%;height:1px;margin:9px 1px;*margin:-5px 0 5px;overflow:hidden;background-color:#e5e5e5;border-bottom:1px solid #fff}
.dropdown-menu>li>a{display:block;padding:3px 20px;clear:both;font-weight:normal;line-height:20px;color:#333;white-space:nowrap}
.dropdown-menu>li>a:hover,.dropdown-menu>li>a:focus,.dropdown-submenu:hover>a,.dropdown-submenu:focus>a{text-decoration:none;color:#fff;background-color:#0081c2;background-image:-moz-linear-gradient(top, #08c, #0077b3);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#0077b3));background-image:-webkit-linear-gradient(top, #08c, #0077b3);background-image:-o-linear-gradient(top, #08c, #0077b3);background-image:linear-gradient(to bottom, #08c, #0077b3);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0)}
.dropdown-menu>.active>a,.dropdown-menu>.active>a:hover,.dropdown-menu>.active>a:focus{color:#fff;text-decoration:none;outline:0;background-color:#0081c2;background-image:-moz-linear-gradient(top, #08c, #0077b3);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#0077b3));background-image:-webkit-linear-gradient(top, #08c, #0077b3);background-image:-o-linear-gradient(top, #08c, #0077b3);background-image:linear-gradient(to bottom, #08c, #0077b3);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0)}
.dropdown-menu>.disabled>a,.dropdown-menu>.disabled>a:hover,.dropdown-menu>.disabled>a:focus{color:#999}
.dropdown-menu>.disabled>a:hover,.dropdown-menu>.disabled>a:focus{text-decoration:none;background-color:transparent;background-image:none;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);cursor:default}
.open{*z-index:1000}.open>.dropdown-menu{display:block}
.dropdown-backdrop{position:fixed;left:0;right:0;bottom:0;top:0;z-index:990}
.pull-right>.dropdown-menu{right:0;left:auto}
.dropup .caret,.navbar-fixed-bottom .dropdown .caret{border-top:0;border-bottom:4px solid #000;content:""}
.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:1px}
.dropdown-submenu{position:relative}
.dropdown-submenu>.dropdown-menu{top:0;left:100%;margin-top:-6px;margin-left:-1px;border-radius:0 6px 6px 6px;-webkit-border-radius:0 6px 6px 6px;-moz-border-radius:0 6px 6px 6px;border-radius:0 6px 6px 6px}
.dropdown-submenu:hover>.dropdown-menu{display:block}
.dropup .dropdown-submenu>.dropdown-menu{top:auto;bottom:0;margin-top:0;margin-bottom:-2px;border-radius:5px 5px 5px 0;-webkit-border-radius:5px 5px 5px 0;-moz-border-radius:5px 5px 5px 0;border-radius:5px 5px 5px 0}
.dropdown-submenu>a:after{display:block;content:" ";float:right;width:0;height:0;border-color:transparent;border-style:solid;border-width:5px 0 5px 5px;border-left-color:#ccc;margin-top:5px;margin-right:-10px}
.dropdown-submenu:hover>a:after{border-left-color:#fff}
.dropdown-submenu.pull-left{float:none}.dropdown-submenu.pull-left>.dropdown-menu{left:-100%;margin-left:10px;border-radius:6px 0 6px 6px;-webkit-border-radius:6px 0 6px 6px;-moz-border-radius:6px 0 6px 6px;border-radius:6px 0 6px 6px}
.dropdown .dropdown-menu .nav-header{padding-left:20px;padding-right:20px}
.typeahead{z-index:1051;margin-top:2px;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.well{min-height:20px;padding:19px;margin-bottom:20px;background-color:#f5f5f5;border:1px solid #e3e3e3;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.05);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.05);box-shadow:inset 0 1px 1px rgba(0,0,0,0.05)}.well blockquote{border-color:#ddd;border-color:rgba(0,0,0,0.15)}
.well-large{padding:24px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.well-small{padding:9px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.fade{opacity:0;-webkit-transition:opacity .15s linear;-moz-transition:opacity .15s linear;-o-transition:opacity .15s linear;transition:opacity .15s linear}.fade.in{opacity:1}
.collapse{position:relative;height:0;overflow:hidden;-webkit-transition:height .35s ease;-moz-transition:height .35s ease;-o-transition:height .35s ease;transition:height .35s ease}.collapse.in{height:auto}
.close{float:right;font-size:20px;font-weight:bold;line-height:20px;color:#000;text-shadow:0 1px 0 #fff;opacity:.2;filter:alpha(opacity=20)}.close:hover,.close:focus{color:#000;text-decoration:none;cursor:pointer;opacity:.4;filter:alpha(opacity=40)}
button.close{padding:0;cursor:pointer;background:transparent;border:0;-webkit-appearance:none}
.btn{display:inline-block;*display:inline;*zoom:1;padding:4px 12px;margin-bottom:0;font-size:13px;line-height:20px;text-align:center;vertical-align:middle;cursor:pointer;color:#333;text-shadow:0 1px 1px rgba(255,255,255,0.75);background-color:#f5f5f5;background-image:-moz-linear-gradient(top, #fff, #e6e6e6);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fff), to(#e6e6e6));background-image:-webkit-linear-gradient(top, #fff, #e6e6e6);background-image:-o-linear-gradient(top, #fff, #e6e6e6);background-image:linear-gradient(to bottom, #fff, #e6e6e6);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe6e6e6', GradientType=0);border-color:#e6e6e6 #e6e6e6 #bfbfbf;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#e6e6e6;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);border:1px solid #ccc;*border:0;border-bottom-color:#b3b3b3;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;*margin-left:.3em;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05)}.btn:hover,.btn:focus,.btn:active,.btn.active,.btn.disabled,.btn[disabled]{color:#333;background-color:#e6e6e6;*background-color:#d9d9d9}
.btn:active,.btn.active{background-color:#ccc \9}
.btn:first-child{*margin-left:0}
.btn:hover,.btn:focus{color:#333;text-decoration:none;background-position:0 -15px;-webkit-transition:background-position .1s linear;-moz-transition:background-position .1s linear;-o-transition:background-position .1s linear;transition:background-position .1s linear}
.btn:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
.btn.active,.btn:active{background-image:none;outline:0;-webkit-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05)}
.btn.disabled,.btn[disabled]{cursor:default;background-image:none;opacity:.65;filter:alpha(opacity=65);-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}
.btn-large{padding:11px 19px;font-size:16.25px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.btn-large [class^="icon-"],.btn-large [class*=" icon-"]{margin-top:4px}
.btn-small{padding:2px 10px;font-size:11.049999999999999px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.btn-small [class^="icon-"],.btn-small [class*=" icon-"]{margin-top:0}
.btn-mini [class^="icon-"],.btn-mini [class*=" icon-"]{margin-top:-1px}
.btn-mini{padding:0 6px;font-size:9.75px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.btn-block{display:block;width:100%;padding-left:0;padding-right:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}
.btn-block+.btn-block{margin-top:5px}
input[type="submit"].btn-block,input[type="reset"].btn-block,input[type="button"].btn-block{width:100%}
.btn-primary.active,.btn-warning.active,.btn-danger.active,.btn-success.active,.btn-info.active,.btn-inverse.active{color:rgba(255,255,255,0.75)}
.btn-primary{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#006dcc;background-image:-moz-linear-gradient(top, #08c, #04c);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#04c));background-image:-webkit-linear-gradient(top, #08c, #04c);background-image:-o-linear-gradient(top, #08c, #04c);background-image:linear-gradient(to bottom, #08c, #04c);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0044cc', GradientType=0);border-color:#04c #04c #002a80;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#04c;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-primary:hover,.btn-primary:focus,.btn-primary:active,.btn-primary.active,.btn-primary.disabled,.btn-primary[disabled]{color:#fff;background-color:#04c;*background-color:#003bb3}
.btn-primary:active,.btn-primary.active{background-color:#039 \9}
.btn-warning{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#faa732;background-image:-moz-linear-gradient(top, #fbb450, #f89406);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));background-image:-webkit-linear-gradient(top, #fbb450, #f89406);background-image:-o-linear-gradient(top, #fbb450, #f89406);background-image:linear-gradient(to bottom, #fbb450, #f89406);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0);border-color:#f89406 #f89406 #ad6704;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#f89406;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-warning:hover,.btn-warning:focus,.btn-warning:active,.btn-warning.active,.btn-warning.disabled,.btn-warning[disabled]{color:#fff;background-color:#f89406;*background-color:#df8505}
.btn-warning:active,.btn-warning.active{background-color:#c67605 \9}
.btn-danger{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#da4f49;background-image:-moz-linear-gradient(top, #ee5f5b, #bd362f);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#bd362f));background-image:-webkit-linear-gradient(top, #ee5f5b, #bd362f);background-image:-o-linear-gradient(top, #ee5f5b, #bd362f);background-image:linear-gradient(to bottom, #ee5f5b, #bd362f);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffbd362f', GradientType=0);border-color:#bd362f #bd362f #802420;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#bd362f;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-danger:hover,.btn-danger:focus,.btn-danger:active,.btn-danger.active,.btn-danger.disabled,.btn-danger[disabled]{color:#fff;background-color:#bd362f;*background-color:#a9302a}
.btn-danger:active,.btn-danger.active{background-color:#942a25 \9}
.btn-success{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#5bb75b;background-image:-moz-linear-gradient(top, #62c462, #51a351);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#51a351));background-image:-webkit-linear-gradient(top, #62c462, #51a351);background-image:-o-linear-gradient(top, #62c462, #51a351);background-image:linear-gradient(to bottom, #62c462, #51a351);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff51a351', GradientType=0);border-color:#51a351 #51a351 #387038;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#51a351;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-success:hover,.btn-success:focus,.btn-success:active,.btn-success.active,.btn-success.disabled,.btn-success[disabled]{color:#fff;background-color:#51a351;*background-color:#499249}
.btn-success:active,.btn-success.active{background-color:#408140 \9}
.btn-info{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#49afcd;background-image:-moz-linear-gradient(top, #5bc0de, #2f96b4);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#2f96b4));background-image:-webkit-linear-gradient(top, #5bc0de, #2f96b4);background-image:-o-linear-gradient(top, #5bc0de, #2f96b4);background-image:linear-gradient(to bottom, #5bc0de, #2f96b4);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff2f96b4', GradientType=0);border-color:#2f96b4 #2f96b4 #1f6377;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#2f96b4;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-info:hover,.btn-info:focus,.btn-info:active,.btn-info.active,.btn-info.disabled,.btn-info[disabled]{color:#fff;background-color:#2f96b4;*background-color:#2a85a0}
.btn-info:active,.btn-info.active{background-color:#24748c \9}
.btn-inverse{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#363636;background-image:-moz-linear-gradient(top, #444, #222);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#444), to(#222));background-image:-webkit-linear-gradient(top, #444, #222);background-image:-o-linear-gradient(top, #444, #222);background-image:linear-gradient(to bottom, #444, #222);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff444444', endColorstr='#ff222222', GradientType=0);border-color:#222 #222 #000;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#222;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-inverse:hover,.btn-inverse:focus,.btn-inverse:active,.btn-inverse.active,.btn-inverse.disabled,.btn-inverse[disabled]{color:#fff;background-color:#222;*background-color:#151515}
.btn-inverse:active,.btn-inverse.active{background-color:#080808 \9}
button.btn,input[type="submit"].btn{*padding-top:3px;*padding-bottom:3px}button.btn::-moz-focus-inner,input[type="submit"].btn::-moz-focus-inner{padding:0;border:0}
button.btn.btn-large,input[type="submit"].btn.btn-large{*padding-top:7px;*padding-bottom:7px}
button.btn.btn-small,input[type="submit"].btn.btn-small{*padding-top:3px;*padding-bottom:3px}
button.btn.btn-mini,input[type="submit"].btn.btn-mini{*padding-top:1px;*padding-bottom:1px}
.btn-link,.btn-link:active,.btn-link[disabled]{background-color:transparent;background-image:none;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}
.btn-link{border-color:transparent;cursor:pointer;color:#08c;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-link:hover,.btn-link:focus{color:#005580;text-decoration:underline;background-color:transparent}
.btn-link[disabled]:hover,.btn-link[disabled]:focus{color:#333;text-decoration:none}
.btn-group{position:relative;display:inline-block;*display:inline;*zoom:1;font-size:0;vertical-align:middle;white-space:nowrap;*margin-left:.3em}.btn-group:first-child{*margin-left:0}
.btn-group+.btn-group{margin-left:5px}
.btn-toolbar{font-size:0;margin-top:10px;margin-bottom:10px}.btn-toolbar>.btn+.btn,.btn-toolbar>.btn-group+.btn,.btn-toolbar>.btn+.btn-group{margin-left:5px}
.btn-group>.btn{position:relative;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-group>.btn+.btn{margin-left:-1px}
.btn-group>.btn,.btn-group>.dropdown-menu,.btn-group>.popover{font-size:13px}
.btn-group>.btn-mini{font-size:9.75px}
.btn-group>.btn-small{font-size:11.049999999999999px}
.btn-group>.btn-large{font-size:16.25px}
.btn-group>.btn:first-child{margin-left:0;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.btn-group>.btn:last-child,.btn-group>.dropdown-toggle{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.btn-group>.btn.large:first-child{margin-left:0;-webkit-border-top-left-radius:6px;-moz-border-radius-topleft:6px;border-top-left-radius:6px;-webkit-border-bottom-left-radius:6px;-moz-border-radius-bottomleft:6px;border-bottom-left-radius:6px}
.btn-group>.btn.large:last-child,.btn-group>.large.dropdown-toggle{-webkit-border-top-right-radius:6px;-moz-border-radius-topright:6px;border-top-right-radius:6px;-webkit-border-bottom-right-radius:6px;-moz-border-radius-bottomright:6px;border-bottom-right-radius:6px}
.btn-group>.btn:hover,.btn-group>.btn:focus,.btn-group>.btn:active,.btn-group>.btn.active{z-index:2}
.btn-group .dropdown-toggle:active,.btn-group.open .dropdown-toggle{outline:0}
.btn-group>.btn+.dropdown-toggle{padding-left:8px;padding-right:8px;-webkit-box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);*padding-top:5px;*padding-bottom:5px}
.btn-group>.btn-mini+.dropdown-toggle{padding-left:5px;padding-right:5px;*padding-top:2px;*padding-bottom:2px}
.btn-group>.btn-small+.dropdown-toggle{*padding-top:5px;*padding-bottom:4px}
.btn-group>.btn-large+.dropdown-toggle{padding-left:12px;padding-right:12px;*padding-top:7px;*padding-bottom:7px}
.btn-group.open .dropdown-toggle{background-image:none;-webkit-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05)}
.btn-group.open .btn.dropdown-toggle{background-color:#e6e6e6}
.btn-group.open .btn-primary.dropdown-toggle{background-color:#04c}
.btn-group.open .btn-warning.dropdown-toggle{background-color:#f89406}
.btn-group.open .btn-danger.dropdown-toggle{background-color:#bd362f}
.btn-group.open .btn-success.dropdown-toggle{background-color:#51a351}
.btn-group.open .btn-info.dropdown-toggle{background-color:#2f96b4}
.btn-group.open .btn-inverse.dropdown-toggle{background-color:#222}
.btn .caret{margin-top:8px;margin-left:0}
.btn-large .caret{margin-top:6px}
.btn-large .caret{border-left-width:5px;border-right-width:5px;border-top-width:5px}
.btn-mini .caret,.btn-small .caret{margin-top:8px}
.dropup .btn-large .caret{border-bottom-width:5px}
.btn-primary .caret,.btn-warning .caret,.btn-danger .caret,.btn-info .caret,.btn-success .caret,.btn-inverse .caret{border-top-color:#fff;border-bottom-color:#fff}
.btn-group-vertical{display:inline-block;*display:inline;*zoom:1}
.btn-group-vertical>.btn{display:block;float:none;max-width:100%;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-group-vertical>.btn+.btn{margin-left:0;margin-top:-1px}
.btn-group-vertical>.btn:first-child{border-radius:4px 4px 0 0;-webkit-border-radius:4px 4px 0 0;-moz-border-radius:4px 4px 0 0;border-radius:4px 4px 0 0}
.btn-group-vertical>.btn:last-child{border-radius:0 0 4px 4px;-webkit-border-radius:0 0 4px 4px;-moz-border-radius:0 0 4px 4px;border-radius:0 0 4px 4px}
.btn-group-vertical>.btn-large:first-child{border-radius:6px 6px 0 0;-webkit-border-radius:6px 6px 0 0;-moz-border-radius:6px 6px 0 0;border-radius:6px 6px 0 0}
.btn-group-vertical>.btn-large:last-child{border-radius:0 0 6px 6px;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px}
.alert{padding:8px 35px 8px 14px;margin-bottom:20px;text-shadow:0 1px 0 rgba(255,255,255,0.5);background-color:#fcf8e3;border:1px solid #fbeed5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.alert,.alert h4{color:#c09853}
.alert h4{margin:0}
.alert .close{position:relative;top:-2px;right:-21px;line-height:20px}
.alert-success{background-color:#dff0d8;border-color:#d6e9c6;color:#468847}
.alert-success h4{color:#468847}
.alert-danger,.alert-error{background-color:#f2dede;border-color:#eed3d7;color:#b94a48}
.alert-danger h4,.alert-error h4{color:#b94a48}
.alert-info{background-color:#d9edf7;border-color:#bce8f1;color:#3a87ad}
.alert-info h4{color:#3a87ad}
.alert-block{padding-top:14px;padding-bottom:14px}
.alert-block>p,.alert-block>ul{margin-bottom:0}
.alert-block p+p{margin-top:5px}
.nav{margin-left:0;margin-bottom:20px;list-style:none}
.nav>li>a{display:block}
.nav>li>a:hover,.nav>li>a:focus{text-decoration:none;background-color:#eee}
.nav>li>a>img{max-width:none}
.nav>.pull-right{float:right}
.nav-header{display:block;padding:3px 15px;font-size:11px;font-weight:bold;line-height:20px;color:#999;text-shadow:0 1px 0 rgba(255,255,255,0.5);text-transform:uppercase}
.nav li+.nav-header{margin-top:9px}
.nav-list{padding-left:15px;padding-right:15px;margin-bottom:0}
.nav-list>li>a,.nav-list .nav-header{margin-left:-15px;margin-right:-15px;text-shadow:0 1px 0 rgba(255,255,255,0.5)}
.nav-list>li>a{padding:3px 15px}
.nav-list>.active>a,.nav-list>.active>a:hover,.nav-list>.active>a:focus{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.2);background-color:#08c}
.nav-list [class^="icon-"],.nav-list [class*=" icon-"]{margin-right:2px}
.nav-list .divider{*width:100%;height:1px;margin:9px 1px;*margin:-5px 0 5px;overflow:hidden;background-color:#e5e5e5;border-bottom:1px solid #fff}
.nav-tabs,.nav-pills{*zoom:1}.nav-tabs:before,.nav-pills:before,.nav-tabs:after,.nav-pills:after{display:table;content:"";line-height:0}
.nav-tabs:after,.nav-pills:after{clear:both}
.nav-tabs>li,.nav-pills>li{float:left}
.nav-tabs>li>a,.nav-pills>li>a{padding-right:12px;padding-left:12px;margin-right:2px;line-height:14px}
.nav-tabs{border-bottom:1px solid #ddd}
.nav-tabs>li{margin-bottom:-1px}
.nav-tabs>li>a{padding-top:8px;padding-bottom:8px;line-height:20px;border:1px solid transparent;border-radius:4px 4px 0 0;-webkit-border-radius:4px 4px 0 0;-moz-border-radius:4px 4px 0 0;border-radius:4px 4px 0 0}.nav-tabs>li>a:hover,.nav-tabs>li>a:focus{border-color:#eee #eee #ddd}
.nav-tabs>.active>a,.nav-tabs>.active>a:hover,.nav-tabs>.active>a:focus{color:#555;background-color:#fff;border:1px solid #ddd;border-bottom-color:transparent;cursor:default}
.nav-pills>li>a{padding-top:8px;padding-bottom:8px;margin-top:2px;margin-bottom:2px;border-radius:5px;-webkit-border-radius:5px;-moz-border-radius:5px;border-radius:5px}
.nav-pills>.active>a,.nav-pills>.active>a:hover,.nav-pills>.active>a:focus{color:#fff;background-color:#08c}
.nav-stacked>li{float:none}
.nav-stacked>li>a{margin-right:0}
.nav-tabs.nav-stacked{border-bottom:0}
.nav-tabs.nav-stacked>li>a{border:1px solid #ddd;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.nav-tabs.nav-stacked>li:first-child>a{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.nav-tabs.nav-stacked>li:last-child>a{-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.nav-tabs.nav-stacked>li>a:hover,.nav-tabs.nav-stacked>li>a:focus{border-color:#ddd;z-index:2}
.nav-pills.nav-stacked>li>a{margin-bottom:3px}
.nav-pills.nav-stacked>li:last-child>a{margin-bottom:1px}
.nav-tabs .dropdown-menu{border-radius:0 0 6px 6px;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px}
.nav-pills .dropdown-menu{border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.nav .dropdown-toggle .caret{border-top-color:#08c;border-bottom-color:#08c;margin-top:6px}
.nav .dropdown-toggle:hover .caret,.nav .dropdown-toggle:focus .caret{border-top-color:#005580;border-bottom-color:#005580}
.nav-tabs .dropdown-toggle .caret{margin-top:8px}
.nav .active .dropdown-toggle .caret{border-top-color:#fff;border-bottom-color:#fff}
.nav-tabs .active .dropdown-toggle .caret{border-top-color:#555;border-bottom-color:#555}
.nav>.dropdown.active>a:hover,.nav>.dropdown.active>a:focus{cursor:pointer}
.nav-tabs .open .dropdown-toggle,.nav-pills .open .dropdown-toggle,.nav>li.dropdown.open.active>a:hover,.nav>li.dropdown.open.active>a:focus{color:#fff;background-color:#999;border-color:#999}
.nav li.dropdown.open .caret,.nav li.dropdown.open.active .caret,.nav li.dropdown.open a:hover .caret,.nav li.dropdown.open a:focus .caret{border-top-color:#fff;border-bottom-color:#fff;opacity:1;filter:alpha(opacity=100)}
.tabs-stacked .open>a:hover,.tabs-stacked .open>a:focus{border-color:#999}
.tabbable{*zoom:1}.tabbable:before,.tabbable:after{display:table;content:"";line-height:0}
.tabbable:after{clear:both}
.tab-content{overflow:auto}
.tabs-below>.nav-tabs,.tabs-right>.nav-tabs,.tabs-left>.nav-tabs{border-bottom:0}
.tab-content>.tab-pane,.pill-content>.pill-pane{display:none}
.tab-content>.active,.pill-content>.active{display:block}
.tabs-below>.nav-tabs{border-top:1px solid #ddd}
.tabs-below>.nav-tabs>li{margin-top:-1px;margin-bottom:0}
.tabs-below>.nav-tabs>li>a{border-radius:0 0 4px 4px;-webkit-border-radius:0 0 4px 4px;-moz-border-radius:0 0 4px 4px;border-radius:0 0 4px 4px}.tabs-below>.nav-tabs>li>a:hover,.tabs-below>.nav-tabs>li>a:focus{border-bottom-color:transparent;border-top-color:#ddd}
.tabs-below>.nav-tabs>.active>a,.tabs-below>.nav-tabs>.active>a:hover,.tabs-below>.nav-tabs>.active>a:focus{border-color:transparent #ddd #ddd #ddd}
.tabs-left>.nav-tabs>li,.tabs-right>.nav-tabs>li{float:none}
.tabs-left>.nav-tabs>li>a,.tabs-right>.nav-tabs>li>a{min-width:74px;margin-right:0;margin-bottom:3px}
.tabs-left>.nav-tabs{float:left;margin-right:19px;border-right:1px solid #ddd}
.tabs-left>.nav-tabs>li>a{margin-right:-1px;border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.tabs-left>.nav-tabs>li>a:hover,.tabs-left>.nav-tabs>li>a:focus{border-color:#eee #ddd #eee #eee}
.tabs-left>.nav-tabs .active>a,.tabs-left>.nav-tabs .active>a:hover,.tabs-left>.nav-tabs .active>a:focus{border-color:#ddd transparent #ddd #ddd;*border-right-color:#fff}
.tabs-right>.nav-tabs{float:right;margin-left:19px;border-left:1px solid #ddd}
.tabs-right>.nav-tabs>li>a{margin-left:-1px;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.tabs-right>.nav-tabs>li>a:hover,.tabs-right>.nav-tabs>li>a:focus{border-color:#eee #eee #eee #ddd}
.tabs-right>.nav-tabs .active>a,.tabs-right>.nav-tabs .active>a:hover,.tabs-right>.nav-tabs .active>a:focus{border-color:#ddd #ddd #ddd transparent;*border-left-color:#fff}
.nav>.disabled>a{color:#999}
.nav>.disabled>a:hover,.nav>.disabled>a:focus{text-decoration:none;background-color:transparent;cursor:default}
.navbar{overflow:visible;margin-bottom:20px;*position:relative;*z-index:2}
.navbar-inner{min-height:36px;padding-left:20px;padding-right:20px;background-color:#fafafa;background-image:-moz-linear-gradient(top, #fff, #f2f2f2);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fff), to(#f2f2f2));background-image:-webkit-linear-gradient(top, #fff, #f2f2f2);background-image:-o-linear-gradient(top, #fff, #f2f2f2);background-image:linear-gradient(to bottom, #fff, #f2f2f2);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff2f2f2', GradientType=0);border:1px solid #d4d4d4;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 4px rgba(0,0,0,0.065);-moz-box-shadow:0 1px 4px rgba(0,0,0,0.065);box-shadow:0 1px 4px rgba(0,0,0,0.065);*zoom:1}.navbar-inner:before,.navbar-inner:after{display:table;content:"";line-height:0}
.navbar-inner:after{clear:both}
.navbar .container{width:auto}
.nav-collapse.collapse{height:auto;overflow:visible}
.navbar .brand{float:left;display:block;padding:8px 20px 8px;margin-left:-20px;font-size:20px;font-weight:200;color:#777;text-shadow:0 1px 0 #fff}.navbar .brand:hover,.navbar .brand:focus{text-decoration:none}
.navbar-text{margin-bottom:0;line-height:36px;color:#777}
.navbar-link{color:#777}.navbar-link:hover,.navbar-link:focus{color:#333}
.navbar .divider-vertical{height:36px;margin:0 9px;border-left:1px solid #f2f2f2;border-right:1px solid #fff}
.navbar .btn,.navbar .btn-group{margin-top:3px}
.navbar .btn-group .btn,.navbar .input-prepend .btn,.navbar .input-append .btn,.navbar .input-prepend .btn-group,.navbar .input-append .btn-group{margin-top:0}
.navbar-form{margin-bottom:0;*zoom:1}.navbar-form:before,.navbar-form:after{display:table;content:"";line-height:0}
.navbar-form:after{clear:both}
.navbar-form input,.navbar-form select,.navbar-form .radio,.navbar-form .checkbox{margin-top:3px}
.navbar-form input,.navbar-form select,.navbar-form .btn{display:inline-block;margin-bottom:0}
.navbar-form input[type="image"],.navbar-form input[type="checkbox"],.navbar-form input[type="radio"]{margin-top:3px}
.navbar-form .input-append,.navbar-form .input-prepend{margin-top:5px;white-space:nowrap}.navbar-form .input-append input,.navbar-form .input-prepend input{margin-top:0}
.navbar-search{position:relative;float:left;margin-top:3px;margin-bottom:0}.navbar-search .search-query{margin-bottom:0;padding:4px 14px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;font-weight:normal;line-height:1;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.navbar-static-top{position:static;margin-bottom:0}.navbar-static-top .navbar-inner{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.navbar-fixed-top,.navbar-fixed-bottom{position:fixed;right:0;left:0;z-index:1030;margin-bottom:0}
.navbar-fixed-top .navbar-inner,.navbar-static-top .navbar-inner{border-width:0 0 1px}
.navbar-fixed-bottom .navbar-inner{border-width:1px 0 0}
.navbar-fixed-top .navbar-inner,.navbar-fixed-bottom .navbar-inner{padding-left:0;padding-right:0;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:940px}
.navbar-fixed-top{top:0}
.navbar-fixed-top .navbar-inner,.navbar-static-top .navbar-inner{-webkit-box-shadow:0 1px 10px rgba(0,0,0,.1);-moz-box-shadow:0 1px 10px rgba(0,0,0,.1);box-shadow:0 1px 10px rgba(0,0,0,.1)}
.navbar-fixed-bottom{bottom:0}.navbar-fixed-bottom .navbar-inner{-webkit-box-shadow:0 -1px 10px rgba(0,0,0,.1);-moz-box-shadow:0 -1px 10px rgba(0,0,0,.1);box-shadow:0 -1px 10px rgba(0,0,0,.1)}
.navbar .nav{position:relative;left:0;display:block;float:left;margin:0 10px 0 0}
.navbar .nav.pull-right{float:right;margin-right:0}
.navbar .nav>li{float:left}
.navbar .nav>li>a{float:none;padding:8px 15px 8px;color:#777;text-decoration:none;text-shadow:0 1px 0 #fff}
.navbar .nav .dropdown-toggle .caret{margin-top:8px}
.navbar .nav>li>a:focus,.navbar .nav>li>a:hover{background-color:transparent;color:#333;text-decoration:none}
.navbar .nav>.active>a,.navbar .nav>.active>a:hover,.navbar .nav>.active>a:focus{color:#555;text-decoration:none;background-color:#e5e5e5;-webkit-box-shadow:inset 0 3px 8px rgba(0,0,0,0.125);-moz-box-shadow:inset 0 3px 8px rgba(0,0,0,0.125);box-shadow:inset 0 3px 8px rgba(0,0,0,0.125)}
.navbar .btn-navbar{display:none;float:right;padding:7px 10px;margin-left:5px;margin-right:5px;color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#ededed;background-image:-moz-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#f2f2f2), to(#e5e5e5));background-image:-webkit-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:-o-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:linear-gradient(to bottom, #f2f2f2, #e5e5e5);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2f2f2', endColorstr='#ffe5e5e5', GradientType=0);border-color:#e5e5e5 #e5e5e5 #bfbfbf;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#e5e5e5;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075)}.navbar .btn-navbar:hover,.navbar .btn-navbar:focus,.navbar .btn-navbar:active,.navbar .btn-navbar.active,.navbar .btn-navbar.disabled,.navbar .btn-navbar[disabled]{color:#fff;background-color:#e5e5e5;*background-color:#d9d9d9}
.navbar .btn-navbar:active,.navbar .btn-navbar.active{background-color:#ccc \9}
.navbar .btn-navbar .icon-bar{display:block;width:18px;height:2px;background-color:#f5f5f5;-webkit-border-radius:1px;-moz-border-radius:1px;border-radius:1px;-webkit-box-shadow:0 1px 0 rgba(0,0,0,0.25);-moz-box-shadow:0 1px 0 rgba(0,0,0,0.25);box-shadow:0 1px 0 rgba(0,0,0,0.25)}
.btn-navbar .icon-bar+.icon-bar{margin-top:3px}
.navbar .nav>li>.dropdown-menu:before{content:'';display:inline-block;border-left:7px solid transparent;border-right:7px solid transparent;border-bottom:7px solid #ccc;border-bottom-color:rgba(0,0,0,0.2);position:absolute;top:-7px;left:9px}
.navbar .nav>li>.dropdown-menu:after{content:'';display:inline-block;border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:6px solid #fff;position:absolute;top:-6px;left:10px}
.navbar-fixed-bottom .nav>li>.dropdown-menu:before{border-top:7px solid #ccc;border-top-color:rgba(0,0,0,0.2);border-bottom:0;bottom:-7px;top:auto}
.navbar-fixed-bottom .nav>li>.dropdown-menu:after{border-top:6px solid #fff;border-bottom:0;bottom:-6px;top:auto}
.navbar .nav li.dropdown>a:hover .caret,.navbar .nav li.dropdown>a:focus .caret{border-top-color:#333;border-bottom-color:#333}
.navbar .nav li.dropdown.open>.dropdown-toggle,.navbar .nav li.dropdown.active>.dropdown-toggle,.navbar .nav li.dropdown.open.active>.dropdown-toggle{background-color:#e5e5e5;color:#555}
.navbar .nav li.dropdown>.dropdown-toggle .caret{border-top-color:#777;border-bottom-color:#777}
.navbar .nav li.dropdown.open>.dropdown-toggle .caret,.navbar .nav li.dropdown.active>.dropdown-toggle .caret,.navbar .nav li.dropdown.open.active>.dropdown-toggle .caret{border-top-color:#555;border-bottom-color:#555}
.navbar .pull-right>li>.dropdown-menu,.navbar .nav>li>.dropdown-menu.pull-right{left:auto;right:0}.navbar .pull-right>li>.dropdown-menu:before,.navbar .nav>li>.dropdown-menu.pull-right:before{left:auto;right:12px}
.navbar .pull-right>li>.dropdown-menu:after,.navbar .nav>li>.dropdown-menu.pull-right:after{left:auto;right:13px}
.navbar .pull-right>li>.dropdown-menu .dropdown-menu,.navbar .nav>li>.dropdown-menu.pull-right .dropdown-menu{left:auto;right:100%;margin-left:0;margin-right:-1px;border-radius:6px 0 6px 6px;-webkit-border-radius:6px 0 6px 6px;-moz-border-radius:6px 0 6px 6px;border-radius:6px 0 6px 6px}
.navbar-inverse .navbar-inner{background-color:#1b1b1b;background-image:-moz-linear-gradient(top, #222, #111);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#222), to(#111));background-image:-webkit-linear-gradient(top, #222, #111);background-image:-o-linear-gradient(top, #222, #111);background-image:linear-gradient(to bottom, #222, #111);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff222222', endColorstr='#ff111111', GradientType=0);border-color:#252525}
.navbar-inverse .brand,.navbar-inverse .nav>li>a{color:#999;text-shadow:0 -1px 0 rgba(0,0,0,0.25)}.navbar-inverse .brand:hover,.navbar-inverse .nav>li>a:hover,.navbar-inverse .brand:focus,.navbar-inverse .nav>li>a:focus{color:#fff}
.navbar-inverse .brand{color:#999}
.navbar-inverse .navbar-text{color:#999}
.navbar-inverse .nav>li>a:focus,.navbar-inverse .nav>li>a:hover{background-color:transparent;color:#fff}
.navbar-inverse .nav .active>a,.navbar-inverse .nav .active>a:hover,.navbar-inverse .nav .active>a:focus{color:#fff;background-color:#111}
.navbar-inverse .navbar-link{color:#999}.navbar-inverse .navbar-link:hover,.navbar-inverse .navbar-link:focus{color:#fff}
.navbar-inverse .divider-vertical{border-left-color:#111;border-right-color:#222}
.navbar-inverse .nav li.dropdown.open>.dropdown-toggle,.navbar-inverse .nav li.dropdown.active>.dropdown-toggle,.navbar-inverse .nav li.dropdown.open.active>.dropdown-toggle{background-color:#111;color:#fff}
.navbar-inverse .nav li.dropdown>a:hover .caret,.navbar-inverse .nav li.dropdown>a:focus .caret{border-top-color:#fff;border-bottom-color:#fff}
.navbar-inverse .nav li.dropdown>.dropdown-toggle .caret{border-top-color:#999;border-bottom-color:#999}
.navbar-inverse .nav li.dropdown.open>.dropdown-toggle .caret,.navbar-inverse .nav li.dropdown.active>.dropdown-toggle .caret,.navbar-inverse .nav li.dropdown.open.active>.dropdown-toggle .caret{border-top-color:#fff;border-bottom-color:#fff}
.navbar-inverse .navbar-search .search-query{color:#fff;background-color:#515151;border-color:#111;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);-webkit-transition:none;-moz-transition:none;-o-transition:none;transition:none}.navbar-inverse .navbar-search .search-query:-moz-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query:-ms-input-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query::-webkit-input-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query:focus,.navbar-inverse .navbar-search .search-query.focused{padding:5px 15px;color:#333;text-shadow:0 1px 0 #fff;background-color:#fff;border:0;-webkit-box-shadow:0 0 3px rgba(0,0,0,0.15);-moz-box-shadow:0 0 3px rgba(0,0,0,0.15);box-shadow:0 0 3px rgba(0,0,0,0.15);outline:0}
.navbar-inverse .btn-navbar{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#0e0e0e;background-image:-moz-linear-gradient(top, #151515, #040404);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#151515), to(#040404));background-image:-webkit-linear-gradient(top, #151515, #040404);background-image:-o-linear-gradient(top, #151515, #040404);background-image:linear-gradient(to bottom, #151515, #040404);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff151515', endColorstr='#ff040404', GradientType=0);border-color:#040404 #040404 #000;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#040404;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.navbar-inverse .btn-navbar:hover,.navbar-inverse .btn-navbar:focus,.navbar-inverse .btn-navbar:active,.navbar-inverse .btn-navbar.active,.navbar-inverse .btn-navbar.disabled,.navbar-inverse .btn-navbar[disabled]{color:#fff;background-color:#040404;*background-color:#000}
.navbar-inverse .btn-navbar:active,.navbar-inverse .btn-navbar.active{background-color:#000 \9}
.breadcrumb{padding:8px 15px;margin:0 0 20px;list-style:none;background-color:#f5f5f5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}.breadcrumb>li{display:inline-block;*display:inline;*zoom:1;text-shadow:0 1px 0 #fff}.breadcrumb>li>.divider{padding:0 5px;color:#ccc}
.breadcrumb>.active{color:#999}
.pagination{margin:20px 0}
.pagination ul{display:inline-block;*display:inline;*zoom:1;margin-left:0;margin-bottom:0;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.05);-moz-box-shadow:0 1px 2px rgba(0,0,0,0.05);box-shadow:0 1px 2px rgba(0,0,0,0.05)}
.pagination ul>li{display:inline}
.pagination ul>li>a,.pagination ul>li>span{float:left;padding:4px 12px;line-height:20px;text-decoration:none;background-color:#fff;border:1px solid #ddd;border-left-width:0}
.pagination ul>li>a:hover,.pagination ul>li>a:focus,.pagination ul>.active>a,.pagination ul>.active>span{background-color:#f5f5f5}
.pagination ul>.active>a,.pagination ul>.active>span{color:#999;cursor:default}
.pagination ul>.disabled>span,.pagination ul>.disabled>a,.pagination ul>.disabled>a:hover,.pagination ul>.disabled>a:focus{color:#999;background-color:transparent;cursor:default}
.pagination ul>li:first-child>a,.pagination ul>li:first-child>span{border-left-width:1px;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.pagination ul>li:last-child>a,.pagination ul>li:last-child>span{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.pagination-centered{text-align:center}
.pagination-right{text-align:right}
.pagination-large ul>li>a,.pagination-large ul>li>span{padding:11px 19px;font-size:16.25px}
.pagination-large ul>li:first-child>a,.pagination-large ul>li:first-child>span{-webkit-border-top-left-radius:6px;-moz-border-radius-topleft:6px;border-top-left-radius:6px;-webkit-border-bottom-left-radius:6px;-moz-border-radius-bottomleft:6px;border-bottom-left-radius:6px}
.pagination-large ul>li:last-child>a,.pagination-large ul>li:last-child>span{-webkit-border-top-right-radius:6px;-moz-border-radius-topright:6px;border-top-right-radius:6px;-webkit-border-bottom-right-radius:6px;-moz-border-radius-bottomright:6px;border-bottom-right-radius:6px}
.pagination-mini ul>li:first-child>a,.pagination-small ul>li:first-child>a,.pagination-mini ul>li:first-child>span,.pagination-small ul>li:first-child>span{-webkit-border-top-left-radius:3px;-moz-border-radius-topleft:3px;border-top-left-radius:3px;-webkit-border-bottom-left-radius:3px;-moz-border-radius-bottomleft:3px;border-bottom-left-radius:3px}
.pagination-mini ul>li:last-child>a,.pagination-small ul>li:last-child>a,.pagination-mini ul>li:last-child>span,.pagination-small ul>li:last-child>span{-webkit-border-top-right-radius:3px;-moz-border-radius-topright:3px;border-top-right-radius:3px;-webkit-border-bottom-right-radius:3px;-moz-border-radius-bottomright:3px;border-bottom-right-radius:3px}
.pagination-small ul>li>a,.pagination-small ul>li>span{padding:2px 10px;font-size:11.049999999999999px}
.pagination-mini ul>li>a,.pagination-mini ul>li>span{padding:0 6px;font-size:9.75px}
.pager{margin:20px 0;list-style:none;text-align:center;*zoom:1}.pager:before,.pager:after{display:table;content:"";line-height:0}
.pager:after{clear:both}
.pager li{display:inline}
.pager li>a,.pager li>span{display:inline-block;padding:5px 14px;background-color:#fff;border:1px solid #ddd;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.pager li>a:hover,.pager li>a:focus{text-decoration:none;background-color:#f5f5f5}
.pager .next>a,.pager .next>span{float:right}
.pager .previous>a,.pager .previous>span{float:left}
.pager .disabled>a,.pager .disabled>a:hover,.pager .disabled>a:focus,.pager .disabled>span{color:#999;background-color:#fff;cursor:default}
.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0}
.modal-backdrop,.modal-backdrop.fade.in{opacity:.8;filter:alpha(opacity=80)}
.modal{position:fixed;top:10%;left:50%;z-index:1050;width:560px;margin-left:-280px;background-color:#fff;border:1px solid #999;border:1px solid rgba(0,0,0,0.3);*border:1px solid #999;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 3px 7px rgba(0,0,0,0.3);-moz-box-shadow:0 3px 7px rgba(0,0,0,0.3);box-shadow:0 3px 7px rgba(0,0,0,0.3);-webkit-background-clip:padding-box;-moz-background-clip:padding-box;background-clip:padding-box;outline:none}.modal.fade{-webkit-transition:opacity .3s linear, top .3s ease-out;-moz-transition:opacity .3s linear, top .3s ease-out;-o-transition:opacity .3s linear, top .3s ease-out;transition:opacity .3s linear, top .3s ease-out;top:-25%}
.modal.fade.in{top:10%}
.modal-header{padding:9px 15px;border-bottom:1px solid #eee}.modal-header .close{margin-top:2px}
.modal-header h3{margin:0;line-height:30px}
.modal-body{position:relative;overflow-y:auto;max-height:400px;padding:15px}
.modal-form{margin-bottom:0}
.modal-footer{padding:14px 15px 15px;margin-bottom:0;text-align:right;background-color:#f5f5f5;border-top:1px solid #ddd;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px;-webkit-box-shadow:inset 0 1px 0 #fff;-moz-box-shadow:inset 0 1px 0 #fff;box-shadow:inset 0 1px 0 #fff;*zoom:1}.modal-footer:before,.modal-footer:after{display:table;content:"";line-height:0}
.modal-footer:after{clear:both}
.modal-footer .btn+.btn{margin-left:5px;margin-bottom:0}
.modal-footer .btn-group .btn+.btn{margin-left:-1px}
.modal-footer .btn-block+.btn-block{margin-left:0}
.tooltip{position:absolute;z-index:1030;display:block;visibility:visible;font-size:11px;line-height:1.4;opacity:0;filter:alpha(opacity=0)}.tooltip.in{opacity:.8;filter:alpha(opacity=80)}
.tooltip.top{margin-top:-3px;padding:5px 0}
.tooltip.right{margin-left:3px;padding:0 5px}
.tooltip.bottom{margin-top:3px;padding:5px 0}
.tooltip.left{margin-left:-3px;padding:0 5px}
.tooltip-inner{max-width:200px;padding:8px;color:#fff;text-align:center;text-decoration:none;background-color:#000;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.tooltip-arrow{position:absolute;width:0;height:0;border-color:transparent;border-style:solid}
.tooltip.top .tooltip-arrow{bottom:0;left:50%;margin-left:-5px;border-width:5px 5px 0;border-top-color:#000}
.tooltip.right .tooltip-arrow{top:50%;left:0;margin-top:-5px;border-width:5px 5px 5px 0;border-right-color:#000}
.tooltip.left .tooltip-arrow{top:50%;right:0;margin-top:-5px;border-width:5px 0 5px 5px;border-left-color:#000}
.tooltip.bottom .tooltip-arrow{top:0;left:50%;margin-left:-5px;border-width:0 5px 5px;border-bottom-color:#000}
.popover{position:absolute;top:0;left:0;z-index:1010;display:none;max-width:276px;padding:1px;text-align:left;background-color:#fff;-webkit-background-clip:padding-box;-moz-background-clip:padding;background-clip:padding-box;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,0.2);-moz-box-shadow:0 5px 10px rgba(0,0,0,0.2);box-shadow:0 5px 10px rgba(0,0,0,0.2);white-space:normal}.popover.top{margin-top:-10px}
.popover.right{margin-left:10px}
.popover.bottom{margin-top:10px}
.popover.left{margin-left:-10px}
.popover-title{margin:0;padding:8px 14px;font-size:14px;font-weight:normal;line-height:18px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-radius:5px 5px 0 0;-webkit-border-radius:5px 5px 0 0;-moz-border-radius:5px 5px 0 0;border-radius:5px 5px 0 0}.popover-title:empty{display:none}
.popover-content{padding:9px 14px}
.popover .arrow,.popover .arrow:after{position:absolute;display:block;width:0;height:0;border-color:transparent;border-style:solid}
.popover .arrow{border-width:11px}
.popover .arrow:after{border-width:10px;content:""}
.popover.top .arrow{left:50%;margin-left:-11px;border-bottom-width:0;border-top-color:#999;border-top-color:rgba(0,0,0,0.25);bottom:-11px}.popover.top .arrow:after{bottom:1px;margin-left:-10px;border-bottom-width:0;border-top-color:#fff}
.popover.right .arrow{top:50%;left:-11px;margin-top:-11px;border-left-width:0;border-right-color:#999;border-right-color:rgba(0,0,0,0.25)}.popover.right .arrow:after{left:1px;bottom:-10px;border-left-width:0;border-right-color:#fff}
.popover.bottom .arrow{left:50%;margin-left:-11px;border-top-width:0;border-bottom-color:#999;border-bottom-color:rgba(0,0,0,0.25);top:-11px}.popover.bottom .arrow:after{top:1px;margin-left:-10px;border-top-width:0;border-bottom-color:#fff}
.popover.left .arrow{top:50%;right:-11px;margin-top:-11px;border-right-width:0;border-left-color:#999;border-left-color:rgba(0,0,0,0.25)}.popover.left .arrow:after{right:1px;border-right-width:0;border-left-color:#fff;bottom:-10px}
.thumbnails{margin-left:-20px;list-style:none;*zoom:1}.thumbnails:before,.thumbnails:after{display:table;content:"";line-height:0}
.thumbnails:after{clear:both}
.row-fluid .thumbnails{margin-left:0}
.thumbnails>li{float:left;margin-bottom:20px;margin-left:20px}
.thumbnail{display:block;padding:4px;line-height:20px;border:1px solid #ddd;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.055);-moz-box-shadow:0 1px 3px rgba(0,0,0,0.055);box-shadow:0 1px 3px rgba(0,0,0,0.055);-webkit-transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out}
a.thumbnail:hover,a.thumbnail:focus{border-color:#08c;-webkit-box-shadow:0 1px 4px rgba(0,105,214,0.25);-moz-box-shadow:0 1px 4px rgba(0,105,214,0.25);box-shadow:0 1px 4px rgba(0,105,214,0.25)}
.thumbnail>img{display:block;max-width:100%;margin-left:auto;margin-right:auto}
.thumbnail .caption{padding:9px;color:#555}
.media,.media-body{overflow:hidden;*overflow:visible;zoom:1}
.media,.media .media{margin-top:15px}
.media:first-child{margin-top:0}
.media-object{display:block}
.media-heading{margin:0 0 5px}
.media>.pull-left{margin-right:10px}
.media>.pull-right{margin-left:10px}
.media-list{margin-left:0;list-style:none}
.label,.badge{display:inline-block;padding:2px 4px;font-size:10.998px;font-weight:bold;line-height:14px;color:#fff;vertical-align:baseline;white-space:nowrap;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#999}
.label{border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.badge{padding-left:9px;padding-right:9px;border-radius:9px;-webkit-border-radius:9px;-moz-border-radius:9px;border-radius:9px}
.label:empty,.badge:empty{display:none}
a.label:hover,a.label:focus,a.badge:hover,a.badge:focus{color:#fff;text-decoration:none;cursor:pointer}
.label-important,.badge-important{background-color:#b94a48}
.label-important[href],.badge-important[href]{background-color:#953b39}
.label-warning,.badge-warning{background-color:#f89406}
.label-warning[href],.badge-warning[href]{background-color:#c67605}
.label-success,.badge-success{background-color:#468847}
.label-success[href],.badge-success[href]{background-color:#356635}
.label-info,.badge-info{background-color:#3a87ad}
.label-info[href],.badge-info[href]{background-color:#2d6987}
.label-inverse,.badge-inverse{background-color:#333}
.label-inverse[href],.badge-inverse[href]{background-color:#1a1a1a}
.btn .label,.btn .badge{position:relative;top:-1px}
.btn-mini .label,.btn-mini .badge{top:0}
@-webkit-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-moz-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-ms-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-o-keyframes progress-bar-stripes{from{background-position:0 0} to{background-position:40px 0}}@keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}.progress{overflow:hidden;height:20px;margin-bottom:20px;background-color:#f7f7f7;background-image:-moz-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#f5f5f5), to(#f9f9f9));background-image:-webkit-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:-o-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:linear-gradient(to bottom, #f5f5f5, #f9f9f9);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#fff9f9f9', GradientType=0);-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.progress .bar{width:0;height:100%;color:#fff;float:left;font-size:12px;text-align:center;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#0e90d2;background-image:-moz-linear-gradient(top, #149bdf, #0480be);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#149bdf), to(#0480be));background-image:-webkit-linear-gradient(top, #149bdf, #0480be);background-image:-o-linear-gradient(top, #149bdf, #0480be);background-image:linear-gradient(to bottom, #149bdf, #0480be);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff149bdf', endColorstr='#ff0480be', GradientType=0);-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);-moz-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;-webkit-transition:width .6s ease;-moz-transition:width .6s ease;-o-transition:width .6s ease;transition:width .6s ease}
.progress .bar+.bar{-webkit-box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);-moz-box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15)}
.progress-striped .bar{background-color:#149bdf;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);-webkit-background-size:40px 40px;-moz-background-size:40px 40px;-o-background-size:40px 40px;background-size:40px 40px}
.progress.active .bar{-webkit-animation:progress-bar-stripes 2s linear infinite;-moz-animation:progress-bar-stripes 2s linear infinite;-ms-animation:progress-bar-stripes 2s linear infinite;-o-animation:progress-bar-stripes 2s linear infinite;animation:progress-bar-stripes 2s linear infinite}
.progress-danger .bar,.progress .bar-danger{background-color:#dd514c;background-image:-moz-linear-gradient(top, #ee5f5b, #c43c35);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#c43c35));background-image:-webkit-linear-gradient(top, #ee5f5b, #c43c35);background-image:-o-linear-gradient(top, #ee5f5b, #c43c35);background-image:linear-gradient(to bottom, #ee5f5b, #c43c35);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffc43c35', GradientType=0)}
.progress-danger.progress-striped .bar,.progress-striped .bar-danger{background-color:#ee5f5b;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-success .bar,.progress .bar-success{background-color:#5eb95e;background-image:-moz-linear-gradient(top, #62c462, #57a957);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#57a957));background-image:-webkit-linear-gradient(top, #62c462, #57a957);background-image:-o-linear-gradient(top, #62c462, #57a957);background-image:linear-gradient(to bottom, #62c462, #57a957);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff57a957', GradientType=0)}
.progress-success.progress-striped .bar,.progress-striped .bar-success{background-color:#62c462;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-info .bar,.progress .bar-info{background-color:#4bb1cf;background-image:-moz-linear-gradient(top, #5bc0de, #339bb9);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#339bb9));background-image:-webkit-linear-gradient(top, #5bc0de, #339bb9);background-image:-o-linear-gradient(top, #5bc0de, #339bb9);background-image:linear-gradient(to bottom, #5bc0de, #339bb9);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff339bb9', GradientType=0)}
.progress-info.progress-striped .bar,.progress-striped .bar-info{background-color:#5bc0de;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-warning .bar,.progress .bar-warning{background-color:#faa732;background-image:-moz-linear-gradient(top, #fbb450, #f89406);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));background-image:-webkit-linear-gradient(top, #fbb450, #f89406);background-image:-o-linear-gradient(top, #fbb450, #f89406);background-image:linear-gradient(to bottom, #fbb450, #f89406);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0)}
.progress-warning.progress-striped .bar,.progress-striped .bar-warning{background-color:#fbb450;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.accordion{margin-bottom:20px}
.accordion-group{margin-bottom:2px;border:1px solid #e5e5e5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.accordion-heading{border-bottom:0}
.accordion-heading .accordion-toggle{display:block;padding:8px 15px}
.accordion-toggle{cursor:pointer}
.accordion-inner{padding:9px 15px;border-top:1px solid #e5e5e5}
.carousel{position:relative;margin-bottom:20px;line-height:1}
.carousel-inner{overflow:hidden;width:100%;position:relative}
.carousel-inner>.item{display:none;position:relative;-webkit-transition:.6s ease-in-out left;-moz-transition:.6s ease-in-out left;-o-transition:.6s ease-in-out left;transition:.6s ease-in-out left}.carousel-inner>.item>img,.carousel-inner>.item>a>img{display:block;line-height:1}
.carousel-inner>.active,.carousel-inner>.next,.carousel-inner>.prev{display:block}
.carousel-inner>.active{left:0}
.carousel-inner>.next,.carousel-inner>.prev{position:absolute;top:0;width:100%}
.carousel-inner>.next{left:100%}
.carousel-inner>.prev{left:-100%}
.carousel-inner>.next.left,.carousel-inner>.prev.right{left:0}
.carousel-inner>.active.left{left:-100%}
.carousel-inner>.active.right{left:100%}
.carousel-control{position:absolute;top:40%;left:15px;width:40px;height:40px;margin-top:-20px;font-size:60px;font-weight:100;line-height:30px;color:#fff;text-align:center;background:#222;border:3px solid #fff;-webkit-border-radius:23px;-moz-border-radius:23px;border-radius:23px;opacity:.5;filter:alpha(opacity=50)}.carousel-control.right{left:auto;right:15px}
.carousel-control:hover,.carousel-control:focus{color:#fff;text-decoration:none;opacity:.9;filter:alpha(opacity=90)}
.carousel-indicators{position:absolute;top:15px;right:15px;z-index:5;margin:0;list-style:none}.carousel-indicators li{display:block;float:left;width:10px;height:10px;margin-left:5px;text-indent:-999px;background-color:#ccc;background-color:rgba(255,255,255,0.25);border-radius:5px}
.carousel-indicators .active{background-color:#fff}
.carousel-caption{position:absolute;left:0;right:0;bottom:0;padding:15px;background:#333;background:rgba(0,0,0,0.75)}
.carousel-caption h4,.carousel-caption p{color:#fff;line-height:20px}
.carousel-caption h4{margin:0 0 5px}
.carousel-caption p{margin-bottom:0}
.hero-unit{padding:60px;margin-bottom:30px;font-size:18px;font-weight:200;line-height:30px;color:inherit;background-color:#eee;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}.hero-unit h1{margin-bottom:0;font-size:60px;line-height:1;color:inherit;letter-spacing:-1px}
.hero-unit li{line-height:30px}
.pull-right{float:right}
.pull-left{float:left}
.hide{display:none}
.show{display:block}
.invisible{visibility:hidden}
.affix{position:fixed}
@-ms-viewport{width:device-width}.hidden{display:none;visibility:hidden}
.visible-phone{display:none !important}
.visible-tablet{display:none !important}
.hidden-desktop{display:none !important}
.visible-desktop{display:inherit !important}
@media (min-width:768px) and (max-width:979px){.hidden-desktop{display:inherit !important} .visible-desktop{display:none !important} .visible-tablet{display:inherit !important} .hidden-tablet{display:none !important}}@media (max-width:767px){.hidden-desktop{display:inherit !important} .visible-desktop{display:none !important} .visible-phone{display:inherit !important} .hidden-phone{display:none !important}}.visible-print{display:none !important}
@media print{.visible-print{display:inherit !important} .hidden-print{display:none !important}}@media (min-width:1200px){.row{margin-left:-30px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0} .row:after{clear:both} [class*="span"]{float:left;min-height:1px;margin-left:30px} .container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:1170px} .span12{width:1170px} .span11{width:1070px} .span10{width:970px} .span9{width:870px} .span8{width:770px} .span7{width:670px} .span6{width:570px} .span5{width:470px} .span4{width:370px} .span3{width:270px} .span2{width:170px} .span1{width:70px} .offset12{margin-left:1230px} .offset11{margin-left:1130px} .offset10{margin-left:1030px} .offset9{margin-left:930px} .offset8{margin-left:830px} .offset7{margin-left:730px} .offset6{margin-left:630px} .offset5{margin-left:530px} .offset4{margin-left:430px} .offset3{margin-left:330px} .offset2{margin-left:230px} .offset1{margin-left:130px} .row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0} .row-fluid:after{clear:both} .row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.564102564102564%;*margin-left:2.5109110747408616%} .row-fluid [class*="span"]:first-child{margin-left:0} .row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.564102564102564%} .row-fluid .span12{width:100%;*width:99.94680851063829%} .row-fluid .span11{width:91.45299145299145%;*width:91.39979996362975%} .row-fluid .span10{width:82.90598290598291%;*width:82.8527914166212%} .row-fluid .span9{width:74.35897435897436%;*width:74.30578286961266%} .row-fluid .span8{width:65.81196581196582%;*width:65.75877432260411%} .row-fluid .span7{width:57.26495726495726%;*width:57.21176577559556%} .row-fluid .span6{width:48.717948717948715%;*width:48.664757228587014%} .row-fluid .span5{width:40.17094017094017%;*width:40.11774868157847%} .row-fluid .span4{width:31.623931623931625%;*width:31.570740134569924%} .row-fluid .span3{width:23.076923076923077%;*width:23.023731587561375%} .row-fluid .span2{width:14.52991452991453%;*width:14.476723040552828%} .row-fluid .span1{width:5.982905982905983%;*width:5.929714493544281%} .row-fluid .offset12{margin-left:105.12820512820512%;*margin-left:105.02182214948171%} .row-fluid .offset12:first-child{margin-left:102.56410256410257%;*margin-left:102.45771958537915%} .row-fluid .offset11{margin-left:96.58119658119658%;*margin-left:96.47481360247316%} .row-fluid .offset11:first-child{margin-left:94.01709401709402%;*margin-left:93.91071103837061%} .row-fluid .offset10{margin-left:88.03418803418803%;*margin-left:87.92780505546462%} .row-fluid .offset10:first-child{margin-left:85.47008547008548%;*margin-left:85.36370249136206%} .row-fluid .offset9{margin-left:79.48717948717949%;*margin-left:79.38079650845607%} .row-fluid .offset9:first-child{margin-left:76.92307692307693%;*margin-left:76.81669394435352%} .row-fluid .offset8{margin-left:70.94017094017094%;*margin-left:70.83378796144753%} .row-fluid .offset8:first-child{margin-left:68.37606837606839%;*margin-left:68.26968539734497%} .row-fluid .offset7{margin-left:62.393162393162385%;*margin-left:62.28677941443899%} .row-fluid .offset7:first-child{margin-left:59.82905982905982%;*margin-left:59.72267685033642%} .row-fluid .offset6{margin-left:53.84615384615384%;*margin-left:53.739770867430444%} .row-fluid .offset6:first-child{margin-left:51.28205128205128%;*margin-left:51.175668303327875%} .row-fluid .offset5{margin-left:45.299145299145295%;*margin-left:45.1927623204219%} .row-fluid .offset5:first-child{margin-left:42.73504273504273%;*margin-left:42.62865975631933%} .row-fluid .offset4{margin-left:36.75213675213675%;*margin-left:36.645753773413354%} .row-fluid .offset4:first-child{margin-left:34.18803418803419%;*margin-left:34.081651209310785%} .row-fluid .offset3{margin-left:28.205128205128204%;*margin-left:28.0987452264048%} .row-fluid .offset3:first-child{margin-left:25.641025641025642%;*margin-left:25.53464266230224%} .row-fluid .offset2{margin-left:19.65811965811966%;*margin-left:19.551736679396257%} .row-fluid .offset2:first-child{margin-left:17.094017094017094%;*margin-left:16.98763411529369%} .row-fluid .offset1{margin-left:11.11111111111111%;*margin-left:11.004728132387708%} .row-fluid .offset1:first-child{margin-left:8.547008547008547%;*margin-left:8.440625568285142%} input,textarea,.uneditable-input{margin-left:0} .controls-row [class*="span"]+[class*="span"]{margin-left:30px} input.span12,textarea.span12,.uneditable-input.span12{width:1156px} input.span11,textarea.span11,.uneditable-input.span11{width:1056px} input.span10,textarea.span10,.uneditable-input.span10{width:956px} input.span9,textarea.span9,.uneditable-input.span9{width:856px} input.span8,textarea.span8,.uneditable-input.span8{width:756px} input.span7,textarea.span7,.uneditable-input.span7{width:656px} input.span6,textarea.span6,.uneditable-input.span6{width:556px} input.span5,textarea.span5,.uneditable-input.span5{width:456px} input.span4,textarea.span4,.uneditable-input.span4{width:356px} input.span3,textarea.span3,.uneditable-input.span3{width:256px} input.span2,textarea.span2,.uneditable-input.span2{width:156px} input.span1,textarea.span1,.uneditable-input.span1{width:56px} .thumbnails{margin-left:-30px} .thumbnails>li{margin-left:30px} .row-fluid .thumbnails{margin-left:0}}@media (min-width:768px) and (max-width:979px){.row{margin-left:-20px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0} .row:after{clear:both} [class*="span"]{float:left;min-height:1px;margin-left:20px} .container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:724px} .span12{width:724px} .span11{width:662px} .span10{width:600px} .span9{width:538px} .span8{width:476px} .span7{width:414px} .span6{width:352px} .span5{width:290px} .span4{width:228px} .span3{width:166px} .span2{width:104px} .span1{width:42px} .offset12{margin-left:764px} .offset11{margin-left:702px} .offset10{margin-left:640px} .offset9{margin-left:578px} .offset8{margin-left:516px} .offset7{margin-left:454px} .offset6{margin-left:392px} .offset5{margin-left:330px} .offset4{margin-left:268px} .offset3{margin-left:206px} .offset2{margin-left:144px} .offset1{margin-left:82px} .row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0} .row-fluid:after{clear:both} .row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.7624309392265194%;*margin-left:2.709239449864817%} .row-fluid [class*="span"]:first-child{margin-left:0} .row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.7624309392265194%} .row-fluid .span12{width:100%;*width:99.94680851063829%} .row-fluid .span11{width:91.43646408839778%;*width:91.38327259903608%} .row-fluid .span10{width:82.87292817679558%;*width:82.81973668743387%} .row-fluid .span9{width:74.30939226519337%;*width:74.25620077583166%} .row-fluid .span8{width:65.74585635359117%;*width:65.69266486422946%} .row-fluid .span7{width:57.18232044198895%;*width:57.12912895262725%} .row-fluid .span6{width:48.61878453038674%;*width:48.56559304102504%} .row-fluid .span5{width:40.05524861878453%;*width:40.00205712942283%} .row-fluid .span4{width:31.491712707182323%;*width:31.43852121782062%} .row-fluid .span3{width:22.92817679558011%;*width:22.87498530621841%} .row-fluid .span2{width:14.3646408839779%;*width:14.311449394616199%} .row-fluid .span1{width:5.801104972375691%;*width:5.747913483013988%} .row-fluid .offset12{margin-left:105.52486187845304%;*margin-left:105.41847889972962%} .row-fluid .offset12:first-child{margin-left:102.76243093922652%;*margin-left:102.6560479605031%} .row-fluid .offset11{margin-left:96.96132596685082%;*margin-left:96.8549429881274%} .row-fluid .offset11:first-child{margin-left:94.1988950276243%;*margin-left:94.09251204890089%} .row-fluid .offset10{margin-left:88.39779005524862%;*margin-left:88.2914070765252%} .row-fluid .offset10:first-child{margin-left:85.6353591160221%;*margin-left:85.52897613729868%} .row-fluid .offset9{margin-left:79.8342541436464%;*margin-left:79.72787116492299%} .row-fluid .offset9:first-child{margin-left:77.07182320441989%;*margin-left:76.96544022569647%} .row-fluid .offset8{margin-left:71.2707182320442%;*margin-left:71.16433525332079%} .row-fluid .offset8:first-child{margin-left:68.50828729281768%;*margin-left:68.40190431409427%} .row-fluid .offset7{margin-left:62.70718232044199%;*margin-left:62.600799341718584%} .row-fluid .offset7:first-child{margin-left:59.94475138121547%;*margin-left:59.838368402492065%} .row-fluid .offset6{margin-left:54.14364640883978%;*margin-left:54.037263430116376%} .row-fluid .offset6:first-child{margin-left:51.38121546961326%;*margin-left:51.27483249088986%} .row-fluid .offset5{margin-left:45.58011049723757%;*margin-left:45.47372751851417%} .row-fluid .offset5:first-child{margin-left:42.81767955801105%;*margin-left:42.71129657928765%} .row-fluid .offset4{margin-left:37.01657458563536%;*margin-left:36.91019160691196%} .row-fluid .offset4:first-child{margin-left:34.25414364640884%;*margin-left:34.14776066768544%} .row-fluid .offset3{margin-left:28.45303867403315%;*margin-left:28.346655695309746%} .row-fluid .offset3:first-child{margin-left:25.69060773480663%;*margin-left:25.584224756083227%} .row-fluid .offset2{margin-left:19.88950276243094%;*margin-left:19.783119783707537%} .row-fluid .offset2:first-child{margin-left:17.12707182320442%;*margin-left:17.02068884448102%} .row-fluid .offset1{margin-left:11.32596685082873%;*margin-left:11.219583872105325%} .row-fluid .offset1:first-child{margin-left:8.56353591160221%;*margin-left:8.457152932878806%} input,textarea,.uneditable-input{margin-left:0} .controls-row [class*="span"]+[class*="span"]{margin-left:20px} input.span12,textarea.span12,.uneditable-input.span12{width:710px} input.span11,textarea.span11,.uneditable-input.span11{width:648px} input.span10,textarea.span10,.uneditable-input.span10{width:586px} input.span9,textarea.span9,.uneditable-input.span9{width:524px} input.span8,textarea.span8,.uneditable-input.span8{width:462px} input.span7,textarea.span7,.uneditable-input.span7{width:400px} input.span6,textarea.span6,.uneditable-input.span6{width:338px} input.span5,textarea.span5,.uneditable-input.span5{width:276px} input.span4,textarea.span4,.uneditable-input.span4{width:214px} input.span3,textarea.span3,.uneditable-input.span3{width:152px} input.span2,textarea.span2,.uneditable-input.span2{width:90px} input.span1,textarea.span1,.uneditable-input.span1{width:28px}}@media (max-width:767px){body{padding-left:20px;padding-right:20px} .navbar-fixed-top,.navbar-fixed-bottom,.navbar-static-top{margin-left:-20px;margin-right:-20px} .container-fluid{padding:0} .dl-horizontal dt{float:none;clear:none;width:auto;text-align:left} .dl-horizontal dd{margin-left:0} .container{width:auto} .row-fluid{width:100%} .row,.thumbnails{margin-left:0} .thumbnails>li{float:none;margin-left:0} [class*="span"],.uneditable-input[class*="span"],.row-fluid [class*="span"]{float:none;display:block;width:100%;margin-left:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .span12,.row-fluid .span12{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .row-fluid [class*="offset"]:first-child{margin-left:0} .input-large,.input-xlarge,.input-xxlarge,input[class*="span"],select[class*="span"],textarea[class*="span"],.uneditable-input{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .input-prepend input,.input-append input,.input-prepend input[class*="span"],.input-append input[class*="span"]{display:inline-block;width:auto} .controls-row [class*="span"]+[class*="span"]{margin-left:0} .modal{position:fixed;top:20px;left:20px;right:20px;width:auto;margin:0}.modal.fade{top:-100px} .modal.fade.in{top:20px}}@media (max-width:480px){.nav-collapse{-webkit-transform:translate3d(0, 0, 0)} .page-header h1 small{display:block;line-height:20px} input[type="checkbox"],input[type="radio"]{border:1px solid #ccc} .form-horizontal .control-label{float:none;width:auto;padding-top:0;text-align:left} .form-horizontal .controls{margin-left:0} .form-horizontal .control-list{padding-top:0} .form-horizontal .form-actions{padding-left:10px;padding-right:10px} .media .pull-left,.media .pull-right{float:none;display:block;margin-bottom:10px} .media-object{margin-right:0;margin-left:0} .modal{top:10px;left:10px;right:10px} .modal-header .close{padding:10px;margin:-10px} .carousel-caption{position:static}}@media (max-width:979px){body{padding-top:0} .navbar-fixed-top,.navbar-fixed-bottom{position:static} .navbar-fixed-top{margin-bottom:20px} .navbar-fixed-bottom{margin-top:20px} .navbar-fixed-top .navbar-inner,.navbar-fixed-bottom .navbar-inner{padding:5px} .navbar .container{width:auto;padding:0} .navbar .brand{padding-left:10px;padding-right:10px;margin:0 0 0 -5px} .nav-collapse{clear:both} .nav-collapse .nav{float:none;margin:0 0 10px} .nav-collapse .nav>li{float:none} .nav-collapse .nav>li>a{margin-bottom:2px} .nav-collapse .nav>.divider-vertical{display:none} .nav-collapse .nav .nav-header{color:#777;text-shadow:none} .nav-collapse .nav>li>a,.nav-collapse .dropdown-menu a{padding:9px 15px;font-weight:bold;color:#777;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px} .nav-collapse .btn{padding:4px 10px 4px;font-weight:normal;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px} .nav-collapse .dropdown-menu li+li a{margin-bottom:2px} .nav-collapse .nav>li>a:hover,.nav-collapse .nav>li>a:focus,.nav-collapse .dropdown-menu a:hover,.nav-collapse .dropdown-menu a:focus{background-color:#f2f2f2} .navbar-inverse .nav-collapse .nav>li>a,.navbar-inverse .nav-collapse .dropdown-menu a{color:#999} .navbar-inverse .nav-collapse .nav>li>a:hover,.navbar-inverse .nav-collapse .nav>li>a:focus,.navbar-inverse .nav-collapse .dropdown-menu a:hover,.navbar-inverse .nav-collapse .dropdown-menu a:focus{background-color:#111} .nav-collapse.in .btn-group{margin-top:5px;padding:0} .nav-collapse .dropdown-menu{position:static;top:auto;left:auto;float:none;display:none;max-width:none;margin:0 15px;padding:0;background-color:transparent;border:none;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none} .nav-collapse .open>.dropdown-menu{display:block} .nav-collapse .dropdown-menu:before,.nav-collapse .dropdown-menu:after{display:none} .nav-collapse .dropdown-menu .divider{display:none} .nav-collapse .nav>li>.dropdown-menu:before,.nav-collapse .nav>li>.dropdown-menu:after{display:none} .nav-collapse .navbar-form,.nav-collapse .navbar-search{float:none;padding:10px 15px;margin:10px 0;border-top:1px solid #f2f2f2;border-bottom:1px solid #f2f2f2;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1)} .navbar-inverse .nav-collapse .navbar-form,.navbar-inverse .nav-collapse .navbar-search{border-top-color:#111;border-bottom-color:#111} .navbar .nav-collapse .nav.pull-right{float:none;margin-left:0} .nav-collapse,.nav-collapse.collapse{overflow:hidden;height:0} .navbar .btn-navbar{display:block} .navbar-static .navbar-inner{padding-left:10px;padding-right:10px}}@media (min-width:979px + 1){.nav-collapse.collapse{height:auto !important;overflow:visible !important}}@font-face{font-family:'FontAwesome';src:url('../components/font-awesome/font/fontawesome-webfont.eot?v=3.2.1');src:url('../components/font-awesome/font/fontawesome-webfont.eot?#iefix&v=3.2.1') format('embedded-opentype'),url('../components/font-awesome/font/fontawesome-webfont.woff?v=3.2.1') format('woff'),url('../components/font-awesome/font/fontawesome-webfont.ttf?v=3.2.1') format('truetype'),url('../components/font-awesome/font/fontawesome-webfont.svg#fontawesomeregular?v=3.2.1') format('svg');font-weight:normal;font-style:normal}[class^="icon-"],[class*=" icon-"]{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em}
[class^="icon-"]:before,[class*=" icon-"]:before{text-decoration:inherit;display:inline-block;speak:none}
.icon-large:before{vertical-align:-10%;font-size:1.3333333333333333em}
a [class^="icon-"],a [class*=" icon-"]{display:inline}
[class^="icon-"].icon-fixed-width,[class*=" icon-"].icon-fixed-width{display:inline-block;width:1.1428571428571428em;text-align:right;padding-right:.2857142857142857em}[class^="icon-"].icon-fixed-width.icon-large,[class*=" icon-"].icon-fixed-width.icon-large{width:1.4285714285714286em}
.icons-ul{margin-left:2.142857142857143em;list-style-type:none}.icons-ul>li{position:relative}
.icons-ul .icon-li{position:absolute;left:-2.142857142857143em;width:2.142857142857143em;text-align:center;line-height:inherit}
[class^="icon-"].hide,[class*=" icon-"].hide{display:none}
.icon-muted{color:#eee}
.icon-light{color:#fff}
.icon-dark{color:#333}
.icon-border{border:solid 1px #eee;padding:.2em .25em .15em;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.icon-2x{font-size:2em}.icon-2x.icon-border{border-width:2px;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.icon-3x{font-size:3em}.icon-3x.icon-border{border-width:3px;border-radius:5px;-webkit-border-radius:5px;-moz-border-radius:5px;border-radius:5px}
.icon-4x{font-size:4em}.icon-4x.icon-border{border-width:4px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.icon-5x{font-size:5em}.icon-5x.icon-border{border-width:5px;border-radius:7px;-webkit-border-radius:7px;-moz-border-radius:7px;border-radius:7px}
.pull-right{float:right}
.pull-left{float:left}
[class^="icon-"].pull-left,[class*=" icon-"].pull-left{margin-right:.3em}
[class^="icon-"].pull-right,[class*=" icon-"].pull-right{margin-left:.3em}
[class^="icon-"],[class*=" icon-"]{display:inline;width:auto;height:auto;line-height:normal;vertical-align:baseline;background-image:none;background-position:0 0;background-repeat:repeat;margin-top:0}
.icon-white,.nav-pills>.active>a>[class^="icon-"],.nav-pills>.active>a>[class*=" icon-"],.nav-list>.active>a>[class^="icon-"],.nav-list>.active>a>[class*=" icon-"],.navbar-inverse .nav>.active>a>[class^="icon-"],.navbar-inverse .nav>.active>a>[class*=" icon-"],.dropdown-menu>li>a:hover>[class^="icon-"],.dropdown-menu>li>a:hover>[class*=" icon-"],.dropdown-menu>.active>a>[class^="icon-"],.dropdown-menu>.active>a>[class*=" icon-"],.dropdown-submenu:hover>a>[class^="icon-"],.dropdown-submenu:hover>a>[class*=" icon-"]{background-image:none}
.btn [class^="icon-"].icon-large,.nav [class^="icon-"].icon-large,.btn [class*=" icon-"].icon-large,.nav [class*=" icon-"].icon-large{line-height:.9em}
.btn [class^="icon-"].icon-spin,.nav [class^="icon-"].icon-spin,.btn [class*=" icon-"].icon-spin,.nav [class*=" icon-"].icon-spin{display:inline-block}
.nav-tabs [class^="icon-"],.nav-pills [class^="icon-"],.nav-tabs [class*=" icon-"],.nav-pills [class*=" icon-"],.nav-tabs [class^="icon-"].icon-large,.nav-pills [class^="icon-"].icon-large,.nav-tabs [class*=" icon-"].icon-large,.nav-pills [class*=" icon-"].icon-large{line-height:.9em}
.btn [class^="icon-"].pull-left.icon-2x,.btn [class*=" icon-"].pull-left.icon-2x,.btn [class^="icon-"].pull-right.icon-2x,.btn [class*=" icon-"].pull-right.icon-2x{margin-top:.18em}
.btn [class^="icon-"].icon-spin.icon-large,.btn [class*=" icon-"].icon-spin.icon-large{line-height:.8em}
.btn.btn-small [class^="icon-"].pull-left.icon-2x,.btn.btn-small [class*=" icon-"].pull-left.icon-2x,.btn.btn-small [class^="icon-"].pull-right.icon-2x,.btn.btn-small [class*=" icon-"].pull-right.icon-2x{margin-top:.25em}
.btn.btn-large [class^="icon-"],.btn.btn-large [class*=" icon-"]{margin-top:0}.btn.btn-large [class^="icon-"].pull-left.icon-2x,.btn.btn-large [class*=" icon-"].pull-left.icon-2x,.btn.btn-large [class^="icon-"].pull-right.icon-2x,.btn.btn-large [class*=" icon-"].pull-right.icon-2x{margin-top:.05em}
.btn.btn-large [class^="icon-"].pull-left.icon-2x,.btn.btn-large [class*=" icon-"].pull-left.icon-2x{margin-right:.2em}
.btn.btn-large [class^="icon-"].pull-right.icon-2x,.btn.btn-large [class*=" icon-"].pull-right.icon-2x{margin-left:.2em}
.nav-list [class^="icon-"],.nav-list [class*=" icon-"]{line-height:inherit}
.icon-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:-35%}.icon-stack [class^="icon-"],.icon-stack [class*=" icon-"]{display:block;text-align:center;position:absolute;width:100%;height:100%;font-size:1em;line-height:inherit;*line-height:2em}
.icon-stack .icon-stack-base{font-size:2em;*line-height:1em}
.icon-spin{display:inline-block;-moz-animation:spin 2s infinite linear;-o-animation:spin 2s infinite linear;-webkit-animation:spin 2s infinite linear;animation:spin 2s infinite linear}
a .icon-stack,a .icon-spin{display:inline-block;text-decoration:none}
@-moz-keyframes spin{0%{-moz-transform:rotate(0deg)} 100%{-moz-transform:rotate(359deg)}}@-webkit-keyframes spin{0%{-webkit-transform:rotate(0deg)} 100%{-webkit-transform:rotate(359deg)}}@-o-keyframes spin{0%{-o-transform:rotate(0deg)} 100%{-o-transform:rotate(359deg)}}@-ms-keyframes spin{0%{-ms-transform:rotate(0deg)} 100%{-ms-transform:rotate(359deg)}}@keyframes spin{0%{transform:rotate(0deg)} 100%{transform:rotate(359deg)}}.icon-rotate-90:before{-webkit-transform:rotate(90deg);-moz-transform:rotate(90deg);-ms-transform:rotate(90deg);-o-transform:rotate(90deg);transform:rotate(90deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=1)}
.icon-rotate-180:before{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);-o-transform:rotate(180deg);transform:rotate(180deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2)}
.icon-rotate-270:before{-webkit-transform:rotate(270deg);-moz-transform:rotate(270deg);-ms-transform:rotate(270deg);-o-transform:rotate(270deg);transform:rotate(270deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3)}
.icon-flip-horizontal:before{-webkit-transform:scale(-1, 1);-moz-transform:scale(-1, 1);-ms-transform:scale(-1, 1);-o-transform:scale(-1, 1);transform:scale(-1, 1)}
.icon-flip-vertical:before{-webkit-transform:scale(1, -1);-moz-transform:scale(1, -1);-ms-transform:scale(1, -1);-o-transform:scale(1, -1);transform:scale(1, -1)}
a .icon-rotate-90:before,a .icon-rotate-180:before,a .icon-rotate-270:before,a .icon-flip-horizontal:before,a .icon-flip-vertical:before{display:inline-block}
.icon-glass:before{content:"\f000"}
.icon-music:before{content:"\f001"}
.icon-search:before{content:"\f002"}
.icon-envelope-alt:before{content:"\f003"}
.icon-heart:before{content:"\f004"}
.icon-star:before{content:"\f005"}
.icon-star-empty:before{content:"\f006"}
.icon-user:before{content:"\f007"}
.icon-film:before{content:"\f008"}
.icon-th-large:before{content:"\f009"}
.icon-th:before{content:"\f00a"}
.icon-th-list:before{content:"\f00b"}
.icon-ok:before{content:"\f00c"}
.icon-remove:before{content:"\f00d"}
.icon-zoom-in:before{content:"\f00e"}
.icon-zoom-out:before{content:"\f010"}
.icon-power-off:before,.icon-off:before{content:"\f011"}
.icon-signal:before{content:"\f012"}
.icon-gear:before,.icon-cog:before{content:"\f013"}
.icon-trash:before{content:"\f014"}
.icon-home:before{content:"\f015"}
.icon-file-alt:before{content:"\f016"}
.icon-time:before{content:"\f017"}
.icon-road:before{content:"\f018"}
.icon-download-alt:before{content:"\f019"}
.icon-download:before{content:"\f01a"}
.icon-upload:before{content:"\f01b"}
.icon-inbox:before{content:"\f01c"}
.icon-play-circle:before{content:"\f01d"}
.icon-rotate-right:before,.icon-repeat:before{content:"\f01e"}
.icon-refresh:before{content:"\f021"}
.icon-list-alt:before{content:"\f022"}
.icon-lock:before{content:"\f023"}
.icon-flag:before{content:"\f024"}
.icon-headphones:before{content:"\f025"}
.icon-volume-off:before{content:"\f026"}
.icon-volume-down:before{content:"\f027"}
.icon-volume-up:before{content:"\f028"}
.icon-qrcode:before{content:"\f029"}
.icon-barcode:before{content:"\f02a"}
.icon-tag:before{content:"\f02b"}
.icon-tags:before{content:"\f02c"}
.icon-book:before{content:"\f02d"}
.icon-bookmark:before{content:"\f02e"}
.icon-print:before{content:"\f02f"}
.icon-camera:before{content:"\f030"}
.icon-font:before{content:"\f031"}
.icon-bold:before{content:"\f032"}
.icon-italic:before{content:"\f033"}
.icon-text-height:before{content:"\f034"}
.icon-text-width:before{content:"\f035"}
.icon-align-left:before{content:"\f036"}
.icon-align-center:before{content:"\f037"}
.icon-align-right:before{content:"\f038"}
.icon-align-justify:before{content:"\f039"}
.icon-list:before{content:"\f03a"}
.icon-indent-left:before{content:"\f03b"}
.icon-indent-right:before{content:"\f03c"}
.icon-facetime-video:before{content:"\f03d"}
.icon-picture:before{content:"\f03e"}
.icon-pencil:before{content:"\f040"}
.icon-map-marker:before{content:"\f041"}
.icon-adjust:before{content:"\f042"}
.icon-tint:before{content:"\f043"}
.icon-edit:before{content:"\f044"}
.icon-share:before{content:"\f045"}
.icon-check:before{content:"\f046"}
.icon-move:before{content:"\f047"}
.icon-step-backward:before{content:"\f048"}
.icon-fast-backward:before{content:"\f049"}
.icon-backward:before{content:"\f04a"}
.icon-play:before{content:"\f04b"}
.icon-pause:before{content:"\f04c"}
.icon-stop:before{content:"\f04d"}
.icon-forward:before{content:"\f04e"}
.icon-fast-forward:before{content:"\f050"}
.icon-step-forward:before{content:"\f051"}
.icon-eject:before{content:"\f052"}
.icon-chevron-left:before{content:"\f053"}
.icon-chevron-right:before{content:"\f054"}
.icon-plus-sign:before{content:"\f055"}
.icon-minus-sign:before{content:"\f056"}
.icon-remove-sign:before{content:"\f057"}
.icon-ok-sign:before{content:"\f058"}
.icon-question-sign:before{content:"\f059"}
.icon-info-sign:before{content:"\f05a"}
.icon-screenshot:before{content:"\f05b"}
.icon-remove-circle:before{content:"\f05c"}
.icon-ok-circle:before{content:"\f05d"}
.icon-ban-circle:before{content:"\f05e"}
.icon-arrow-left:before{content:"\f060"}
.icon-arrow-right:before{content:"\f061"}
.icon-arrow-up:before{content:"\f062"}
.icon-arrow-down:before{content:"\f063"}
.icon-mail-forward:before,.icon-share-alt:before{content:"\f064"}
.icon-resize-full:before{content:"\f065"}
.icon-resize-small:before{content:"\f066"}
.icon-plus:before{content:"\f067"}
.icon-minus:before{content:"\f068"}
.icon-asterisk:before{content:"\f069"}
.icon-exclamation-sign:before{content:"\f06a"}
.icon-gift:before{content:"\f06b"}
.icon-leaf:before{content:"\f06c"}
.icon-fire:before{content:"\f06d"}
.icon-eye-open:before{content:"\f06e"}
.icon-eye-close:before{content:"\f070"}
.icon-warning-sign:before{content:"\f071"}
.icon-plane:before{content:"\f072"}
.icon-calendar:before{content:"\f073"}
.icon-random:before{content:"\f074"}
.icon-comment:before{content:"\f075"}
.icon-magnet:before{content:"\f076"}
.icon-chevron-up:before{content:"\f077"}
.icon-chevron-down:before{content:"\f078"}
.icon-retweet:before{content:"\f079"}
.icon-shopping-cart:before{content:"\f07a"}
.icon-folder-close:before{content:"\f07b"}
.icon-folder-open:before{content:"\f07c"}
.icon-resize-vertical:before{content:"\f07d"}
.icon-resize-horizontal:before{content:"\f07e"}
.icon-bar-chart:before{content:"\f080"}
.icon-twitter-sign:before{content:"\f081"}
.icon-facebook-sign:before{content:"\f082"}
.icon-camera-retro:before{content:"\f083"}
.icon-key:before{content:"\f084"}
.icon-gears:before,.icon-cogs:before{content:"\f085"}
.icon-comments:before{content:"\f086"}
.icon-thumbs-up-alt:before{content:"\f087"}
.icon-thumbs-down-alt:before{content:"\f088"}
.icon-star-half:before{content:"\f089"}
.icon-heart-empty:before{content:"\f08a"}
.icon-signout:before{content:"\f08b"}
.icon-linkedin-sign:before{content:"\f08c"}
.icon-pushpin:before{content:"\f08d"}
.icon-external-link:before{content:"\f08e"}
.icon-signin:before{content:"\f090"}
.icon-trophy:before{content:"\f091"}
.icon-github-sign:before{content:"\f092"}
.icon-upload-alt:before{content:"\f093"}
.icon-lemon:before{content:"\f094"}
.icon-phone:before{content:"\f095"}
.icon-unchecked:before,.icon-check-empty:before{content:"\f096"}
.icon-bookmark-empty:before{content:"\f097"}
.icon-phone-sign:before{content:"\f098"}
.icon-twitter:before{content:"\f099"}
.icon-facebook:before{content:"\f09a"}
.icon-github:before{content:"\f09b"}
.icon-unlock:before{content:"\f09c"}
.icon-credit-card:before{content:"\f09d"}
.icon-rss:before{content:"\f09e"}
.icon-hdd:before{content:"\f0a0"}
.icon-bullhorn:before{content:"\f0a1"}
.icon-bell:before{content:"\f0a2"}
.icon-certificate:before{content:"\f0a3"}
.icon-hand-right:before{content:"\f0a4"}
.icon-hand-left:before{content:"\f0a5"}
.icon-hand-up:before{content:"\f0a6"}
.icon-hand-down:before{content:"\f0a7"}
.icon-circle-arrow-left:before{content:"\f0a8"}
.icon-circle-arrow-right:before{content:"\f0a9"}
.icon-circle-arrow-up:before{content:"\f0aa"}
.icon-circle-arrow-down:before{content:"\f0ab"}
.icon-globe:before{content:"\f0ac"}
.icon-wrench:before{content:"\f0ad"}
.icon-tasks:before{content:"\f0ae"}
.icon-filter:before{content:"\f0b0"}
.icon-briefcase:before{content:"\f0b1"}
.icon-fullscreen:before{content:"\f0b2"}
.icon-group:before{content:"\f0c0"}
.icon-link:before{content:"\f0c1"}
.icon-cloud:before{content:"\f0c2"}
.icon-beaker:before{content:"\f0c3"}
.icon-cut:before{content:"\f0c4"}
.icon-copy:before{content:"\f0c5"}
.icon-paperclip:before,.icon-paper-clip:before{content:"\f0c6"}
.icon-save:before{content:"\f0c7"}
.icon-sign-blank:before{content:"\f0c8"}
.icon-reorder:before{content:"\f0c9"}
.icon-list-ul:before{content:"\f0ca"}
.icon-list-ol:before{content:"\f0cb"}
.icon-strikethrough:before{content:"\f0cc"}
.icon-underline:before{content:"\f0cd"}
.icon-table:before{content:"\f0ce"}
.icon-magic:before{content:"\f0d0"}
.icon-truck:before{content:"\f0d1"}
.icon-pinterest:before{content:"\f0d2"}
.icon-pinterest-sign:before{content:"\f0d3"}
.icon-google-plus-sign:before{content:"\f0d4"}
.icon-google-plus:before{content:"\f0d5"}
.icon-money:before{content:"\f0d6"}
.icon-caret-down:before{content:"\f0d7"}
.icon-caret-up:before{content:"\f0d8"}
.icon-caret-left:before{content:"\f0d9"}
.icon-caret-right:before{content:"\f0da"}
.icon-columns:before{content:"\f0db"}
.icon-sort:before{content:"\f0dc"}
.icon-sort-down:before{content:"\f0dd"}
.icon-sort-up:before{content:"\f0de"}
.icon-envelope:before{content:"\f0e0"}
.icon-linkedin:before{content:"\f0e1"}
.icon-rotate-left:before,.icon-undo:before{content:"\f0e2"}
.icon-legal:before{content:"\f0e3"}
.icon-dashboard:before{content:"\f0e4"}
.icon-comment-alt:before{content:"\f0e5"}
.icon-comments-alt:before{content:"\f0e6"}
.icon-bolt:before{content:"\f0e7"}
.icon-sitemap:before{content:"\f0e8"}
.icon-umbrella:before{content:"\f0e9"}
.icon-paste:before{content:"\f0ea"}
.icon-lightbulb:before{content:"\f0eb"}
.icon-exchange:before{content:"\f0ec"}
.icon-cloud-download:before{content:"\f0ed"}
.icon-cloud-upload:before{content:"\f0ee"}
.icon-user-md:before{content:"\f0f0"}
.icon-stethoscope:before{content:"\f0f1"}
.icon-suitcase:before{content:"\f0f2"}
.icon-bell-alt:before{content:"\f0f3"}
.icon-coffee:before{content:"\f0f4"}
.icon-food:before{content:"\f0f5"}
.icon-file-text-alt:before{content:"\f0f6"}
.icon-building:before{content:"\f0f7"}
.icon-hospital:before{content:"\f0f8"}
.icon-ambulance:before{content:"\f0f9"}
.icon-medkit:before{content:"\f0fa"}
.icon-fighter-jet:before{content:"\f0fb"}
.icon-beer:before{content:"\f0fc"}
.icon-h-sign:before{content:"\f0fd"}
.icon-plus-sign-alt:before{content:"\f0fe"}
.icon-double-angle-left:before{content:"\f100"}
.icon-double-angle-right:before{content:"\f101"}
.icon-double-angle-up:before{content:"\f102"}
.icon-double-angle-down:before{content:"\f103"}
.icon-angle-left:before{content:"\f104"}
.icon-angle-right:before{content:"\f105"}
.icon-angle-up:before{content:"\f106"}
.icon-angle-down:before{content:"\f107"}
.icon-desktop:before{content:"\f108"}
.icon-laptop:before{content:"\f109"}
.icon-tablet:before{content:"\f10a"}
.icon-mobile-phone:before{content:"\f10b"}
.icon-circle-blank:before{content:"\f10c"}
.icon-quote-left:before{content:"\f10d"}
.icon-quote-right:before{content:"\f10e"}
.icon-spinner:before{content:"\f110"}
.icon-circle:before{content:"\f111"}
.icon-mail-reply:before,.icon-reply:before{content:"\f112"}
.icon-github-alt:before{content:"\f113"}
.icon-folder-close-alt:before{content:"\f114"}
.icon-folder-open-alt:before{content:"\f115"}
.icon-expand-alt:before{content:"\f116"}
.icon-collapse-alt:before{content:"\f117"}
.icon-smile:before{content:"\f118"}
.icon-frown:before{content:"\f119"}
.icon-meh:before{content:"\f11a"}
.icon-gamepad:before{content:"\f11b"}
.icon-keyboard:before{content:"\f11c"}
.icon-flag-alt:before{content:"\f11d"}
.icon-flag-checkered:before{content:"\f11e"}
.icon-terminal:before{content:"\f120"}
.icon-code:before{content:"\f121"}
.icon-reply-all:before{content:"\f122"}
.icon-mail-reply-all:before{content:"\f122"}
.icon-star-half-full:before,.icon-star-half-empty:before{content:"\f123"}
.icon-location-arrow:before{content:"\f124"}
.icon-crop:before{content:"\f125"}
.icon-code-fork:before{content:"\f126"}
.icon-unlink:before{content:"\f127"}
.icon-question:before{content:"\f128"}
.icon-info:before{content:"\f129"}
.icon-exclamation:before{content:"\f12a"}
.icon-superscript:before{content:"\f12b"}
.icon-subscript:before{content:"\f12c"}
.icon-eraser:before{content:"\f12d"}
.icon-puzzle-piece:before{content:"\f12e"}
.icon-microphone:before{content:"\f130"}
.icon-microphone-off:before{content:"\f131"}
.icon-shield:before{content:"\f132"}
.icon-calendar-empty:before{content:"\f133"}
.icon-fire-extinguisher:before{content:"\f134"}
.icon-rocket:before{content:"\f135"}
.icon-maxcdn:before{content:"\f136"}
.icon-chevron-sign-left:before{content:"\f137"}
.icon-chevron-sign-right:before{content:"\f138"}
.icon-chevron-sign-up:before{content:"\f139"}
.icon-chevron-sign-down:before{content:"\f13a"}
.icon-html5:before{content:"\f13b"}
.icon-css3:before{content:"\f13c"}
.icon-anchor:before{content:"\f13d"}
.icon-unlock-alt:before{content:"\f13e"}
.icon-bullseye:before{content:"\f140"}
.icon-ellipsis-horizontal:before{content:"\f141"}
.icon-ellipsis-vertical:before{content:"\f142"}
.icon-rss-sign:before{content:"\f143"}
.icon-play-sign:before{content:"\f144"}
.icon-ticket:before{content:"\f145"}
.icon-minus-sign-alt:before{content:"\f146"}
.icon-check-minus:before{content:"\f147"}
.icon-level-up:before{content:"\f148"}
.icon-level-down:before{content:"\f149"}
.icon-check-sign:before{content:"\f14a"}
.icon-edit-sign:before{content:"\f14b"}
.icon-external-link-sign:before{content:"\f14c"}
.icon-share-sign:before{content:"\f14d"}
.icon-compass:before{content:"\f14e"}
.icon-collapse:before{content:"\f150"}
.icon-collapse-top:before{content:"\f151"}
.icon-expand:before{content:"\f152"}
.icon-euro:before,.icon-eur:before{content:"\f153"}
.icon-gbp:before{content:"\f154"}
.icon-dollar:before,.icon-usd:before{content:"\f155"}
.icon-rupee:before,.icon-inr:before{content:"\f156"}
.icon-yen:before,.icon-jpy:before{content:"\f157"}
.icon-renminbi:before,.icon-cny:before{content:"\f158"}
.icon-won:before,.icon-krw:before{content:"\f159"}
.icon-bitcoin:before,.icon-btc:before{content:"\f15a"}
.icon-file:before{content:"\f15b"}
.icon-file-text:before{content:"\f15c"}
.icon-sort-by-alphabet:before{content:"\f15d"}
.icon-sort-by-alphabet-alt:before{content:"\f15e"}
.icon-sort-by-attributes:before{content:"\f160"}
.icon-sort-by-attributes-alt:before{content:"\f161"}
.icon-sort-by-order:before{content:"\f162"}
.icon-sort-by-order-alt:before{content:"\f163"}
.icon-thumbs-up:before{content:"\f164"}
.icon-thumbs-down:before{content:"\f165"}
.icon-youtube-sign:before{content:"\f166"}
.icon-youtube:before{content:"\f167"}
.icon-xing:before{content:"\f168"}
.icon-xing-sign:before{content:"\f169"}
.icon-youtube-play:before{content:"\f16a"}
.icon-dropbox:before{content:"\f16b"}
.icon-stackexchange:before{content:"\f16c"}
.icon-instagram:before{content:"\f16d"}
.icon-flickr:before{content:"\f16e"}
.icon-adn:before{content:"\f170"}
.icon-bitbucket:before{content:"\f171"}
.icon-bitbucket-sign:before{content:"\f172"}
.icon-tumblr:before{content:"\f173"}
.icon-tumblr-sign:before{content:"\f174"}
.icon-long-arrow-down:before{content:"\f175"}
.icon-long-arrow-up:before{content:"\f176"}
.icon-long-arrow-left:before{content:"\f177"}
.icon-long-arrow-right:before{content:"\f178"}
.icon-apple:before{content:"\f179"}
.icon-windows:before{content:"\f17a"}
.icon-android:before{content:"\f17b"}
.icon-linux:before{content:"\f17c"}
.icon-dribbble:before{content:"\f17d"}
.icon-skype:before{content:"\f17e"}
.icon-foursquare:before{content:"\f180"}
.icon-trello:before{content:"\f181"}
.icon-female:before{content:"\f182"}
.icon-male:before{content:"\f183"}
.icon-gittip:before{content:"\f184"}
.icon-sun:before{content:"\f185"}
.icon-moon:before{content:"\f186"}
.icon-archive:before{content:"\f187"}
.icon-bug:before{content:"\f188"}
.icon-vk:before{content:"\f189"}
.icon-weibo:before{content:"\f18a"}
.icon-renren:before{content:"\f18b"}
code{color:#000}
pre{font-size:inherit;line-height:inherit}
.border-box-sizing{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}
.corner-all{border-radius:4px}
.hbox{display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.hbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}
.vbox{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
.vbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}
.hbox.reverse,.vbox.reverse,.reverse{-webkit-box-direction:reverse;-moz-box-direction:reverse;box-direction:reverse;flex-direction:row-reverse}
.hbox.box-flex0,.vbox.box-flex0,.box-flex0{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none;width:auto}
.hbox.box-flex1,.vbox.box-flex1,.box-flex1{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
.hbox.box-flex,.vbox.box-flex,.box-flex{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
.hbox.box-flex2,.vbox.box-flex2,.box-flex2{-webkit-box-flex:2;-moz-box-flex:2;box-flex:2;flex:2}
.box-group1{-webkit-box-flex-group:1;-moz-box-flex-group:1;box-flex-group:1}
.box-group2{-webkit-box-flex-group:2;-moz-box-flex-group:2;box-flex-group:2}
.hbox.start,.vbox.start,.start{-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start}
.hbox.end,.vbox.end,.end{-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;justify-content:flex-end}
.hbox.center,.vbox.center,.center{-webkit-box-pack:center;-moz-box-pack:center;box-pack:center;justify-content:center}
.hbox.align-start,.vbox.align-start,.align-start{-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.hbox.align-end,.vbox.align-end,.align-end{-webkit-box-align:end;-moz-box-align:end;box-align:end;align-items:flex-end}
.hbox.align-center,.vbox.align-center,.align-center{-webkit-box-align:center;-moz-box-align:center;box-align:center;align-items:center}
div.error{margin:2em;text-align:center}
div.error>h1{font-size:500%;line-height:normal}
div.error>p{font-size:200%;line-height:normal}
div.traceback-wrapper{text-align:left;max-width:800px;margin:auto}
body{background-color:#fff;position:absolute;left:0;right:0;top:0;bottom:0;overflow:visible}
div#header{display:none}
#ipython_notebook{padding-left:16px}
#noscript{width:auto;padding-top:16px;padding-bottom:16px;text-align:center;font-size:22px;color:#f00;font-weight:bold}
#ipython_notebook img{font-family:Verdana,"Helvetica Neue",Arial,Helvetica,Geneva,sans-serif;height:24px;text-decoration:none;color:#000}
#site{width:100%;display:none}
.ui-button .ui-button-text{padding:.2em .8em;font-size:77%}
input.ui-button{padding:.3em .9em}
.navbar span{margin-top:3px}
span#login_widget{float:right}
.nav-header{text-transform:none}
.navbar-nobg{background-color:transparent;background-image:none}
#header>span{margin-top:10px}
.modal_stretch{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;height:80%}.modal_stretch .modal-body{max-height:none;flex:1}
@media (min-width:768px){.modal{width:700px;margin-left:-350px}}.center-nav{display:inline-block;margin-bottom:-4px}
.alternate_upload{background-color:none;display:inline}
.alternate_upload.form{padding:0;margin:0}
.alternate_upload input.fileinput{background-color:#f00;position:relative;opacity:0;z-index:2;width:295px;margin-left:163px;cursor:pointer;height:26px}
ul#tabs{margin-bottom:4px}
ul#tabs a{padding-top:4px;padding-bottom:4px}
ul.breadcrumb a:focus,ul.breadcrumb a:hover{text-decoration:none}
ul.breadcrumb i.icon-home{font-size:16px;margin-right:4px}
ul.breadcrumb span{color:#5e5e5e}
.list_toolbar{padding:4px 0 4px 0}
.list_toolbar [class*="span"]{min-height:26px}
.list_header{font-weight:bold}
.list_container{margin-top:4px;margin-bottom:20px;border:1px solid #ababab;border-radius:4px}
.list_container>div{border-bottom:1px solid #ababab}.list_container>div:hover .list-item{background-color:#f00}
.list_container>div:last-child{border:none}
.list_item:hover .list_item{background-color:#ddd}
.list_item a{text-decoration:none}
.list_header>div,.list_item>div{padding-top:4px;padding-bottom:4px;padding-left:7px;padding-right:7px;height:22px;line-height:22px}
.item_name{line-height:22px;height:26px}
.item_icon{font-size:14px;color:#5e5e5e;margin-right:7px}
.item_buttons{line-height:1em}
.toolbar_info{height:26px;line-height:26px}
input.nbname_input,input.engine_num_input{padding-top:3px;padding-bottom:3px;height:14px;line-height:14px;margin:0}
input.engine_num_input{width:60px}
.highlight_text{color:#00f}
#project_name>.breadcrumb{padding:0;margin-bottom:0;background-color:transparent;font-weight:bold}
.folder_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f114"}
.notebook_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f02d"}
.ansibold{font-weight:bold}
.ansiblack{color:#000}
.ansired{color:#8b0000}
.ansigreen{color:#006400}
.ansiyellow{color:#a52a2a}
.ansiblue{color:#00008b}
.ansipurple{color:#9400d3}
.ansicyan{color:#4682b4}
.ansigray{color:#808080}
.ansibgblack{background-color:#000}
.ansibgred{background-color:#f00}
.ansibggreen{background-color:#008000}
.ansibgyellow{background-color:#ff0}
.ansibgblue{background-color:#00f}
.ansibgpurple{background-color:#f0f}
.ansibgcyan{background-color:#0ff}
.ansibggray{background-color:#808080}
div.cell{border:1px solid transparent;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}div.cell.selected{border-radius:4px;border:thin #ababab solid}
div.cell.edit_mode{border-radius:4px;border:thin #008000 solid}
div.cell{width:100%;padding:5px 5px 5px 0;margin:0;outline:none}
div.prompt{min-width:11ex;padding:.4em;margin:0;font-family:monospace;text-align:right;line-height:1.21429em}
@media (max-width:480px){div.prompt{text-align:left}}div.inner_cell{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
div.input_area{border:1px solid #cfcfcf;border-radius:4px;background:#f7f7f7;line-height:1.21429em}
div.prompt:empty{padding-top:0;padding-bottom:0}
div.input{page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
@media (max-width:480px){div.input{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.input_prompt{color:#000080;border-top:1px solid transparent}
div.input_area>div.highlight{margin:.4em;border:none;padding:0;background-color:transparent}
div.input_area>div.highlight>pre{margin:0;border:none;padding:0;background-color:transparent}
.CodeMirror{line-height:1.21429em;height:auto;background:none;}
.CodeMirror-scroll{overflow-y:hidden;overflow-x:auto}
.CodeMirror-lines{padding:.4em}
.CodeMirror-linenumber{padding:0 8px 0 4px}
.CodeMirror-gutters{border-bottom-left-radius:4px;border-top-left-radius:4px}
.CodeMirror pre{padding:0;border:0;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
pre code{display:block;padding:.5em}
.highlight-base,pre code,pre .subst,pre .tag .title,pre .lisp .title,pre .clojure .built_in,pre .nginx .title{color:#000}
.highlight-string,pre .string,pre .constant,pre .parent,pre .tag .value,pre .rules .value,pre .rules .value .number,pre .preprocessor,pre .ruby .symbol,pre .ruby .symbol .string,pre .aggregate,pre .template_tag,pre .django .variable,pre .smalltalk .class,pre .addition,pre .flow,pre .stream,pre .bash .variable,pre .apache .tag,pre .apache .cbracket,pre .tex .command,pre .tex .special,pre .erlang_repl .function_or_atom,pre .markdown .header{color:#ba2121}
.highlight-comment,pre .comment,pre .annotation,pre .template_comment,pre .diff .header,pre .chunk,pre .markdown .blockquote{color:#408080;font-style:italic}
.highlight-number,pre .number,pre .date,pre .regexp,pre .literal,pre .smalltalk .symbol,pre .smalltalk .char,pre .go .constant,pre .change,pre .markdown .bullet,pre .markdown .link_url{color:#080}
pre .label,pre .javadoc,pre .ruby .string,pre .decorator,pre .filter .argument,pre .localvars,pre .array,pre .attr_selector,pre .important,pre .pseudo,pre .pi,pre .doctype,pre .deletion,pre .envvar,pre .shebang,pre .apache .sqbracket,pre .nginx .built_in,pre .tex .formula,pre .erlang_repl .reserved,pre .prompt,pre .markdown .link_label,pre .vhdl .attribute,pre .clojure .attribute,pre .coffeescript .property{color:#88f}
.highlight-keyword,pre .keyword,pre .id,pre .phpdoc,pre .aggregate,pre .css .tag,pre .javadoctag,pre .phpdoc,pre .yardoctag,pre .smalltalk .class,pre .winutils,pre .bash .variable,pre .apache .tag,pre .go .typename,pre .tex .command,pre .markdown .strong,pre .request,pre .status{color:#008000;font-weight:bold}
.highlight-builtin,pre .built_in{color:#008000}
pre .markdown .emphasis{font-style:italic}
pre .nginx .built_in{font-weight:normal}
pre .coffeescript .javascript,pre .javascript .xml,pre .tex .formula,pre .xml .javascript,pre .xml .vbscript,pre .xml .css,pre .xml .cdata{opacity:.5}
.cm-s-ipython span.cm-variable{color:#000}
.cm-s-ipython span.cm-keyword{color:#008000;font-weight:bold}
.cm-s-ipython span.cm-number{color:#080}
.cm-s-ipython span.cm-comment{color:#408080;font-style:italic}
.cm-s-ipython span.cm-string{color:#ba2121}
.cm-s-ipython span.cm-builtin{color:#008000}
.cm-s-ipython span.cm-error{color:#f00}
.cm-s-ipython span.cm-operator{color:#a2f;font-weight:bold}
.cm-s-ipython span.cm-meta{color:#a2f}
.cm-s-ipython span.cm-tab{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);background-position:right;background-repeat:no-repeat}
div.output_wrapper{position:relative;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
div.output_scroll{height:24em;width:100%;overflow:auto;border-radius:4px;-webkit-box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);-moz-box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);display:block}
div.output_collapsed{margin:0;padding:0;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
div.out_prompt_overlay{height:100%;padding:0 .4em;position:absolute;border-radius:4px}
div.out_prompt_overlay:hover{-webkit-box-shadow:inset 0 0 1px #000;-moz-box-shadow:inset 0 0 1px #000;box-shadow:inset 0 0 1px #000;background:rgba(240,240,240,0.5)}
div.output_prompt{color:#8b0000}
div.output_area{padding:0;page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}div.output_area .MathJax_Display{text-align:left !important}
div.output_area .rendered_html table{margin-left:0;margin-right:0}
div.output_area .rendered_html img{margin-left:0;margin-right:0}
.output{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
@media (max-width:480px){div.output_area{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.output_area pre{margin:0;padding:0;border:0;vertical-align:baseline;color:#000;background-color:transparent;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
div.output_subarea{padding:.4em .4em 0 .4em;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
div.output_text{text-align:left;color:#000;line-height:1.21429em}
div.output_stderr{background:#fdd;}
div.output_latex{text-align:left}
div.output_javascript:empty{padding:0}
.js-error{color:#8b0000}
div.raw_input_container{font-family:monospace;padding-top:5px}
span.raw_input_prompt{}
input.raw_input{font-family:inherit;font-size:inherit;color:inherit;width:auto;vertical-align:baseline;padding:0 .25em;margin:0 .25em}
input.raw_input:focus{box-shadow:none}
p.p-space{margin-bottom:10px}
.rendered_html{color:#000;}.rendered_html em{font-style:italic}
.rendered_html strong{font-weight:bold}
.rendered_html u{text-decoration:underline}
.rendered_html :link{text-decoration:underline}
.rendered_html :visited{text-decoration:underline}
.rendered_html h1{font-size:185.7%;margin:1.08em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h2{font-size:157.1%;margin:1.27em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h3{font-size:128.6%;margin:1.55em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h4{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h5{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1;font-style:italic}
.rendered_html h6{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1;font-style:italic}
.rendered_html h1:first-child{margin-top:.538em}
.rendered_html h2:first-child{margin-top:.636em}
.rendered_html h3:first-child{margin-top:.777em}
.rendered_html h4:first-child{margin-top:1em}
.rendered_html h5:first-child{margin-top:1em}
.rendered_html h6:first-child{margin-top:1em}
.rendered_html ul{list-style:disc;margin:0 2em}
.rendered_html ul ul{list-style:square;margin:0 2em}
.rendered_html ul ul ul{list-style:circle;margin:0 2em}
.rendered_html ol{list-style:decimal;margin:0 2em}
.rendered_html ol ol{list-style:upper-alpha;margin:0 2em}
.rendered_html ol ol ol{list-style:lower-alpha;margin:0 2em}
.rendered_html ol ol ol ol{list-style:lower-roman;margin:0 2em}
.rendered_html ol ol ol ol ol{list-style:decimal;margin:0 2em}
.rendered_html *+ul{margin-top:1em}
.rendered_html *+ol{margin-top:1em}
.rendered_html hr{color:#000;background-color:#000}
.rendered_html pre{margin:1em 2em}
.rendered_html pre,.rendered_html code{border:0;background-color:#fff;color:#000;font-size:100%;padding:0}
.rendered_html blockquote{margin:1em 2em}
.rendered_html table{margin-left:auto;margin-right:auto;border:1px solid #000;border-collapse:collapse}
.rendered_html tr,.rendered_html th,.rendered_html td{border:1px solid #000;border-collapse:collapse;margin:1em 2em}
.rendered_html td,.rendered_html th{text-align:left;vertical-align:middle;padding:4px}
.rendered_html th{font-weight:bold}
.rendered_html *+table{margin-top:1em}
.rendered_html p{text-align:justify}
.rendered_html *+p{margin-top:1em}
.rendered_html img{display:block;margin-left:auto;margin-right:auto}
.rendered_html *+img{margin-top:1em}
div.text_cell{padding:5px 5px 5px 0;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
@media (max-width:480px){div.text_cell>div.prompt{display:none}}div.text_cell_render{outline:none;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#000}
a.anchor-link:link{text-decoration:none;padding:0 20px;visibility:hidden}
h1:hover .anchor-link,h2:hover .anchor-link,h3:hover .anchor-link,h4:hover .anchor-link,h5:hover .anchor-link,h6:hover .anchor-link{visibility:visible}
div.cell.text_cell.rendered{padding:0}
.widget-area{page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.widget-area .widget-subarea{padding:.44em .4em .4em 1px;margin-left:6px;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:2;-moz-box-flex:2;box-flex:2;flex:2;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-hlabel{min-width:10ex;padding-right:8px;padding-top:3px;text-align:right;vertical-align:text-top}
.widget-vlabel{padding-bottom:5px;text-align:center;vertical-align:text-bottom}
.widget-hreadout{padding-left:8px;padding-top:3px;text-align:left;vertical-align:text-top}
.widget-vreadout{padding-top:5px;text-align:center;vertical-align:text-top}
.slide-track{border:1px solid #ccc;background:#fff;border-radius:4px;}
.widget-hslider{padding-left:8px;padding-right:5px;overflow:visible;width:348px;height:5px;max-height:5px;margin-top:11px;margin-bottom:10px;border:1px solid #ccc;background:#fff;border-radius:4px;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.widget-hslider .ui-slider{border:0 !important;background:none !important;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.widget-hslider .ui-slider .ui-slider-handle{width:14px !important;height:28px !important;margin-top:-8px !important}
.widget-vslider{padding-bottom:8px;overflow:visible;width:5px;max-width:5px;height:250px;margin-left:12px;border:1px solid #ccc;background:#fff;border-radius:4px;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}.widget-vslider .ui-slider{border:0 !important;background:none !important;margin-left:-4px;margin-top:5px;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.widget-vslider .ui-slider .ui-slider-handle{width:28px !important;height:14px !important;margin-left:-9px}
.widget-text{width:350px;margin:0 !important}
.widget-listbox{width:364px;margin-bottom:0}
.widget-numeric-text{width:150px;margin:0 !important}
.widget-progress{width:363px}.widget-progress .bar{-webkit-transition:none;-moz-transition:none;-ms-transition:none;-o-transition:none;transition:none}
.widget-combo-btn{min-width:138px;}
.widget-box{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-hbox{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.widget-hbox-single{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;height:30px}
.widget-vbox{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
.widget-vbox-single{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;width:30px}
.widget-modal{overflow:hidden;position:absolute !important;top:0;left:0;margin-left:0 !important}
.widget-modal-body{max-height:none !important}
.widget-container{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-radio-box{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;padding-top:4px}
.docked-widget-modal{overflow:hidden;position:relative !important;top:0 !important;left:0 !important;margin-left:0 !important}
body{background-color:#fff}
body.notebook_app{overflow:hidden}
@media (max-width:767px){body.notebook_app{padding-left:0;padding-right:0}}span#notebook_name{height:1em;line-height:1em;padding:3px;border:none;font-size:146.5%}
div#notebook_panel{margin:0 0 0 0;padding:0;-webkit-box-shadow:0 -1px 10px rgba(0,0,0,0.1);-moz-box-shadow:0 -1px 10px rgba(0,0,0,0.1);box-shadow:0 -1px 10px rgba(0,0,0,0.1)}
div#notebook{font-size:14px;line-height:20px;overflow-y:scroll;overflow-x:auto;width:100%;padding:1em 0 1em 0;margin:0;border-top:1px solid #ababab;outline:none;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}
div.ui-widget-content{border:1px solid #ababab;outline:none}
pre.dialog{background-color:#f7f7f7;border:1px solid #ddd;border-radius:4px;padding:.4em;padding-left:2em}
p.dialog{padding:.2em}
pre,code,kbd,samp{white-space:pre-wrap}
#fonttest{font-family:monospace}
p{margin-bottom:0}
.end_space{height:200px}
.celltoolbar{border:thin solid #cfcfcf;border-bottom:none;background:#eee;border-radius:3px 3px 0 0;width:100%;-webkit-box-pack:end;height:22px;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;-webkit-box-direction:reverse;-moz-box-direction:reverse;box-direction:reverse;flex-direction:row-reverse}
.ctb_hideshow{display:none;vertical-align:bottom;padding-right:2px}
.celltoolbar>div{padding-top:0}
.ctb_global_show .ctb_show.ctb_hideshow{display:block}
.ctb_global_show .ctb_show+.input_area,.ctb_global_show .ctb_show+div.text_cell_input{border-top-right-radius:0;border-top-left-radius:0}
.celltoolbar .button_container select{margin:10px;margin-top:1px;margin-bottom:0;padding:0;font-size:87%;width:auto;display:inline-block;height:18px;line-height:18px;vertical-align:top}
.celltoolbar label{display:inline-block;height:15px;line-height:15px;vertical-align:top}
.celltoolbar label span{font-size:85%}
.celltoolbar input[type=checkbox]{margin:0;margin-left:4px;margin-right:4px}
.celltoolbar .ui-button{border:none;vertical-align:top;height:20px;min-width:30px}
.completions{position:absolute;z-index:10;overflow:hidden;border:1px solid #ababab;border-radius:4px;-webkit-box-shadow:0 6px 10px -1px #adadad;-moz-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad}
.completions select{background:#fff;outline:none;border:none;padding:0;margin:0;overflow:auto;font-family:monospace;font-size:110%;color:#000;width:auto}
.completions select option.context{color:#0064cd}
#menubar .navbar-inner{min-height:28px;border-top:1px;border-radius:0 0 4px 4px}
#menubar .navbar{margin-bottom:8px}
.nav-wrapper{border-bottom:1px solid #d4d4d4}
#menubar li.dropdown{line-height:12px}
i.menu-icon{padding-top:4px}
ul#help_menu li a{overflow:hidden;padding-right:2.2em}ul#help_menu li a i{margin-right:-1.2em}
#notification_area{z-index:10}
.indicator_area{color:#777;padding:4px 3px;margin:0;width:11px;z-index:10;text-align:center}
#kernel_indicator{margin-right:-16px}
.edit_mode_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f040"}
.command_mode_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:' '}
.kernel_idle_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f10c"}
.kernel_busy_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f111"}
.notification_widget{color:#777;padding:1px 12px;margin:2px 4px;z-index:10;border:1px solid #ccc;border-radius:4px;background:rgba(240,240,240,0.5)}.notification_widget.span{padding-right:2px}
div#pager_splitter{height:8px}
#pager-container{position:relative;padding:15px 0}
div#pager{font-size:14px;line-height:20px;overflow:auto;display:none}div#pager pre{line-height:1.21429em;color:#000;background-color:#f7f7f7;padding:.4em}
.quickhelp{display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.shortcut_key{display:inline-block;width:20ex;text-align:right;font-family:monospace}
.shortcut_descr{display:inline-block;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
span#save_widget{padding:0 5px;margin-top:12px}
span#checkpoint_status,span#autosave_status{font-size:small}
@media (max-width:767px){span#save_widget{font-size:small} span#checkpoint_status,span#autosave_status{font-size:x-small}}@media (max-width:767px){span#checkpoint_status,span#autosave_status{display:none}}@media (min-width:768px) and (max-width:979px){span#checkpoint_status{display:none} span#autosave_status{font-size:x-small}}.toolbar{padding:0 10px;margin-top:-5px}.toolbar select,.toolbar label{width:auto;height:26px;vertical-align:middle;margin-right:2px;margin-bottom:0;display:inline;font-size:92%;margin-left:.3em;margin-right:.3em;padding:0;padding-top:3px}
.toolbar .btn{padding:2px 8px}
.toolbar .btn-group{margin-top:0}
.toolbar-inner{border:none !important;-webkit-box-shadow:none !important;-moz-box-shadow:none !important;box-shadow:none !important}
#maintoolbar{margin-bottom:0}
@-moz-keyframes fadeOut{from{opacity:1} to{opacity:0}}@-webkit-keyframes fadeOut{from{opacity:1} to{opacity:0}}@-moz-keyframes fadeIn{from{opacity:0} to{opacity:1}}@-webkit-keyframes fadeIn{from{opacity:0} to{opacity:1}}.bigtooltip{overflow:auto;height:200px;-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms}
.smalltooltip{-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms;text-overflow:ellipsis;overflow:hidden;height:80px}
.tooltipbuttons{position:absolute;padding-right:15px;top:0;right:0}
.tooltiptext{padding-right:30px}
.ipython_tooltip{max-width:700px;-webkit-animation:fadeOut 400ms;-moz-animation:fadeOut 400ms;animation:fadeOut 400ms;-webkit-animation:fadeIn 400ms;-moz-animation:fadeIn 400ms;animation:fadeIn 400ms;vertical-align:middle;background-color:#f7f7f7;overflow:visible;border:#ababab 1px solid;outline:none;padding:3px;margin:0;padding-left:7px;font-family:monospace;min-height:50px;-moz-box-shadow:0 6px 10px -1px #adadad;-webkit-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad;border-radius:4px;position:absolute;z-index:2}.ipython_tooltip a{float:right}
.ipython_tooltip .tooltiptext pre{border:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;font-size:100%;background-color:#f7f7f7}
.pretooltiparrow{left:0;margin:0;top:-16px;width:40px;height:16px;overflow:hidden;position:absolute}
.pretooltiparrow:before{background-color:#f7f7f7;border:1px #ababab solid;z-index:11;content:"";position:absolute;left:15px;top:10px;width:25px;height:25px;-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);-o-transform:rotate(45deg)}

    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration -->

</head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[1]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="o">%</span><span class="k">matplotlib</span> <span class="n">inline</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span> <span class="c"># side-stepping mpl backend</span>
<span class="kn">import</span> <span class="nn">matplotlib.gridspec</span> <span class="kn">as</span> <span class="nn">gridspec</span> <span class="c"># subplots</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.dates</span> <span class="kn">as</span> <span class="nn">mdates</span>
<span class="kn">import</span> <span class="nn">csv</span>
<span class="kn">import</span> <span class="nn">datetime</span>

<span class="n">d</span> <span class="o">=</span> <span class="p">{}</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s">&#39;Final_GSWS01_2014.csv&#39;</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">readfile</span><span class="p">:</span>
    <span class="n">reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">readfile</span><span class="p">)</span>
    
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">reader</span><span class="p">:</span>
        
        <span class="n">dt</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="s">&#39;%Y-%m-</span><span class="si">%d</span><span class="s"> %H:%M:%S&#39;</span><span class="p">)</span>
        <span class="n">ori</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
        <span class="n">adj</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
        
        <span class="k">if</span> <span class="n">dt</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span>
            <span class="n">d</span><span class="p">[</span><span class="n">dt</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;ori&#39;</span><span class="p">:</span> <span class="nb">round</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">ori</span><span class="p">),</span><span class="mi">3</span><span class="p">),</span> <span class="s">&#39;adj&#39;</span><span class="p">:</span> <span class="nb">round</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">adj</span><span class="p">),</span><span class="mi">3</span><span class="p">)}</span>
        <span class="k">elif</span> <span class="n">dt</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span>
            <span class="k">pass</span>            
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[4]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>

<span class="c"># add a grid to the background</span>
<span class="n">ax</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="n">alpha</span> <span class="o">=</span> <span class="mf">0.2</span><span class="p">)</span>
<span class="c"># the x axis contains date</span>
<span class="n">fig</span><span class="o">.</span><span class="n">autofmt_xdate</span><span class="p">()</span>
<span class="c"># the dates are year, month</span>
<span class="n">ax</span><span class="o">.</span><span class="n">fmt_xdata</span> <span class="o">=</span> <span class="n">mdates</span><span class="o">.</span><span class="n">DateFormatter</span><span class="p">(</span><span class="s">&#39;%Y-%m&#39;</span><span class="p">)</span>

<span class="n">days</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">d</span><span class="o">.</span><span class="n">keys</span><span class="p">())[</span><span class="mi">42500</span><span class="p">:</span><span class="mi">43000</span><span class="p">]</span>
<span class="n">original</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">new</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">dot1</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span>
<span class="n">dot2</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span>

<span class="k">print</span> <span class="s">&quot;At the end of the period, the CR value was 0.207 and the HG was 0.212&quot;</span>
<span class="k">print</span> <span class="s">&quot;The next period begins with an adjusted value of &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">dot2</span><span class="p">)</span>

<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">original</span><span class="p">,</span> <span class="s">&#39;r-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">new</span><span class="p">,</span> <span class="s">&#39;b-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot1</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;pink&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot2</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;cyan&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s">&#39;date&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s">&#39;stage&#39;</span><span class="p">)</span>
<span class="k">print</span> <span class="s">&quot;The blue line is the adjusted value and the red graph is the original value&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
At the end of the period, the CR value was 0.207 and the HG was 0.212
The next period begins with an adjusted value of 0.214

</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
d7uOLcMAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
The blue line is the adjusted value and the red graph is the original value

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[5]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>

<span class="c"># add a grid to the background</span>
<span class="n">ax</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="n">alpha</span> <span class="o">=</span> <span class="mf">0.2</span><span class="p">)</span>
<span class="c"># the x axis contains date</span>
<span class="n">fig</span><span class="o">.</span><span class="n">autofmt_xdate</span><span class="p">()</span>
<span class="c"># the dates are year, month</span>
<span class="n">ax</span><span class="o">.</span><span class="n">fmt_xdata</span> <span class="o">=</span> <span class="n">mdates</span><span class="o">.</span><span class="n">DateFormatter</span><span class="p">(</span><span class="s">&#39;%Y-%m&#39;</span><span class="p">)</span>

<span class="n">days</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">d</span><span class="o">.</span><span class="n">keys</span><span class="p">())[</span><span class="mi">41500</span><span class="p">:</span><span class="mi">45000</span><span class="p">]</span>
<span class="n">original</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">new</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">dot1</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span>
<span class="n">dot2</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span>

<span class="k">print</span> <span class="s">&quot;Here are the same values within the context of a few days&quot;</span>

<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">original</span><span class="p">,</span> <span class="s">&#39;r-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">new</span><span class="p">,</span> <span class="s">&#39;b-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot1</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;pink&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot2</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;cyan&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s">&#39;date&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s">&#39;stage&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="k">print</span> <span class="s">&quot;Now let&#39;s see between this period and the next one&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
Here are the same values within the context of a few days

</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
c83+8QDdW6UEZMclYxrz2eYeZKVlFV3ZJjIzeX92Y26+ISdPUde+5ejSYCfD728Qkkvb5CjqABv9
tjf59vljgJNEZKGITBGRVsG4sO19xEuCV7SoDrsIho65n26gQ8Jy4urVyFNW9eL+DKjyF8u/WlXk
eUyO4dO59ejev1yJbUhMTKRxn/rUi97MrAmRNfhu7Udz+YPOnHVb43yfx1dza/LQ1yeG5No2OYri
ZJ8XAPWMMe2B54AvQ2uSoijBYsH3O+ncYGeB5fVrZzLkoR788d7yQs/z10crWZ1Rn1P+1SJgW85s
uZp5P+wN+Hg3+OmT3VzYfBHlCvCP1atD2+Ll9EuMTd1jNwP1/Lbr4bQqDmOMSfH7/1sReVFEKhtj
9hx7sjFjxhAX53SX69atG7169TrshXPjrbnb27ZtIzExscDySNr2jyXbYE+g26mpqdSsWdMaewLd
1udxZHvpEjiljRRYftdz9fmu/xZmf7uB5ufUy/d8u1ftoeOldbmp/TSSag8usT25/3fsnsG33yZy
uyX3tzjbv82Jpd+5JmjPY/78+cyYMYOMjLzreByLNd1jRSQGWAn0B7YAc4GhxpjlfnVqADuMMUZE
ugIfG2Ma5nOuEnWPTU1N9UyIwCtaVIddBENH5wp/89zYHfS4o2eBdR4/fQZbtgpP/9k73/L/O3sG
n02vzMz97QKyIVfH2l820rR3LQ6m5BCXWPT4C7cx+5KpUimbaT9AxwGVQ/K+iojuscaYLOBm4Dtg
GfCRMWa5iFwnItf5ql0ALBaRv4CngUuCcW0vfJBz8YoW1WEXpdWxP9nwx/5mtDq1bqH1Tj6zMt8u
rV/gIkPTZ5dl6GmBh4xydTQ6pR6NYzfy/eN/BXyucDLp3rnspTId+lcGwv++sqZFEUx0wJ2i2MXb
D67ntfFb+S29K0QV/Ps0IzWDiklZjOo5l/G/9jmqLCstizJlDAs+XUvb85uV2qbbOvzM7uRo3l1T
cAvHFs6sMYeTToLRX3QL2TUiokXhJl7p6w7e0aI67KK0OmZ+vo1ezXYU6iQA4hLjmPLU37w4sx0Z
qUfHzqc9+ReNYzeVykn467jo+sr8vKFko8HdYOW3a5i8oxuX33MkhavrUSiK4jl+XVWT7gOKFy7p
dWNbykUd4rbusw/vS9uXxiVjm3LtwPVBs6n71a3ZnV2RpZNWB+2coeDF0RsZUn0u9brVds0GdRR4
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
gg==
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
Now let&apos;s see between this period and the next one

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[10]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>

<span class="c"># add a grid to the background</span>
<span class="n">ax</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="n">alpha</span> <span class="o">=</span> <span class="mf">0.2</span><span class="p">)</span>
<span class="c"># the x axis contains date</span>
<span class="n">fig</span><span class="o">.</span><span class="n">autofmt_xdate</span><span class="p">()</span>
<span class="c"># the dates are year, month</span>
<span class="n">ax</span><span class="o">.</span><span class="n">fmt_xdata</span> <span class="o">=</span> <span class="n">mdates</span><span class="o">.</span><span class="n">DateFormatter</span><span class="p">(</span><span class="s">&#39;%Y-%m&#39;</span><span class="p">)</span>

<span class="n">days</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">d</span><span class="o">.</span><span class="n">keys</span><span class="p">())[</span><span class="mi">41000</span><span class="p">:</span><span class="mi">49000</span><span class="p">]</span>
<span class="n">original</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">new</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">days</span><span class="p">]</span>
<span class="n">dot1</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span>
<span class="n">dot2</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">)][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span>
<span class="n">dot3</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">18</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">10</span><span class="p">)][</span><span class="s">&#39;ori&#39;</span><span class="p">]</span>
<span class="n">dot4</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">18</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">10</span><span class="p">)][</span><span class="s">&#39;adj&#39;</span><span class="p">]</span>

<span class="k">print</span> <span class="s">&quot;It&#39;s not super easy to see here because there were flashes from events, but in the end the adjusted and the CR are in lock-step at 0.202 which is mostly just good fortune&quot;</span> 

<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">original</span><span class="p">,</span> <span class="s">&#39;r-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">new</span><span class="p">,</span> <span class="s">&#39;b-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot1</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;pink&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">30</span><span class="p">),</span> <span class="n">dot2</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;cyan&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">18</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">10</span><span class="p">),</span> <span class="n">dot3</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;pink&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">18</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">10</span><span class="p">),</span> <span class="n">dot4</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;cyan&#39;</span><span class="p">)</span>

<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s">&#39;date&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s">&#39;stage&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
It&apos;s not super easy to see here because there were flashes from events, but in the end the adjusted and the CR are in lock-step at 0.202 which is mostly just good fortune

</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[10]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre> 
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
