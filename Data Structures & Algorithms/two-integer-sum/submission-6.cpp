class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> value_index(nums.size());
        for (size_t i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (value_index.contains(complement)) {
                return {value_index[complement], static_cast<int>(i)};
            }
            value_index[nums[i]] = i;
        }
        return {-1, -1};
    }
};
