$(document).ready(function () {
  //ready函数，这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码。
  $("button").click(
    //隐藏所有button元素
    function () {
      $(this).hide();
    });

  $("#id_1").click(
    //隐藏所有id=id_1的元素
    function () {
      $(this).hide();
    });

  $(".class_1").click(
    //隐藏所有class=class_1的元素
    function () {
      $(this).hide();
    });

  $("table").click(function () {
    $(this).toggle(500);
  });

  $("#button2").click(function () {
    var div_1 = $("#div_1");
    div_1.animate({
      left: '250px',
      opacity: '0.5',
      height: '150px',
      width: '150px'
    });

    var div_2 = $("#div_2");
    div_2.animate({left:'100px'},"slow");
    div_2.animate({fontSize:'3em'},"slow");
  });

  $("#flip").click(function(){
    $("#panel").slideDown(3000);
  });
  $("#stop").click(function(){
    $("#panel").stop();
  });

});