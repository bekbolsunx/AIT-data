

public class LRU
{
    // public static void main(String[] args) {
        // int a = 25;
        // int b = 5;

        // int sum = a + b;
        // int diff = a - b;
        // int prod = a * b;
        // double avg = (a + b) / 2;

        // int min = Math.min(a , b);
        // int max = Math.max(a , b);


        // System.out.println("Sum of two integers:" + sum);
        // System.out.println("Difference of two integers:"+ diff);
        // System.out.println("Product of two integers:" + prod);
        // System.out.println("Average of two integers:" + avg);
        // System.out.println("Max integer:" + max);
        // System.out.println("Min integer:" + min);


        // public static void main(String[] args) {


        //     int tar = 1;
            
        //     for (int i = 0; i <= 5; i++) {
        //         for (int j = 0; j <= i; j++) {
        //             System.out.print(tar + " ");
        //             tar ++;
        //         }
        //         System.out.println();
        //     }

        // }
        // int tar = 10;
            
        // for (int i = 0; i <= tar; i++) {
        //     for (int j = 0; j <= i; j++) {
        //         System.out.print(i);
        //     }
        //     System.out.println();
        // }


}

// abstract class Animal {

//      void eat(){
//         System.out.println("Programmer");
//     }

//     public void  getSalary(){}


//     class Lion extends Animal{
//         @Override
//         void eat(){}

//         public void sleep(){}

//     class Tiger extends Animal{
//         @Override
//         void eat(){}

//         public void sleep(){}

//     }
//     class Deer extends Animal{
//         @Override
//         void eat(){}

//         public void sleep(){}
//     }

//     }
// }


interface Sortable{

    void sort();

}

class BubleSort implements Sortable{
    int[] arr = {1,2,3,4,5};

    public void sort(){
        System.out.println("This is buble sort method:" + arr);
    }
}

class SelectionSort implements Sortable{
    int[] arr = {2,3,4,5};

    public void sort(){
        System.out.println("This is selection sort method:" + arr);
    }
}

class exArr{

    public static void main(String[] args) {
        pairs(new int[]{14, -15, 9, 16, 25, 45, 12, 8}, 30);
    }

    static void pairs(int[] inputArr , int inputNm){

        for (int i = 0; i <inputArr.length; i++){
            for (int j = i + 1; j < inputArr.length; j++){
                if (inputArr[i] + inputArr[j] == inputNm){
                    System.out.print("1)"+inputArr[i] + "+"+ inputArr[j] +"="+ inputNm+" 2)");
                }

            }
        }
    }

}

           ////////////////////////EXERCISE/////////////////////////
//1
//22
//333      
        //int tar = 10;
            
           // for (int i = 0; i <= tar; i++) {
              // for (int j = 0; j <= i; j++) {
                  //  System.out.print(i);
               // }
               // System.out.println();
           // }
       // }



           ////////////////////////EXERCISE 2 /////////////////////////
//1
//2 3
//4 5 6  
        // int start = 1;

           // for (int i = 0; i <= 5; i++) {
               //for (int j = 0; j <= i; j++) {
                   //  System.out.print(start + " ");
                 //    start ++;
               //  }
            //    System.out.println();
          

  
        
        ////////////////////////BASIC//////////////////////////////
        // import java.util.ArrayList;
        // import java.util.List;
        // import java.util.Collections;
        
        //         class Employee{
        
        //      void work(){
        //         System.out.println("Programmer");
        //     }
        
        //     public void  getSalary(){}
        
        
        //     class HRmanager extends Employee{
        //         @Override
        //         void work(){}
        
        //         public void addEmployee(){}
        
        //     }
        //     }
                    
        //             /////////////////////////////ABSTRACT////////////////////////////
        //     abstract class Animal {
        
        //         abstract void eat();
                    
        
        //         public void  getSalary(){}
            
            
        //     }
        
        //     class Lion extends Animal{
        //         //@Override
        //         void eat(){}
        
        //         public void sleep(){}
                
        //     }
           
        
        //     class Tiger extends Animal{
        //         //@Override
        //         void eat(){}
        
        //         public void sleep(){}
        
        //     }
                
        //     class Deer extends Animal{
        //         //@Override
        //         void eat(){}
        
        //         public void sleep(){}
        
        //     }
        
        //             ////////////////////////////INTERFACE///////////////////////////////
        //   interface Sortable{
        
        //     void sort();
        
        // }
        
        // class BubleSort implements Sortable{
        //     int[] arr = {1,2,3,4,5};
        
        //     public void sort(){
        //         System.out.println("This is buble sort method:" + arr);
        //     }
        // }
        
        // class SelectionSort implements Sortable{
        //     int[] arr = {2,3,4,5};
        
        //     public void sort(){
        //         System.out.println("This is selection sort method:" + arr);
        //     }
        // }
        //            ///////////////////////////ARRAY///////////////////////////////////
        
        
        
        // class Main {
        //     public static void main(String[] args) {
        //         List<String> l1 = new ArrayList<>();
        //         l1.add("A");
        //         l1.add("B");
        
        //         List<String> l2 = new ArrayList<>();
        //         l2.add("C");
        //         l2.add("D");
        
                
        //         l1.addAll(l2);
        
        //         //System.out.println(l1);
                
                
        //         ArrayList<String> org = new ArrayList<>();
        //         org.add("apple");
        //         org.add("pineapple");
                
        //         ArrayList<String> clone = new ArrayList<>(org);
                
                
        //         System.out.print("Original "+org);
        //         System.out.print("Cloned "+clone);
                
                
        //         org.removeAll(org);
                
        //         System.out.print("Empty list "+org);
                
                
        //     }
        // }
                
                // pairs(new int[]{14, -15, 9, 16, 25, 45, 12, 8}, 30);
        
        
            // static void pairs(int[] inputArr , int inputNm){
        
               // for (int i = 0; i <inputArr.length; i++){
                  //  for (int j = i + 1; j < inputArr.length; j++){
                     //   if (inputArr[i] + inputArr[j] == inputNm){
              // System.out.print("1)"+inputArr[i] + "+"+ inputArr[j] +"="+ inputNm+" 2)");
                       // }
        
                     //}
                //}
            //}
        //}

class Main{
    public static void main(String[] args) {
        
        
    }
}
