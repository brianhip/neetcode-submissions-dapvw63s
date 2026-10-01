class Solution {
public:
    bool isAnagram(string s, string t) {
        // Manually count each character
        // Create a map
        // Check both maps
        // return true if equal else false
        std::unordered_map<char, int> char_count;
        for (char c : s){
            if (!char_count.contains(c)){
                char_count[c] = 0;
            }
            char_count[c] += 1;
        }

        for (char c : t) {
            if (!char_count.contains(c)){
                return false;
            }
            char_count[c] -= 1;
            if (char_count[c] == 0) {
                char_count.erase(c);
            }
        }


        return char_count.size() == 0;
    }
};
