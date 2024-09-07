class Solution {
    public int[][] merge(int[][] intervals) {
//        Arrays.sort(intervals, Comparator.comparingInt(interval->interval[0]));
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        
        List<int[]> lst = new ArrayList<>();
        int start = intervals[0][0];
        int end = intervals[0][1];
        for(int i = 1;i<intervals.length;i++){
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            if(end >= currStart){
                end = Math.max(currEnd, end);
            } else {
                lst.add(new int[]{start, end});
                start = currStart;
                end = currEnd;
            }
        }
        lst.add(new int[]{start, end});
        return lst.toArray(new int[lst.size()][]);
    }
}