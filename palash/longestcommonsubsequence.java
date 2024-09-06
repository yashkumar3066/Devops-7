class LongestSub {
    public static int longestSub(String s, String b, int n, int m){
        if(n < 0 || m < 0){
            return 0;
        }

        int x = 0, y = 0;
        if(s.charAt(n) == b.charAt(m)){
            x = 1 + longestSub(s, b, n - 1, m - 1);
        }

        else{
            y = Math.max(longestSub(s, b, n - 1, m), longestSub(s, b, n, m - 1));
        }
        return Math.max(x, y);
    }
    public static void main(String[] args) {
        String s = "abba";
        String b = "babbab";


        int ans =  longestSub(s, b, s.length() - 1, b.length() - 1);

        System.err.println(ans);
    }

    
}