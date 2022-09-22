//Node Class
public class Node{
    int data;
    Node next;
    
    public Node(int tempData){
        data = tempData;
    }
    
    public int getData(){
        //Returns the data from the node
        return data;
    }
    
    public Node getNext(){
        //Returns the next node
        return next;
    }
}