function minimizedMaximum(n: number, quants: number[]): number {
    let left = 1,
        right = quants.reduce((prev, curr) => Math.max(prev, curr)), 
        x = 0;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (quants.reduce((prev, curr) => prev + Math.ceil(curr / mid), 0) <= n) {
            x = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return x;
}