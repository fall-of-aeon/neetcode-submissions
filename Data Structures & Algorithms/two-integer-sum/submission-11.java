class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> Table = new HashMap<>();
        int[] result = new int[2];
        int difference;
        for(int i = 0; i < nums.length; i++) {
            difference = target - nums[i];
            if(!Table.containsKey(difference))
                Table.put(nums[i],i);
            else
                return new int[] {Table.get(difference),i};

        }
            return result;
        
    }
}