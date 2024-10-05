function checkInclusion(s1: string, s2: string): boolean {
    const a = s1.length, b = s2.length;
    if (a > b) return false
    const arr1: number[] = Array(26).fill(0);
    const arr2: number[] = Array(26).fill(0);

    for (let i = 0; i < a; i++){
        arr1[s1.charCodeAt(i) - 97]++;
        arr2[s2.charCodeAt(i) - 97]++;
    }
    let matches = 0;
    for (let i = 0; i < 26; i++){
        if (arr1[i] === arr2[i])
            matches++;
    }
    if (matches === 26) return true
    for (let i = a; i < b; i++){
        const indexIn = s2.charCodeAt(i) - 97;
        const indexOut = s2.charCodeAt(i - a) - 97;
        
        arr2[indexIn]++;
        if (arr1[indexIn] === arr2[indexIn]) {
            matches++;
        } else if (arr1[indexIn] === arr2[indexIn] - 1) {
            matches--;
        }

        arr2[indexOut]--;
        if (arr1[indexOut] === arr2[indexOut]) {
            matches++;
        } else if (arr1[indexOut] === arr2[indexOut] + 1) {
            matches--;
        }
        if (matches === 26) return true
    }
    return false
};