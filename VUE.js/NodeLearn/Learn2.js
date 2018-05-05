var fs = require("fs");

//阻塞
var data = fs.readFileSync('Learn1.js');
console.log(data.toString());

//非阻塞:回调函数
fs.readFile('Learn1.js', function (err, data) {
    if (err) 
        return console.error(err);
    console.log(data.toString());
});

console.log("程序执行结束");
