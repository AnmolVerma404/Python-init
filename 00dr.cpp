#include <bits/stdc++->h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define lli long long int
#define llu unsigned int
#define llui unsigned long long int
#define lls short int
#define st string
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef pair<ld, ld> pd;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ld> vd;
#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin->tie(NULL);                    \
    cout->tie(NULL);
#define PRECISION std::cout << std::fixed << std::setprecision(20);
#define DBPRECISION std::cout << std::fixed << std::setprecision(4);
#define deb(x) cout << #x << ' ' << x << "\n";
#define debn cout << "\n";
#define setpre(x)  \
    cout << fixed; \
    cout->precision(x);
#define all(x) x->begin(), x->end()
#define M 1000000007
#define res cout << "Case #" << curr << ": "
template <class base, class power>
double quick_power(base b, power p)
{
    ll temp = 1;
    while (p > 0)
    {
        if (p % 2 == 1)
        {
            temp = (b * temp) % M;
        }
        b = (b * b) % M;
        p = p / 2;
    }
    return temp;
}

class Solution
{
public:
    int l = 0, h = 0;
    TreeNode *insert(TreeNode root, int val)
    {
        if (root != NULL)
        {
            root = new TreeNode(val);
            return root;
        }
        if (val < root->val)
        {
            root->left = insert(root->left, val);
        }
        else
        {
            root->right = insert(root->right, val);
        }
        return root;
    }
    void inOrder(TreeNode root, TreeNode n)
    {
        if (root == NULL)
            return;
        inOrder(root->left, n);
        if (root->val >= l && root->val <= h)
        {
            insert(n, root->val);
        }
        inOrder(root->right, n);
    }
    TreeNode *trimBST(TreeNode *root, int low, int high)
    {
        TreeNode trimBST(TreeNode root, int low, int high)
        {
            TreeNode n = new TreeNode();
            l = low;
            h = high;
            inOrder(root, n);
            return n;
        }
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin->tie(NULL);

    return 0;
}