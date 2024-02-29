import java.util.*;

public class ArrayListEgThree
{
    public static void main(String[] args) 
    {
        //creating an Array List which holds references to String
        ArrayList<String> names = new ArrayList<>();

        //Adding new members
        names.add("Bek");
        names.add("Korn");
        names.add("Joe");
        // accessing and print out the objects
        for (int i= 0; i <names.size(); i ++);
            System.out.println("Index of member : " + 1 + " Name : " + names.get(1));

        //replace Joe wiht Zoe 
        names.set(2, "Zoe"); // index whcih you want to change 2 is name which you want write down 
        System.out.println(names);


        Deque<Integer> deque = new ArrayDeque<>();
        deque.addFirst(1);
        deque.addFirst(2);
        deque.addLast(3);
        deque.addLast(4);

        int first = deque.removeFirst(); // this variables hold deleted nums
        int last = deque.removeLast();

        System.out.println("First : "+ first + " Last : " + last);
        System.out.println(deque);// what we have in our massive in the end 

        deque.remove(); // pop() both of them removes first nums in massive 
        System.out.println(deque);
    }
}