package com.zixiong.leetcode;

/**
 * Created by zixiong on 2018/06/07.
 */
public class MinDistance {

    // 递推的写法
    public int minDistance(String word1, String word2) {
        int rows = word1.length();
        int cols = word2.length();

        int[][] dp = new int[rows + 1][cols + 1];

        for (int i = 0; i <= rows; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= cols; j++) {
            dp[0][j] = j;
        }

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                }
            }
        }
        return dp[rows][cols];
    }

    // 递归的写法
    public int minDistance2(String word1, String word2) {
        int rows = word1.length();
        int cols = word2.length();

        int[][] dp = new int[rows + 1][cols + 1];

        return getDp(dp, rows, cols, word1, word2);
    }

    private int getDp(int[][] dp, int i, int j, String word1, String word2) {
        if (dp[i][j] > 0) {
            return dp[i][j];
        }
        if (i == 0) {
            return j;
        }
        if (j == 0) {
            return i;
        }

        int result;
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
            result = getDp(dp, i - 1, j - 1, word1, word2);
        } else {
            result = getDp(dp, i - 1, j - 1, word1, word2);
            result = Math.min(result, getDp(dp, i - 1, j, word1, word2));
            result = Math.min(result, getDp(dp, i, j - 1, word1, word2));
            result = result + 1;
        }
        dp[i][j] = result;
        return result;
    }

    public static void main(String[] args) {
        MinDistance minDistance = new MinDistance();
        System.out.println("---->" + minDistance.minDistance2("dinitrophenylhydrazine", "benzalphenylhydrazone"));
    }
}
