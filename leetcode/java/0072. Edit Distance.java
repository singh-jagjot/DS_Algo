class Solution {
    public int minDistance(String word1, String word2) {
        String big, small;
        if(word1.length()>word2.length()){
            big=word1;
            small=word2;
        }else if(word2.length()>word1.length()){
            big=word2;
            small=word1;
        }else{
            big=word1;
            small=word2;
        }
        int [] pre = new int[1+small.length()];
        int [] curr = new int[1+small.length()];

        for (int i=0;i<pre.length;i++){
            pre[i]=i;
        }
        for(int i=0;i<big.length();i++){
            curr[0]=i+1;
            for(int j=0;j<small.length();j++){
                if(big.charAt(i)==small.charAt(j)){
                    curr[j+1]=pre[j];
                }else{
                    curr[j+1]=1+Math.min(curr[j], Math.min(pre[j], pre[j+1]));
                }
            }
            for(int j=0;j<curr.length;j++) pre[j]=curr[j];
        }
        return curr[curr.length-1];
    }
}