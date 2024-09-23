class Trie {
    Map<Character, Trie> children = new HashMap();
    boolean isEnd = false;
}

class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        int n = s.length();
        var root = makeTrie(dictionary);
        var dp = new int[n + 1];

        for (int start = n - 1; start >= 0; start--) {
            dp[start] = dp[start + 1] + 1;
            var node = root;
            for (int end = start; end < n; end++) {
                if (!node.children.containsKey(s.charAt(end))) {
                    break;
                }
                node = node.children.get(s.charAt(end));
                if (node.isEnd) {
                    dp[start] = Math.min(dp[start], dp[end + 1]);
                }
            }
        }

        return dp[0];
    }

    public Trie makeTrie(String[] dictionary) {
        var root = new Trie();
        for (var word : dictionary) {
            var node = root;
            for (var c : word.toCharArray()) {
                node.children.putIfAbsent(c, new Trie());
                node = node.children.get(c);
            }
            node.isEnd = true;
        }
        return root;
    }
}