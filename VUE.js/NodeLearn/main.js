//fs
var fs = require("fs");
var data = fs.readFileSync('input.txt');

console.log(data.toString());

//event
var evnets = require('events');
var eventEmitter = new evnets.EventEmitter();
//绑定事件处理程序
var connectHandler = function connected(){
  console.log('链接成功');
  eventEmitter.emit('data_receoved');
}
// 绑定 connection 事件处理程序
eventEmitter.on('connection', connectHandler);
 
// 使用匿名函数绑定 data_received 事件
eventEmitter.on(
  'data_receoved', 
  function(){
    console.log('数据接收成功。');
  });

// 触发 connection 事件 
eventEmitter.emit('connection');

console.log("程序执行完毕。"); 