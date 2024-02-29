public class StringPart
{
    public static void main (String[] args )
    {
        String str;
        int    len;

        str = new String("Bekbolsun Ibragimov");

        String str2;
        str2 = str.toUpperCase(); 

        len = str.length();

        System.out.println("The length is :" + len );
        System.out.println("This text type 'UPPER CASE': " + str2);
    }
    
}



