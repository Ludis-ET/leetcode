function longestDiverseString(a: number, b: number, c: number): string {
    const charCounts: [number, string][] = [
        [a, 'a'],
        [b, 'b'],
        [c, 'c']
    ];

    let output = "";

    while (true) {
        charCounts.sort((x, y) => y[0] - x[0]);
    
        if (charCounts[0][0] === 0) break;

        const [maxCount, maxChar] = charCounts[0];
        const [secondMaxCount, secondMaxChar] = charCounts[1];

        const hasUsedMaxChar = output[output.length - 1] === maxChar && output[output.length - 2] === maxChar
        const shouldUseSecondMax = output.length >= 2 && hasUsedMaxChar
        if (shouldUseSecondMax) {
            const noSecondMaxToUse = secondMaxCount === 0
            if (noSecondMaxToUse) break; 
            
            output += secondMaxChar;

            charCounts[1][0]--;
            continue
        } 

        const numToAdd = Math.min(2, maxCount);
        output += maxChar.repeat(numToAdd);
        charCounts[0][0] -= numToAdd; 
        
    }

    return output;
}