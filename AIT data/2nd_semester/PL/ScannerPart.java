import java.util.Scanner;

public class ScannerPart
{
    public static void main(String[] args)
    {
        String inData;
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter smth:");
        inData = scan.nextLine();

        System.out.println("You entered:" + inData);
        scan.close();


    }

}