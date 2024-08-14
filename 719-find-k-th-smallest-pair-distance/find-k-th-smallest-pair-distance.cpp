class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.back();
        while (l < r){
            int m = l + ((r - l) / 2);
            int count = 0, left = 0;
            for (int right = 1; right < nums.size(); ++right){
                while (nums[right] - nums[left] > m && left <= right){
                    left++;
                }
                count += right - left;
            }
            if (count >= k){
                r = m;
            }else {
                l = m + 1;
            }
        }
        return r;
    }
};