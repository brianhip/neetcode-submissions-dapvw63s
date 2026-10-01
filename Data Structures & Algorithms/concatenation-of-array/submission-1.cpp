class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        size_t N = nums.size();
        vector<int> output(N * 2);
        for (size_t i = 0; i < N; ++i){
            output[i] = nums[i % N];
            output[i + N] = output[i];
        }
        return output;
    }
};