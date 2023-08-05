/*
 * @lc app=leetcode id=21 lang=java
 *
 * [21] Merge Two Sorted Lists
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (62.76%)
 * Likes:    18686
 * Dislikes: 1738
 * Total Accepted:    3.3M
 * Total Submissions: 5.2M
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * You are given the heads of two sorted linked lists list1 and list2.
 * 
 * Merge the two lists in a one sorted list. The list should be made by
 * splicing together the nodes of the first two lists.
 * 
 * Return the head of the merged linked list.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: list1 = [1,2,4], list2 = [1,3,4]
 * Output: [1,1,2,3,4,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: list1 = [], list2 = []
 * Output: []
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: list1 = [], list2 = [0]
 * Output: [0]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in both lists is in the range [0, 50].
 * -100 <= Node.val <= 100
 * Both list1 and list2 are sorted in non-decreasing order.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                cur.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                cur.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            cur = cur.next;
        }

        if (list1 != null) {
            cur.next = list1;
        } else {
            cur.next = list2;
        }

        return dummy.next;
    }
}
// @lc code=end
