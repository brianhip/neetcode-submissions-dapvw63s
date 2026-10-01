class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> set_nums(nums.begin(), nums.end());
        return set_nums.size() != nums.size();
    }
};