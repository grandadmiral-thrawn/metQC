---
layout: post
title: "Some Daily Discharge Graphs"
date: 2015-09-16T20:17:47-07:00
---

Steve asked me recently about some of the daily discharge on our watersheds for 2015, so I graphed it. Here's a few to look at:

<iframe srcdoc="
<html><head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
  <script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js"></script>
</head>
<style>
  body {
  font-family: 'Helvetica Neue', Helvetica, sans-serif;
  font-size: 12px;
  font-style: normal;
}
  
 path { 
  stroke: red;
  stroke-width: 2.5;
  fill: none;
}

.axis path,
.axis line {
  fill: none;
  stroke: #black;
  shape-rendering: crispEdges;
}

.line {
  fill: none;
  stroke: purple;
  shape-rendering: crispEdges;
}
</style>
<body>
<p> This is Watershed 2, in 2015</p>
  <script>
      var margin = {
      top: 20,
      right: 20,
      bottom: 30,
      left: 50
    },
    width = 700 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  var format = d3.time.format("%Y-%m-%d");

  var date_format = d3.time.format("%d %b");

  var x = d3.time.scale()
    .range([0, width]);

  var y = d3.scale.linear()
    .range([height, 0]);

  var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .tickFormat(date_format);

  var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

  var valueline = d3.svg.line()
    .interpolate("basis")
    .x(function(d) {
      return x(d.MyDate);
    })
    .y(function(d) {
      return y(d.Mean_Q);
    });


  var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  d3.csv("https://raw.githubusercontent.com/dataRonin/weir2k/master/GSWS02_2015_daily.csv",
    function(d) {
      return {
        Sitecode: d.STCODE,
        Format: d.FORMAT,
        Wateryear: d.WATERYEAR,
        MyDate: format.parse(d.DATE),
        Mean_Q: +d.MEAN_Q,
        Max_Q: +d.MAX_Q,
        Min_Q: +d.MIN_Q,
      };
    },
    function(error, rows) {
      rows.forEach(function(d) {
        x.domain(d3.extent(rows, function(d) {
          return d.MyDate;
        }));
        y.domain(d3.extent(rows, function(d) {
          return d.Mean_Q;
        }));
        
        svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

        svg.append("g")
          .attr("class", "y axis")
          .call(yAxis)
          .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 20)
          .attr("dy", ".71em")
          .style("text-anchor", "end")
          .text("Mean Q, cfs");

        svg.append("path")
          .attr("class", "line")
          .attr("d", valueline(rows));
      });
    });
  </script>
</body></html>"></iframe>

You can see a pretty large spike there, reminescent of what Steve also saw on WS1. But the June and July data is quite low, in fact, he is thinking it is the lowest it has ever been!

