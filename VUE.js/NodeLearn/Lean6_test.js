//用管道和链式来压缩和解压文件。

var fs = require("fs");
var zlib = require('zlib');

// 压缩 input.txt 文件为 input.txt.gz
fs.createReadStream('output.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('output.txt.gz'));
  
console.log("文件压缩完成。");


// 解压 input.txt.gz 文件为 input.txt
fs.createReadStream('output.txt.gz')
  .pipe(zlib.createGunzip())
  .pipe(fs.createWriteStream('output.txt'));
  
console.log("文件解压完成。");
