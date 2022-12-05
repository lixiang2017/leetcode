/*
Runtime: 132 ms, faster than 59.25% of C# online submissions for Middle of the Linked List.
Memory Usage: 36.7 MB, less than 55.68% of C# online submissions for Middle of the Linked List.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        var slow = head;
        var fast = head;
        while (fast?.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}



/*
Runtime: 144 ms, faster than 31.32% of C# online submissions for Middle of the Linked List.
Memory Usage: 36.7 MB, less than 41.92% of C# online submissions for Middle of the Linked List.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        ListNode mid = head;
        int count = 1;
        while (head.next != null) {
            head = head.next;
            count += 1;
            if (count % 2 == 0) {
                mid = mid.next;
            }
        }
        return mid;
    }
}


/*
Runtime: 121 ms, faster than 71.40% of C# online submissions for Middle of the Linked List.
Memory Usage: 36.6 MB, less than 70.29% of C# online submissions for Middle of the Linked List.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        List<ListNode> nodes = new List<ListNode>();
        while (head != null) {
            nodes.Add(head);
            head = head.next;
        }
        return nodes[nodes.Count / 2];
    }
}


/*
Runtime: 160 ms, faster than 8.19% of C# online submissions for Middle of the Linked List.
Memory Usage: 36.5 MB, less than 70.29% of C# online submissions for Middle of the Linked List.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        ListNode? slow = head;
        ListNode? fast = head?.next;
        while (fast is not null) {
            slow = slow.next;
            fast = fast.next?.next;
        }
        return slow;
    }
}
