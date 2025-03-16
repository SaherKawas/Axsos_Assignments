function alwaysHungry(arr) {
    var arr2 = [];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            arr2.push("yummy");
        }
    }

    if (arr2.length === 0) {
        arr2.push("I'm hungry");
    }

    for (var i = 0; i < arr2.length; i++) {
        console.log(arr2[i]);
    }
}

alwaysHungry([3.14, "pie", true]);

// 2 high pass filter

function highPass (arr, cutoff){
    var filteredArr= [];
    
    for(var i=0 ; i<arr.length ; i++){
        if(arr[i]>cutoff){
        filteredArr.push (arr[i])
        } 
    }
    return filteredArr;
}

console.log (highPass([6, 8, 3, 10, -2, 5, 9], 5));

// 3 Better than average


    
    function sumElements (arr){
        var sum=0;
    for(var i=0 ; i<arr.length ; i++){
        sum = sum + arr[i]
        console.log (sum)
    }
    var avg=sum/arr.length;

    var count=0
    for(var i=0 ; i<arr.length ; i++){
        if(arr[i]>avg){
            count++;
        }
    }
    return count;
}


    console.log (sumElements ([6,8,3,10,-2,5,9]))

    // 4 array reverse

    
    function reverse(arr) {
        let reversedArray = [];
        let length = arr.length;

    for (let i = 0; i < length; i++) {
        reversedArray.push(arr.pop());

    }

    return reversedArray;
}
console.log (reverse ([3,5,1,4,67,7]))

// 5 fibonacci
 
function fibonacciArray(n){
    var fibArr=[0,1]
    for (i=0 ; i< n-2 ; i++){
        fibArr.push(fibArr[i]+fibArr[i+1]);
    }
    console.log(fibArr)
}
fibonacciArray(6)