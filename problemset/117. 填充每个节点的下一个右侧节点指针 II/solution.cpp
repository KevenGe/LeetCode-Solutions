
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>

using namespace std;

class Node {
public:
	int val;
	Node* left;
	Node* right;
	Node* next;

	Node() : val(0), left(NULL), right(NULL), next(NULL) {}

	Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

	Node(int _val, Node* _left, Node* _right, Node* _next)
		: val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
	Node* connect(Node* root) {
		queue<Node*> curLevel;
		queue<Node*> nextLevel;
		if (root == nullptr)
		{
			return root;
		}
		if (root->left != nullptr)
		{
			nextLevel.push(root->left);
		}
		if (root->right != nullptr)
		{
			nextLevel.push(root->right);
		}

		while (nextLevel.size() != 0)
		{
			curLevel = std::move(nextLevel);
			nextLevel = queue<Node*>();

			Node* priorNode = nullptr;
			while (!curLevel.empty())
			{
				Node * tmpNode = curLevel.front();
				curLevel.pop();
			
				if (tmpNode->left != nullptr)
				{
					nextLevel.push(tmpNode->left);
				}
				if (tmpNode->right != nullptr)
				{
					nextLevel.push(tmpNode->right);
				}


				if (priorNode == nullptr)
				{
					priorNode = tmpNode;
				}
				else
				{
					priorNode->next = tmpNode;
					priorNode = tmpNode;
				}
			}
		}

		return root;
	}
};
