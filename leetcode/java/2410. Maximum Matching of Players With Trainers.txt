class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);

        int pIdx = 0;
        int tIdx = 0;

        int matchings = 0;
        while (pIdx < players.length && tIdx < trainers.length) {
            if(players[pIdx] <= trainers[tIdx]){
                pIdx++;
                matchings++;
            }
            tIdx++;
        }

        return matchings;
    }
}