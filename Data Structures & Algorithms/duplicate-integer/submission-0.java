class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet <Integer> lookup = new HashSet<>();
        for(int i = 0; i < nums.length; i++)
        {
            if(!lookup.add(nums[i]))
                return true;
        }
        return false;

    }
}
