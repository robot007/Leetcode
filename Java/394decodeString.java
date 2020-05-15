package com.company;

import java.util.*;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Solution sol = new Solution();
        // 394. Decode String
//        assert sol.decodeString("3[a]2[bc]").equals("aaabcbc");
        assert sol.decodeString("3[a2[c]]").equals("accaccacc");
        assert sol.decodeString(("2[abc]3[cd]ef")).equals("abcabccdcdcdef");
//        int ret = sol.No13_romanToInt1("VIII");
//        System.out.println(ret);
//        int[] array = {1,2,3};
//        Vector<Integer> nums = new Vector<Integer> (array); // (Arrays.asList(array));
//        Vector<Vector<int>> ret = sol.No46_permute(&nums);
//        nums.
//        ListIterator itlst = ret.
//        for(vector<int> vet: ret){
//            System.out.println(lst);
//        }
        // 5/1/2020: #394

    }
}

class Solution {
    public int No13_romanToInt1(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1); map.put('V', 5); map.put('X', 10); map.put('L', 50);
        map.put('C', 100); map.put('D', 500); map.put('M', 1000);
        int ret = map.get(s.charAt(s.length()-1));
        System.out.println(s.length());
        for (int i=0; i<s.length()-1; i++) {
            if(map.get(s.charAt(i)) < map.get(s.charAt(i+1)))
                ret -= map.get(s.charAt(i));
            else
                ret += map.get(s.charAt(i));
        }
        return ret;
    }

    /**
    public vector<vector<int>> No46_permute(vector<int> nums){
        List<List<Integer>> list = new LinkedList<>();
        this.helper(nums, 0, list);
        return list;
    }

    public void helper(int[] nums, int index, List<List<Integer>> list) {
        if (index == nums.length) {
            // System.out.println(Arrays.toString(nums));
            List<Integer> one_res = new LinkedList<>();
            for (int i : nums) one_res.add(i);
            list.add(one_res);
            return ;
        }

        for (int i = index; i < nums.length; i++) {
            swap(index, i, nums);
            helper(nums, index+1, list);
            swap(index, i, nums);
        }

    }

    private void swap(int i, int j, int[] nums) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
     **/

    // 394. Decode String
//    Given an encoded string, return its decoded string.
//
//    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed
//    to be a positive integer.
//
//    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
//
//            Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
//
//    Examples:
//
//    s = "3[a]2[bc]", return "aaabcbc".
//    s = "3[a2[c]]", return "accaccacc".
//    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
    public String decodeString(String s){
        int begin = s.indexOf('[');
        if (begin<0)
            return s;
        int end = -1;
        Stack<Character> stack = new Stack<>();
        stack.push('[');
        for (int i=begin+1; i<s.length(); i++){
            char c = s.charAt(i);
            if (c=='[')
                stack.push(c);
            else if (c == ']') {
                if (stack.size() == 1) {
                    end = i;
                    break;
                } else {
                    stack.pop();
                }
            }
        }
        int digitBegin = 0;
        while (! Character.isDigit((s.charAt(digitBegin)))){
            digitBegin++;
        }
        int times=Integer.parseInt(s.substring(digitBegin, begin));
        String str = s.substring(begin+1, end );
        return decodeString(s.substring(0, digitBegin)) + decodeString(str).repeat(times)+decodeString(s.substring(end+1));

    }

}