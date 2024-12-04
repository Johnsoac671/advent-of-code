import java.io.File
import kotlin.math.abs

fun main() {
    val data = splitInput(readInput("src/day1_input.txt"))
    println("Difference: ${findDifferences(data).sum()}")
    println("Similarity: ${getSimilarity(data)}")
}

fun getSimilarity(data: List<List<Int>>): Int {
    val left = data[0]
    val right = data[1]

    val countMap = createCountMap(right)

    var similarity = 0
    for (num in left) {
        similarity += (num * countMap.getOrDefault(num, 0))
    }

    return similarity
}

fun createCountMap(data: List<Int>): Map<Int, Int> {
    val countMap = mutableMapOf<Int, Int>()
    for (num in data){
        countMap[num] = countMap[num]?.plus(1) ?: 1
    }
    return countMap
}

fun findDifferences(locations: List<List<Int>>): List<Int> {
    val differences = mutableListOf<Int>()

    for(i in locations[0].indices){
        differences.add(abs(locations[0][i] - locations[1][i]))
    }

    return differences

}

fun splitInput(data: List<String>): List<List<Int>> {
    val leftList = mutableListOf<Int>()
    val rightList = mutableListOf<Int>()

    var seperatedLine: List<String>
    for (line in data) {
        seperatedLine = line.split("   ")

        leftList.add(seperatedLine[0].toInt())
        rightList.add(seperatedLine[1].toInt())
    }

    return listOf(mergeSort(leftList), mergeSort(rightList))
}

fun readInput(filename: String): List<String> {
    val content = File(filename).readLines()
    return content
}

fun mergeSort(data: List<Int>): List<Int> {

    fun merge(a: List<Int>, b: List<Int>): List<Int> {
        val merged = mutableListOf<Int>()

        var indexA = 0
        var indexB = 0

        while (indexA < a.size || indexB < b.size) {
            if (indexA >= a.size) {
                merged.add(b[indexB])
                indexB++
                continue
            }

            if (indexB >= b.size) {
                merged.add(a[indexA])
                indexA++
                continue
            }

            if (a[indexA] <= b[indexB]) {
                merged.add(a[indexA])
                indexA++

            } else {
                merged.add(b[indexB])
                indexB++
            }
        }

        return merged
    }

    if (data.size <= 1) {
        return data
    }

    var left = data.slice(0..<data.size/2)
    var right = data.slice((data.size/2)..<data.size)

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

}



