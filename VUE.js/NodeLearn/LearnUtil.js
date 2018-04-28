//util 是一个Node.js 核心模块，提供常用函数的集合，用于弥补核心JavaScript 的功能 过于精简的不足。
var http = require('http');
var url = require('url');
var util = require('util');
var querystring = require('querystring');
 
var postHTML = 
  '<html><head><meta charset="utf-8"><title>菜鸟教程 Node.js 实例</title></head>' +
  '<body>' +
  '<form method="post">' +
  '网站名： <input name="name"><br>' +
  '网站 URL： <input name="url"><br>' +
  '<input type="submit">' +
  '</form>' +
  '</body></html>';

  http.createServer(function (req, res) {
    // 定义了一个post变量，用于暂存请求体的信息
    var post = "";

    // 通过req的data事件监听函数，每当接受到请求体的数据，就累加到post变量中
    req.on('data', function (chunk) {
      post += chunk;
    });

    // 在end事件触发后，通过querystring.parse将post解析为真正的POST请求格式，然后向客户端返回
    req.on('end', function () {
      // 解析参数
      post = querystring.parse(post);
      // 设置响应头部信息及编码
      res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
   
      if(post.name && post.url) { // 输出提交的数据
          res.write("网站名：" + post.name);
          res.write("<br>");
          res.write("网站 URL：" + post.url);
      } else {  // 输出表单
          res.write(postHTML);
      }
      res.end();
    });
  }).listen(3000);

