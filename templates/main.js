function run() {
  const path = document.getElementById("path").value;
  eel.run(path);
}

eel.expose(result);
function result(r) {
  console.log(r);
  if(r) {
    document.getElementById("result").innerHTML = "Done :)";
  } else {
    document.getElementById("result").innerHTML = "Failed :(";
  }
}