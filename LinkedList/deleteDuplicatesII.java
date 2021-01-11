public ListNode deleteDuplicates(ListNode head) {
    ListNode current = head;
    ListNode previous = null;
    while(current != null && current.next != null){
        if(current.val == current.next.val){
            int value = current.val;
            ListNode temp = current;
            while(temp != null && temp.val == value){
                temp = temp.next;
            }
            if(previous == null) head = temp;
            else previous.next = temp;
            current = temp;
        }else{
            previous = current;
            current = current.next;
        }
    }
    return head;
}