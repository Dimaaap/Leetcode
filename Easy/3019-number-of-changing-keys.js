let countKeyChanges = function(s){
    let counter = 0;
    
    for(let i = 0; i < s.length - 1; i++){
        if(s[i].toLowerCase() !== s[i + 1].toLowerCase()){
            counter++
        }
    }

    return counter
}

console.log(countKeyChanges("aAbBcC"))
console.log(countKeyChanges("AaAaAaAaaA"))