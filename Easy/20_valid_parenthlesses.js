let isValid = s => {
    let stack = [];
    let i = 0;
    const validMap = {"(": ")", "[": "]", "{": "}"}

    while(i < s.length){
        if(s[i] in validMap){
            stack.push(s[i])
        } else {
            if(!stack){
                console.log("stack empty", stack)
                return false;
            }
            
            let lastParenthesis = stack.pop();
            if (validMap[lastParenthesis] !== s[i]){
                return false
            }
        }

        i++;
    }

    if(stack.length){
        return false
    }

    return true
}

console.log(isValid("()"))
console.log(isValid("()[]{}"))
console.log(isValid("(]"))
console.log(isValid("([])"))