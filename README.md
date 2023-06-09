# my_leetcode

1. **Two Sum**

   Given an array of integers nums and an integer target, return indices of the
   two numbers such that they add up to target.

   You may assume that each input would have exactly one solution, and you may
   not use the same element twice.

   You can return the answer in any order.

        Example 1:
        
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        
        Example 2:

        Input: nums = [3,2,4], target = 6
        
        Output: [1,2]
        
        Example 3:
        
        Input: nums = [3,3], target = 6
        Output: [0,1]

___

14. **Roman to Integer**

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D
    and M.

Symbol Value

* I 1
* V 5
* X 10
* L 50
* C 100
* D 500
* M 1000

For example, 2 is written as `II` in Roman numeral, just two ones added
together. 12 is written as `XII`, which is simply `X` + `II`. The number 27 is
written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not `IIII`. Instead, the number four is
written
as `IV`. Because the one is before the five we subtract it making four. The
same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

`I` can be placed before `V` (5) and X (10) to make 4 and 9.
`X` can be placed before `L `(50) and `C` (100) to make 40 and 90.
`C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

    Example 1:
    
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

    Example 2:
    
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

    Example 3:
    
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

___

9. **Palindrome Number**

   Given an integer x, return true if x is a
   palindrome, and false otherwise.

         Example 1:
         
         Input: x = 121
         Output: true
         Explanation: 121 reads as 121 from left to right and from right to left.
         
         Example 2:
         
         Input: x = -121
         Output: false
         Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

         Example 3:
      
         Input: x = 10
         Output: false
         Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

___

14. **Longest Common Prefix**

    Write a function to find the longest common prefix string amongst an array
    of strings.

    If there is no common prefix, return an empty string "".

___

20. Valid Parentheses

    Given a string s containing just the
    characters '(', ')', '{', '}', '[' and ']', determine if the input string
    is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

___

21. **Merge Two Sorted Lists**

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by
    splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

___

26. Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same. Then return the
    number of unique elements in nums.

    Consider the number of unique elements of nums be k, to get accepted, you
    need to do the following things:

    Change the array nums such that the first k elements of nums contain the
    unique elements in the order they were present in nums initially. The
    remaining elements of nums are not important as well as the size of nums.
    Return k.

___

27. Remove Element

    Given an integer array nums and an integer val, remove all occurrences of
    val in nums in-place. The order of the elements may be changed. Then return
    the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to
    get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the
    elements which are not equal to val. The remaining elements of nums are not
    important as well as the size of nums.
    Return k.

___

