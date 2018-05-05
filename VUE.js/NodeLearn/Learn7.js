console.log(__filename);
console.log(__dirname);

//内部只能使用函数
setTimeout(function(){console.log(__dirname);}, 2000)

var t = setTimeout(function(){console.log(__dirname);}, 2000);
clearTimeout(t);

//循环
// setInterval(function (){
//     console.log( "Hello, World!");
// }, 2000);
// clearInterval(t)
//console


console.info("程序开始执行：");
var counter = 10;

//
// 执行一些代码
setInterval(function (){
    console.time('获取数据');
    console.log( "Hello, World!");
    console.timeEnd('获取数据');
}, 2000);
// 


console.info("程序执行完毕。")