func insertionSort( arr:Array<Array<Int>> ) -> Array<Array<Int>> {
  var arr1 = arr
  let len = arr1.count
  for index in 0...(len-1) {
    var key = arr1[index]
    var index_2 = index - 1
    while (index_2 >= 0) && (key[0] < arr1[index_2][0]) {
      arr1[index_2 + 1] = arr1[index_2]
      index_2 -= 1
    }
  arr1[index_2 + 1] = key
  }
  return arr1
}

var test = insertionSort( arr:[[12,34,2,7,1,0,9,56],[1,2,3,4],[1,5,3,8,6,4],[1,2]])

print(test)