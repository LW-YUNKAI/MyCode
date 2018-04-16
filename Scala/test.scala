//val不可变 and var可变
val x = 10
var y = 20

def welcome(name: String) = "hello " + name

//map
List("a", "b", "c").map((name)=>"this is "+name).foreach(println)

//闭包
var f : Int => Int = null
def doStuff() = {
    var n = 3
    def addn(m: Int) = {
        m + n
    }
    f = addn
    n = n + 1
}

//类型判断
//一般为了便于阅读，需要显式声明函数
def addOne(x:Int):Double = {
    val xPlusOne = x + 1.0
    //无需return
    xPlusOne
}

//元组
val t = Tuple3("1", "rick", "王云开")
println(t._1 + " " + t._2 + " " + t._3)

//函数
class myClass(val name:String, id:Integer = 0){
    def makeMessage = "hi " + name + " " + id
}
val/var y1 = new myClass("dog")

//map&reduce
class fruitCount(val name:String, val num:Int)
val groceries:List[fruitCount] = List(
    new fruitCount("banana", 1),
    new fruitCount("apple", 2),
    new fruitCount("melon", 3),
    new fruitCount("pear", 4)
)
// scala> groceries{1}.name
// res15: String = apple
groceries.map(_.num).reduce((a:Int, b:Int)=>a+b)












