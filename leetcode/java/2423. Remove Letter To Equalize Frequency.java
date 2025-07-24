class Solution {
    public boolean equalFrequency(String word) {
        int[] freq = new int[26];

        // Step 1: Count frequency of each character
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }

        // Step 2: Try removing one occurrence of each character and check the result
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) continue;

            freq[i]--;  // Try removing one character
            Set<Integer> freqSet = new HashSet<>();
            for (int f : freq) {
                if (f > 0) freqSet.add(f);  // Skip 0s to focus on active characters
            }

            if (freqSet.size() == 1) return true;
            freq[i]++;  // Restore the original frequency
        }

        return false;
    }
}

// OR my submission (Above recommended)

class Solution {
    public boolean equalFrequency(String word) {
        Map<Character, Integer> charMap = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }

        for(var ch: charMap.keySet()){
            charMap.put(ch, charMap.get(ch) - 1);
            Set<Integer> freqSet = new HashSet<>(charMap.values());
            freqSet.remove(0);
            if(freqSet.size() <= 1) return true;
            charMap.put(ch, charMap.get(ch) + 1);
        }
        return false;
    }
}