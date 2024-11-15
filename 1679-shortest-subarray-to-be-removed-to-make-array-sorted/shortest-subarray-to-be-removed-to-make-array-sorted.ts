function findLengthOfShortestSubarray(arr: number[]): number {
    const n = arr.length;
    let left = 0;
    let right = n - 1;

    while (left < n - 1 && arr[left] <= arr[left + 1]) {
        left++;
    }

    if (left === n - 1) {
        return 0;
    }

    while (right > 0 && arr[right] >= arr[right - 1]) {
        right--;
    }

    let result = Math.min(n - left - 1, right);
    let i = 0, j = right;

    while (i <= left && j < n) {
        if (arr[i] <= arr[j]) {
            result = Math.min(result, j - i - 1);
            i++;
        } else {
            j++;
        }
    }

    return result;
}