class Solution {
    public int threeSumMulti(int[] numList, int target) {
        Arrays.sort(numList);
        int mod = 1_000_000_007;
        int length = numList.length;
        long returnNum = 0;
        for (int i=0; i<length-2; i++){
            int middle = i + 1;
            int end = length -1;
            while (middle<end){
                int sum = numList[i]+numList[middle]+numList[end];
                if (sum<target){
                    middle ++;
                }else if (sum>target){
                    end --;
                }else if (numList[middle] == numList[end]){
                    int interval = end-middle+1;
                    returnNum += interval*(interval-1)/2;
                    returnNum %= mod;
                    break;
                }
                else {
                    int mid_num = 1;
                    int end_num = 1;
                    while(middle+1<end && numList[middle]==numList[middle+1]){
                        mid_num ++;
                        middle ++;
                    }
                    while(end-1>middle && numList[end]==numList[end-1]){
                        end_num ++;
                        end --;
                    }
                    end --;
                    middle ++;
                    returnNum += mid_num*end_num;
                    returnNum %= mod;
                }
            }
        }
        return (int)returnNum;
    }
}