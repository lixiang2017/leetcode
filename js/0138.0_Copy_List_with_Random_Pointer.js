/*
Runtime: 60 ms, faster than 36.03% of JavaScript online submissions for Copy List with Random Pointer.
Memory Usage: 44.4 MB, less than 7.51% of JavaScript online submissions for Copy List with Random Pointer.
*/
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head, cachedNode = new Map()) {
    if (head == null) {
        return null;
    }
    if (!cachedNode.get(head)) {
        cachedNode.set(head, {val: head.val});
        Object.assign(cachedNode.get(head), 
                      {next: copyRandomList(head.next, cachedNode),
                       random: copyRandomList(head.random, cachedNode)});
    }
    return cachedNode.get(head);
};


/*
Runtime: 38 ms, faster than 99.81% of JavaScript online submissions for Copy List with Random Pointer.
Memory Usage: 43.6 MB, less than 79.94% of JavaScript online submissions for Copy List with Random Pointer.
*/
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    if (head == null) {
        return null;
    }
    for (let node = head; node != null; node = node.next.next) {
        const nodeNew = new Node(node.val, node.next, null);
        node.next = nodeNew;
    }
    for (let node = head; node != null; node = node.next.next) {
        const nodeNew = node.next;
        nodeNew.random = (node.random != null) ? node.random.next : null;
    }
    const headNew = head.next;
    for (let node = head; node != null; node = node.next) {
        const nodeNew = node.next;
        node.next = node.next.next;
        nodeNew.next = (nodeNew.next != null) ? nodeNew.next.next : null;
    }
        
    return headNew;
};

