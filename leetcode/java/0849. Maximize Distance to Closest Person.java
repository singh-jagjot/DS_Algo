class Solution {

    public int maxDistToClosest(int[] seats) {
        int maxDist = 0;
        int prev = -1;

        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 1) {
                if (prev == -1) {
                    // Leading zeros
                    maxDist = i;
                } else {
                    // Zeros between two occupied seats
                    int dist = (i - prev) / 2;
                    maxDist = Math.max(maxDist, dist);
                }
                prev = i;
            }
        }

        // Trailing zeros
        maxDist = Math.max(maxDist, seats.length - 1 - prev);

        return maxDist;
    }
}

// OR

class Solution {

    public int maxDistToClosest(int[] seats) {
        int left = 0, right = seats.length - 1;
        int currMaxDistance = -1;

        if (seats[left] == 0) {
            while (seats[left] == 0) {
                left++;
            }
            currMaxDistance = left;

        }

        if (seats[right] == 0) {
            while (seats[right] == 0) {
                right--;
            }
            currMaxDistance = Math.max(currMaxDistance, seats.length - right -1);
        }

        int upper = right;
        while (left < upper) {
            right = left+1;
            while (right < upper && seats[right] == 0) {
                right++;
            }

            // No need for the below commented logic as the other logic gives the same output.
            // int space = right - left -1;
            // currMaxDistance = Math.max(currMaxDistance, (int) Math.round(space/2.0));

            int space = right - left;
            currMaxDistance = Math.max(currMaxDistance, space/2);
            left = right;
            right++;
        }

        return currMaxDistance;
    }
}