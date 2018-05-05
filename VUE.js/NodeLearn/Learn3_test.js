//本例子，connection事件被emit时，绑定了connectionHandler,又绑定了data_received

var events = require('events');
var eventEmitter = new events.EventEmitter();

eventEmitter.on('connection', function(){
    console.log('connection');
    eventEmitter.emit('data_received');
});

eventEmitter.on('data_received', function(){
    console.log('data_received');
 });

eventEmitter.emit('connection');

console.log("程序执行完毕。");
