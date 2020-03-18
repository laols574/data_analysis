//
// buttons.js
// Buttons Example for CSC444 Assignment 05
// Joshua A. Levine <josh@email.arizona.edu
//
// This file provides a simple example of using d3 to create buttons in
// an html webpage.  The buttons are created from a list of buttons
// (called buttonList) that specifies the id, display text, and
// event-handler function that should be called for each button click.
//
// All buttons are inserted by d3 within a div whose id is main
//

// Here is a list with objects that specify some buttons.

var buttonList = [
  {
      id: "non",
      text: "Figure Eight",
      click: function() {
        e = document.getElementById("vis1");
        e.innerHTML = "";
        createVis1(aggregate);
  }
  },
  {
      id: "big",
      text: "MTURK",
      click: function() {
        e = document.getElementById("vis1");
        e.innerHTML = "";
        createVis1(big);
  }
  },
    {
        id: "gender",
        text: "See Gender",
        click: function() {
          let vis1 = d3.select("#vis1")

          vis1.selectAll("circle")
              .data(data)
              .transition()
              .duration(1500)
              .attr("fill", function(d){
                if(d.gender == "Female"){
                  return "#b04175";
                }
                if(d.gender == "Male"){
                  return "#568041";
                }
                else{
                  return "rgb(213,222,217)";
                }
              })
              .attr("opacity", function(d){
                if(d.gender == "Female"){
                  return .7;
                }
                if(d.gender == "Male"){
                  return .7;
                }
                else{
                  return .2;
                }
              })
              ;
    }
  },
  {
      id: "education",
      text: "See Education",
      click: function() {
        let vis1 = d3.select("#vis1")

        vis1.selectAll("circle")
            .data(data)
            .transition()
            .duration(1500)
            .attr("fill", function(d){
              edu = "";
              if(d.education != null){
                edu = d.education.toLowerCase();
              }
              if(edu == "high school"){
                return "#ff5050";
              }
              if(edu == "university" || edu == "college"){
                return "#3366ff";
              }
              else{
                return "rgb(213,222,217)";
              }
            })
            .attr("opacity", function(d){
              edu = "";
              if(d.education != null){
                edu = d.education.toLowerCase();
              }
              if(edu == "high school"){
                return .7;
              }
              if(edu == "university" || edu == "college"){
                return .7;
              }
              else{
                return .1;
              }
            })
            ;
  }
},
  {
      id: "non",
      text: "See Non-Counterspeech",
      click: function() {
        let vis1 = d3.select("#vis1")

        vis1.selectAll("circle")
            .data(data)
            .transition()
            .duration(1500)
            .attr("cx" ,function(d, i) {
              cx = cxScale(data);
              return cx(i);
            }
            )
            ;
  }
},

{
      id: "reactions",
      text: "See Reactions",
      class: "drop",
      click: function() {
        let vis1 = d3.select("#vis1")

        vis1.selectAll("circle")
            .data(data)
            .transition()
            .duration(1500)
            .attr("r", function(d){
              r = rScale2();
              return r(d.reactions);
              }
            )
            ;
  }
},
  {
      id: "sigh",
      text: "See Sighs",
      class: "drop",
      click: function() {
        let vis1 = d3.select("#vis1")

        vis1.selectAll("circle")
            .data(data)
            .transition()
            .duration(1500)
            .attr("r", function(d){
              r = rScale2();
              return r(d.sigh);
              }
            )
            ;
  }
},
{
    id: "grr",
    text: "See Grr",
    class: "drop",
    click: function() {
      let vis1 = d3.select("#vis1")

      vis1.selectAll("circle")
          .data(data)
          .transition()
          .duration(1500)
          .attr("r", function(d){
            r = rScale2();
            return r(d.grr);
            }
          )
          ;
}
},
{
    id: "love",
    text: "See Loves",
    class: "drop",
    click: function() {
      let vis1 = d3.select("#vis1")

      vis1.selectAll("circle")
          .data(data)
          .transition()
          .duration(1500)
          .attr("r", function(d){
            r = rScale2();
            return r(d.love);
            }
          )
          ;
}
},
{
    id: "ahah",
    text: "See ahahas",
    class: "drop",

    click: function() {
      let vis1 = d3.select("#vis1")

      vis1.selectAll("circle")
          .data(data)
          .transition()
          .duration(1500)
          .attr("r", function(d){
            r = rScale2();
            return r(d.ahah);
            }
          )
          ;
}
},
{
    id: "likes",
    text: "See Likes",
    class: "drop",
    click: function() {
      let vis1 = d3.select("#vis1")

      vis1.selectAll("circle")
          .data(data)
          .transition()
          .duration(1500)
          .attr("r", function(d){
            r = rScale2();
            return r(d.likes);
            }
          )
          ;
}
},
{
    id: "wow",
    text: "See Wows",
    class: "drop",
    click: function() {
      let vis1 = d3.select("#vis1")

      vis1.selectAll("circle")
          .data(data)
          .transition()
          .duration(1500)
          .attr("r", function(d){
            r = rScale2(data);
            return r(d.wow);
            }
          )
          ;
}
}
];


d3.select("#main")
    .selectAll("button")
    .data(buttonList)
    .enter()
    .append("button")
    .attr("id", function(d) { return d.id; })
    .text(function(d) { return d.text; })
    .on("click", function(d) {
        // Since the button is bound to the objects from buttonList,
        // the expression below calls the click function from either
        // of the two button specifications in the list.
        return d.click();
    });
