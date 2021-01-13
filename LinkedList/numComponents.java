public int numComponents(ListNode head, int[] G) {
    int connected = 0;
    ListNode current = head;
    Set<Integer> Gset = new HashSet();
    for (int x: G) Gset.add(x);
    boolean connect = false;
    while(current != null){
        if(Gset.contains(current.val)){
            if(!connect){
                connect = true;
                connected++;
            }
        }else{
            if(connect) connect = false;
        }
        current = current.next;
    }
    return connected;
}