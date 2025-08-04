class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalTank = 0;
        int currTank = 0;
        int start = 0;

        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            totalTank += diff;
            currTank += diff;

            // If we can't reach next station from current start, reset
            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }

        // If the totalTank < 0 then the trip is not possible
        return totalTank >= 0 ? start : -1;
    }
}

// May submission but above is recommended
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalDiff = 0;
        for (int i = 0; i < gas.length; i++) {
            totalDiff += gas[i] - cost[i];
        }

        if(totalDiff < 0) return -1;

        int tank;
        int currStation = 0;
        int station  = -1;

        while (currStation < gas.length){
            if(gas[currStation] >= cost[currStation]) {
                tank = 0;
                station = currStation;
                while (currStation < gas.length && tank + gas[currStation] >= cost[currStation]) {
                    tank += gas[currStation] - cost[currStation];
                    currStation++;
                }
            }
            currStation++;
        }
        return station;
    }
}