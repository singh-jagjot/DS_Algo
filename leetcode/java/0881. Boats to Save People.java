class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0, right = people.length - 1;
        int boats = 0;

        while (left <= right) {
            // Try to pair the lightest and heaviest person remaining
            if (people[left] + people[right] <= limit) {
                left++;
            }
            // If people[right] > limit, they must go alone.
            right--;
            // Need additional boat everytime.
            boats++;
        }

        return boats;
    }
}
