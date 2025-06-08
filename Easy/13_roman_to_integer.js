let romanToInt = s => {
    let commonChars = {
        "I": 1, 
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    let specialChars = {
        "IV": 4, "IX": 9,
        "XL": 40, "XC": 90,
        "CD": 400, "CM": 900
    }

    let i = res = 0;
    while(i < s.length){
        let sSlice = s.slice(i, i + 2);

        if(sSlice in specialChars){
            res += specialChars[sSlice]
            i += 2;
        } else {
            res += commonChars[s[i]]
            i++;
        }
    }

    return res;
}

console.log(romanToInt("III"))
console.log(romanToInt("LVIII"))
console.log(romanToInt("MCMXCIV"))