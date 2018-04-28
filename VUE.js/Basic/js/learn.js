var alerttxt = "error"

function validate_required(field, alerttxt) {
  with (field) {
    if (value == null || value == "") {
      alert(alerttxt);
      return false
    } else {
      return true
    }
  }
}

function validate_form(thisform) {
  with (thisform) {
    if (validate_email(email, "Email must be filled out!") == false) {
      email.focus();
      return false
    }
  }
}

function validate_email(field, alerttxt) {
  with (field) {
    apos = value.indexOf("@")
    dotpos = value.lastIndexOf(".")
    if (apos < 1 || dotpos - apos < 2) {
      alert(alerttxt);
      return false
    } else {
      return true
    }
  }
}

function OnloadTest() {
  if (true) {
    alert("Onload只能用在<body>, <frame>, <frameset>, <iframe>, <img>, <link>, <script>里");
  }
}

function addLi() {
  var para = document.createElement("li");
  var node = document.createTextNode("new li");
  para.appendChild(node);

  var element = document.getElementById("p1");
  element.appendChild(para);
}

function delLi() {
  var parent = document.getElementById("p1");
  var child = parent.getElementsByTagName("li");
  var lastChild = child.length - 1;
  alert(lastChild);
  parent.removeChild(child[lastChild]);
}

//对象构造器
function person(firstname, lastname, age, eyecolor) {
  this.firstname = firstname;
  this.lastname = lastname;
  this.age = age;
  this.eyecolor = eyecolor;
}


function addPerson() {
  var myFather = new person("Bill", "Gates", 56, "blue");
  var para = document.createElement("li");
  var node = document.createTextNode(myFather.firstname + " " + myFather.lastname);
  para.appendChild(node);

  var element = document.getElementById("fuc");
  element.appendChild(para);
}

function strMatch() {
  var thisStr = document.getElementById("match");
  str = thisStr.innerHTML;
  if (str.match("world")) {
    alert("done!");
  }
}

function strReplace() {
  var thisStr = document.getElementById("replace");
  str = thisStr.innerHTML;
  thisStr.innerHTML = str.replace(/Hello/, "fuck");
}


function wudandandashibi() {
  alert("wudandanshishabi");
  return wudandandashibi();
}
