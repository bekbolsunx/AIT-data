
// import java.util.Scanner;

// class Calculator {
//     double a, b;
//     String name;

//     public Calculator() {
//         this.name = "";
//     }
//     public Calculator(String str) {
//         this.name = str;
//     }

//     public double add(double a, double b) {
//         return a + b;
//     }
//     public double subtract(double a, double b) {
//         return a - b;
//     }
//     public double multiply(double a, double b) {
//         return a * b;
//     }
//     public double division(double a, double b) {
//         if(b == 0) {
//             System.out.println("Error: Division by zero");
//             return 0;
//         }
//         return a / b;
//     }
// }

// public class helpCalc {
//     public static void main(String[] args) {
//         Calculator calc = new Calculator();
        
//         Scanner scan = new Scanner(System.in);
        
//         System.out.print("Enter first number : ");
//         double a = scan.nextDouble();

//         scan.nextLine(); // Consume the newline left-over

//         System.out.print("Enter operation (+, -, *, /) : ");
//         String op = scan.nextLine();

//         System.out.print("Enter second number : ");
//         double b = scan.nextDouble(); 
        
//         scan.close();
        
//         switch (op.trim()) {
//             case "+":
//                 System.out.println("Result: " + calc.add(a, b));
//                     break;
//             case "-":
//                 System.out.println("Result: " + calc.subtract(a, b));
//                     break;
//             case "*":
//                 System.out.println("Result: " + calc.multiply(a, b));
//                     break;
//             case "/":
//                 if (b == 0) {
//                     System.out.println("Error: Division by zero");
//                 } else {
//                     System.out.println("Result: " + calc.division(a, b));
//                 }
//                 break;
//             default:
//                 System.out.println("Invalid operation");
//                 break;
//         }
//     }
// }
