//Linked List Class
public class LinkedList{
    Node head;
    
    public LinkedList(int data){
        head = new Node(data);
    }
    
    public Node getHead(){
        //Returns the first node of the linked list
        return head;
    }
    
    public void append(int value){
        //Appends a node to the tail of a linked list.
        Node temp = head;
        while(temp.getNext() != null){
            temp = temp.next;
        }
        temp.next = new Node(value);
    }
    
    public Node pop(){
        //Removes the tail node from a linked list and returns it
        Node temp = head;
        while(temp.getNext().getNext() != null){
            temp = temp.next;
        }
        Node poppedNode = temp.getNext();
        temp.next = null;
        return poppedNode;
    }
    
    public int size(){
        //Returns the size of the linked list
        Node temp = head;
        int count = 0;
        while(temp != null){
            count++;
            temp = temp.next;
        }
        return count;
    }
    
    public void print(){
        //Prints out the linked list
        Node temp = head;
        while(temp != null){
            System.out.println(temp.getData());
            temp = temp.next;
        }
    }
    
}
