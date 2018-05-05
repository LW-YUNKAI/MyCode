var events = require('events');
var eventEmitter = new events.EventEmitter();

//监听器 #1
var listener1 = function listener1(){
    console.log('listener1 excute');
}

//监听器 #2
var listener2 = function listener2(){
    console.log('listener2 excute');
}

// 绑定 connection 事件，处理函数为 listener1,listener2 
eventEmitter.addListener('connection', listener1);
eventEmitter.on('connection',listener2);

var eventListeners = require('events').EventEmitter.listenerCount(eventEmitter, 'connection')
console.log(eventListeners + " 个监听器监听连接事件。");

// 处理 connection 事件 
eventEmitter.emit('connection');

// 移除监绑定的 listener1 函数
eventEmitter.removeListener('connection', listener1);
console.log("listener1 不再受监听。");

// 触发连接事件
eventEmitter.emit('connection');

eventListeners = require('events').EventEmitter.listenerCount(eventEmitter,'connection');
console.log(eventListeners + " 个监听器监听连接事件。");

console.log("程序执行完毕。");

//大多数时候我们不会直接使用 EventEmitter，而是在对象中继承它。
//包括 fs、net、 http 在内的，只要是支持事件响应的核心模块都是 EventEmitter 的子类。