import java.util.*;
class LongestSub {
    public static int longestSub(String s, String b, int n, int m, int[][] dp){
        if(n < 0 || m < 0){
            return 0;
        }

        if(dp[n][m] != -1){
            return dp[n][m];
        }
        int x = 0, y = 0;

        if(s.charAt(n) == b.charAt(m)){
            x = 1 + longestSub(s, b, n - 1, m - 1, dp);
        }

        else{
            y = Math.max(longestSub(s, b, n - 1, m, dp), longestSub(s, b, n, m - 1, dp));
        }
        return dp[n][m] = Math.max(x, y);
    }
    public static void main(String[] args) {
        String s = "abba";
        String b = "abb";
        int n = s.length();
        int m = b.length();

        int[][] dp = new int[n][m];

        for(int[] a: dp){
            Arrays.fill(a, -1);
        }

        int ans =  longestSub(s, b, n - 1, m - 1, dp);

        System.err.println(ans);
    }

    
}