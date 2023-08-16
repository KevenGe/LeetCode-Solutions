class Trie {
public:

	struct TreeNode {
		char ch;
		bool end;
		TreeNode * son[26];
		TreeNode(char ch_ = '-') {
			ch = ch_;
			end = false;
			for (int i = 0; i < 26; ++i) {
				son[i] = NULL;
			}
		}
	};
	
	TreeNode* root;


	/** Initialize your data structure here. */
	Trie() {
		root = new TreeNode();
	}

	/** Inserts a word into the trie. */
	void insert(string word) {
		TreeNode* p = root;
		for (unsigned i = 0; i < word.length(); ++i) {
			if (p->son[word[i] - 'a'] == NULL) {
				TreeNode* q = new TreeNode(word[i]);
				p->son[word[i] - 'a'] = q;
				p = q;
			}
			else {
				p = p->son[word[i] - 'a'];
			}
		}
		p->end = true;
	}

	/** Returns if the word is in the trie. */
	bool search(string word) {
		TreeNode* p = root;
		for (unsigned i = 0; i < word.length(); ++i) {
			if (p->son[word[i] - 'a'] == NULL) {
				return false;
			}
			else {
				p = p->son[word[i] - 'a'];
			}
		}
		if (p->end == true)
			return true;
		else
			return false;
	}

	/** Returns if there is any word in the trie that starts with the given prefix. */
	bool startsWith(string prefix) {
		TreeNode* p = root;
		for (unsigned i = 0; i < prefix.length(); ++i) {
			if (p->son[prefix[i] - 'a'] == NULL) {
				return false;
			}
			else {
				p = p->son[prefix[i] - 'a'];
			}
		}
		return true;
	}
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */