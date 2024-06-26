class Solution {
public:
    int fib(int n) {
        int arr[2] = {0, 1};
        for (int c = 2; c < n; c++){
            int tmp = arr[0];
            arr[0] = arr[1];
            arr[1] += tmp;
        }
        return n > 1 ? arr[0] + arr[1] : n;
    }
};