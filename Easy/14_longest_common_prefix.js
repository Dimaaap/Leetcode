let longestCommonPrefix = strs => {

    let sortedStrs = strs.sort((a, b) => a.length - b.length);
    let shortestWord = sortedStrs[0];

    const isStartFromShortest = currentStr => currentStr.startsWith(shortestWord)

    while(shortestWord){
        if(sortedStrs.every(isStartFromShortest)){
            return shortestWord
        } else {
            shortestWord = shortestWord.slice(0, -1);
        }
    }

    return ""
}


console.log(longestCommonPrefix(["flower", "flow", "flight"]))
console.log(longestCommonPrefix(["dog", "racecar", "car"]))