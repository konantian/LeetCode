public ListNode swapNodes(ListNode head, int k) {
    if(head.next == null) return head;
    
        ListNode left = null;
        ListNode right = head;
    
        ListNode tail = head;
        for(int i = 0;i < k;i++){
            left = tail;
            tail = tail.next;
        }
        while(tail != null){
            right = right.next;
            tail = tail.next;
        }
        int temp = left.val;
        left.val = right.val;
        right.val = temp;
        return head;
}
