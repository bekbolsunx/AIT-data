import java.util.Scanner;

public class Pr2 
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        double r , area;

        System.out.print("Print r : ");
        r = scan.nextDouble();

        area = Math.PI * (r * r); // Пr^2

        scan.close();

        System.out.println("The area of circle : " + r + " is " + area);

    }

    
}
