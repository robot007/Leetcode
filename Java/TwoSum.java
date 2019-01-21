public class Solution
{
    
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    
    public static void main(String[] arg)
    {
        int[] nums = {2,7,11,5};
        Solution sol = new Solution();
        int[] ret = sol.twoSum(nums, 12);
        
        System.out.println(ret[0]);
        System.out.println(ret[1]);
    }
}
