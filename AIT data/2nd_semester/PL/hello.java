// import javax.swing.plaf.TreeUI;

// class Hello
// {
//     // public static double harmonic(int n)
//     // {
//     //     double sum  = 0.0;
//     //     for (int i = 1; i < n; i++)
//     //         sum += 1.0/i;
//     //     return sum;
//     // }










//     public static void main(String[] args)



//     {
//         // double d = 0;
//         // d = harmonic(5);

//         //1 exercise
//         System.out.println("Hello world");

//         //2 exercise power of 2^
//             int n = 5;          // this variable for control the num of iterations 
//             long power = 1;      // 2^0 =1 . itaration starts with o , in total we have 6 itarations in example of 5
//         for (int i = 0; i <= n; i++)  
//     {
//         System.out.println(i + " " + power);
//         power = 2*power;
//     }


//         // 3 exercise boolean
//         boolean p = false;
//         boolean q = true;
//         if (q && p ) System.out.println("Yay");
//         else System.out.println("Nay");

//         // 4 exercise . Basic while loop
//         int v = 9;
//         while (power <= v/2)
//         {
//             power = 2*power;
//         }
//         System.out.println(power);

//         // 5 exercise Do - while loop. 1st its check and after do.
//         double x = 0.0;
//         double y = 0.0;

//         do
//         {
//             x = 2.0*Math.random() - 1.0;                 //this 2 lines chek 
//             y = 2.0*Math.random() - 1.0;
//         } 
//         while (Math.sqrt(x*x + y*y) > 1.0);           // this lines after starts to itarate 
//         System.out.println(x);




//         //6 exercise
        // int day = 3;
        // switch (day) 
        // {
        //     case 0: System.out.println("Sun"); break;
        //     case 1: System.out.println("Mon"); break;
        //     case 2: System.out.println("Tue"); break;
        //     case 3: System.out.println("Wed"); break;
        //     case 4: System.out.println("Thu"); break;
        //     case 5: System.out.println("Fri"); break;
        //     case 6: System.out.println("Sat"); break;
        // }
        // System.out.println(day);

//         //7 
//         int a = 29;
//         int b = 52;
//         int sum = 0;
//         int ns = 100;

//         for (int i = 0; i <= ns; i++)
//         {
//             sum += a + b;
//         }
//         System.out.println(sum%10);
  
//         // 8 create array 

//         int n1 = 9;
        
//         double[] a2 = new double[n1];
//         for (int i = 0; i < n1; i++) a2[i] = Math.random();
        
//         for (int i = 0; i < n1; i++) System.out.println(a2[i]);    
//     }
// }
