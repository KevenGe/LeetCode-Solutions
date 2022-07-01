# 1024. 视频拼接
# https://leetcode.cn/problems/video-stitching/


from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [0] + [float("inf")] * time

        for i in range(1, time + 1):
            for clip_idx, clip in enumerate(clips):
                if clip[0] < i <= clip[1]:
                    if clip[0] == 0:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[clip[0]] + 1, dp[i])

        if dp[time] == float("inf"):
            return -1
        else:
            return dp[time]


if __name__ == "__main__":
    so = Solution()
    print(so.videoStitching([[0, 2], [8, 10], [1, 9]], 10))
