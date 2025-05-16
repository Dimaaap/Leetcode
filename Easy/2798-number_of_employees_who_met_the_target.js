let numberOfEmployeesWhoMetTarget = function(hours, target){
    let counter = 0;

    for(let hour of hours){
        if(hour >= target){
            counter++;
        }
    }

    return counter;
}

console.log(numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2))
console.log(numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6))