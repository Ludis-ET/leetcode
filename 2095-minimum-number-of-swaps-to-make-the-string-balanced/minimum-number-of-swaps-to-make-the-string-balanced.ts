function minSwaps(s: string): number {
    let balance = 0
    let swaps = 0

    for (const char of s) {
        if (char === '[') {
            balance += 1
        } else {
            balance -= 1
        }

        if (balance < 0) {
            swaps += 1
            balance += 2
        }
    }

    return swaps
}