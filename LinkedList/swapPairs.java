public ListNode swapPairs(ListNode head) {
    if(head == null || head.next == null) return head;
    ListNode current = head;
    ListNode previous = null;
    int index = 0;
    while(current != null){
        if(index % 2 == 0 && current.next != null){
            ListNode temp = current.next;
            if(previous != null){
                previous.next = current.next;
                current.next = current.next.next;
                temp.next = current;
            }else{
                current.next = current.next.next;
                temp.next = current;
                head = temp;
                
            }
            index += 2;
        }else{
            index++;
        }
        previous = current;
        current = current.next;
        
    }
    return head;
}