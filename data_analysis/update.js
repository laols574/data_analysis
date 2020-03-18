d3.selectAll(".myCheckbox").on("change",update);
update();

function update(){

  oldData = data;
  var choices = [];
  d3.selectAll(".myCheckbox").each(function(d){
    cb = d3.select(this);
    if(cb.property("checked")){
      choices.push(cb.property("value"));
    }
  });

  if(choices.length > 0){
    newData = data.filter(function(d,i){
      return choices.includes(d.type);});
  } else {
    newData = data;
  }
  console.log(newData == oldData);
  document.getElementById("vis1").innerHTML = "";
  createVis1(newData, true);

}
