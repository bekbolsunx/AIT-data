import java.util.Scanner;

public class bill 
{
    public static void main(String[] args) 
    {
        double bill,tax,service,res;
        Scanner scan = new Scanner( System.in);
        System.out.print("Enter ur bill : ");
        bill = scan.nextInt();

        tax = bill*9./100;
        service = bill*15./100;
        res = tax + service + bill;

        scan.close();

        System.out.println("Total bill with (tax,service) : " + res);


    }
}
