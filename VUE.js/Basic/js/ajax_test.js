$(document).ready(function () {

  $("button").click(function () {
    $("#div1").load("leaern.txt", function (responseTxt, statusTxt, xhr) {
      // responseTxt - 包含调用成功时的结果内容
      // statusTXT - 包含调用的状态
      // xhr - 包含 XMLHttpRequest 对象
      if (statusTxt == "success")
        alert("外部内容加载成功！");
      if (statusTxt == "error")
        alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
  });

  function add_score(score) {
    $.ajax({
      url: "/add_score",
      data: {
        "score": score
      },
      success: function (msg) {
        //alert(msg['tip']);
        location.reload();
      }
    });
  }
});