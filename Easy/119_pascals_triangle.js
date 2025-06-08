let generate = numRows => {
    let startRows = [[1], [1, 1]]
    let counter = numRows - 2;

    if(numRows === 1){
        return [[1]]
    } else if(numRows == 2){
        return [[1], [1, 1]]
    }

    while(counter){
        let lastArr = startRows[startRows.length - 1];
        let newArr = [1];

        for(let i = 0; i < lastArr.length; i++){
            let newNum = lastArr[i] + lastArr[i+1];

            if(!isNaN(newNum)) newArr.push(newNum);
        }

        newArr.push(1)

        startRows.push(newArr)
        counter--;
    }

    return startRows
}


console.log(generate(5))
console.log(generate(1))