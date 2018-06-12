package com.leetcode.oc;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * leetcode 120
 * Created by zixiong on 2018/06/08.
 */
public class Triangle {

    public int minimumTotal(List<List<Integer>> triangle) {
        int rows = triangle.size();
        int cols = triangle.get(rows - 1).size();
        Integer[][] dp = new Integer[rows][cols];

        return dfs(0, 0, dp, triangle);
    }

    private int dfs(int i, int j, Integer[][] dp, List<List<Integer>> triangle) {
        if (dp[i][j] != null) {
            return dp[i][j];
        }

        int result;
        int value = triangle.get(i).get(j);
        if (i == triangle.size() - 1) {
            result = value;
        } else {
            result = Math.min(
                    dfs(i + 1, j, dp, triangle),
                    dfs(i + 1, j + 1, dp, triangle)
            ) + value;
        }
        dp[i][j] = result;
        System.out.println("---->" + result);
        return result;
    }

    class Solution {
        public int minimumTotal(List<List<Integer>> triangle) {
            int[] dp = new int[triangle.size() + 1];

            for (int i = triangle.size() - 1; i >= 0; i--) {
                List<Integer> list = triangle.get(i);
                for (int j = 0; j < list.size(); j++) {
                    dp[j] = list.get(j) + Math.min(dp[j], dp[j + 1]);
                }
            }
            return dp[0];
        }
    }

    // [[2],[3,4],[6,5,7],[4,1,8,3]]

    public static void main(String[] args) {
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3, 4));
        triangle.add(Arrays.asList(6, 5, 7));
        triangle.add(Arrays.asList(4, 1, 8, 3));
        Triangle triangle1 = new Triangle();
        System.out.println("---->" + triangle1.minimumTotal(triangle));
    }
}
