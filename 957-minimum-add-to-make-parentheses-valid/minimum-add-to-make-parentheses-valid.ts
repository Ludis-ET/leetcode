function minAddToMakeValid(s: string): number {
    let stack: string[] = [];
    for (const c of s){
        if (stack.length > 0 && stack[stack.length - 1] === '(' && c === ')'){
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    return stack.length
};