let lengthOfLastWord = s => {
    let words = s.trim().split(" ")
    let lastWord = words[words.length - 1];
    return lastWord.length
}

console.log(lengthOfLastWord("Hello World"))
console.log(lengthOfLastWord("    fly me   to   the moon  "))
console.log(lengthOfLastWord("luffy is still joyboy"))