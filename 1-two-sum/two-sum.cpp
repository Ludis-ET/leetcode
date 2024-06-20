class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            int temp = target - nums[i];
            if (ans.find(temp) != ans.end()) {
                return {ans[temp], i};
            }
            ans[nums[i]] = i;
        }
        return {};
    }
};