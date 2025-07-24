class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            while (charSet.contains(currentChar)) {
                charSet.remove(s.charAt(left));
                left++;
            }
            charSet.add(currentChar);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}

//OR, My Submission (above recommended for better clarity)

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        Set<Character> charSet = new HashSet<>();
        int maxLength = 0;
        for (int right = 0; right < s.length(); right++) {
            if (charSet.contains(s.charAt(right))) {
                maxLength = Math.max(maxLength, right - left);
                while (s.charAt(left) != s.charAt(right)) {
                    charSet.remove(s.charAt(left));
                    left++;
                }
                left++;
            }
            charSet.add(s.charAt(right));
        }

        return Math.max(maxLength, s.length() - left);
    }
}