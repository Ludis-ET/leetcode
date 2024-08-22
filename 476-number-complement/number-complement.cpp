class Solution {
public:
    int findComplement(int num) {
        int ans = 0, i = 0;
        while(num > 0){
            if ((num & 1) == 0){
                ans |= (1 << i);
            }
            i += 1;
            num >>= 1;
        }
        return ans;
    }
};