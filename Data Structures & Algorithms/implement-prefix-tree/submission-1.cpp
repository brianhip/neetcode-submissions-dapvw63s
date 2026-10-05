class TreeNode {
    public:
        std::unordered_map<char, TreeNode*> letters;
        bool end_of_word = false;
};
class PrefixTree {
    TreeNode* start;

public:
    PrefixTree() {
        start = new TreeNode();
    }
    
    void insert(string word) {
        TreeNode* curr = start;
        size_t i = 0; 
        size_t length = word.size();
        while (i < length){
            if (!curr->letters.contains(word[i])){
                curr->letters[word[i]] = new TreeNode();
            }
            curr = curr->letters[word[i]];
            i++;
        }
        curr->end_of_word = true;
    }
    
    bool search(string word) {
        TreeNode* curr = start;
        size_t i = 0; 
        size_t length = word.size();
        while (i < length){
            if (!curr->letters.contains(word[i])){
                return false;
            }
            curr = curr->letters[word[i]];
            i++;
        }
        return curr->end_of_word;
    }
    
    bool startsWith(string prefix) {
        TreeNode* curr = start;
        size_t i = 0; 
        size_t length = prefix.size();
        while (i < length){
            if (!curr->letters.contains(prefix[i])){
                return false;
            }
            curr = curr->letters[prefix[i]];
            i++;
        }
        return true;
    }
};
