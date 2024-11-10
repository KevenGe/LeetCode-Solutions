针对[本问题](https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/)，首先可以分析每次切割会造成什么后果。可以发现，分割后形成了两个独立且与父问题相似的子问题，因此，为避免重复计算，我们可以考虑通过**动态规划**或**缓存**的方式优化。

首先,为了对$cuts$有个全面的认知，对$cuts$进行排序并对两侧分别加入边缘长度$0$和$n$，即$cuts = [0] + \mathbf{sorted}    (cuts) + [n]$。

我们可以理解$dp[i][j]$为第$i$段线段和第￥j$段线段完全结合的需要的代价，然后可以有如下公式。
$$
dp[i][j] = \max_{z\in(i,j-1)}{(dp[i][z] + dp[z+1][j])} + (cuts[j+1] - cuts[i])
$$
