fun main() = with(System.`in`.bufferedReader()){
    var a = readLine()
    var list = readLine().split(" ").map { it.toInt() }
    var n = readLine().toInt()
    var answer = list.count({it == n})
    println(answer)
}