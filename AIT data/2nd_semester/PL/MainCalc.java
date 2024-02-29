class BaseCalc 
{
    public void add(int a , int b){
        System.out.println(a+b);
    }
    public void show(int a , int b){
        System.out.println("I'm in BaseCalc)))");
    }

}

class MathCalc extends BaseCalc
{
    public void sqrt(int a){
        System.out.println(Math.sqrt(a));
    }

    public void add(int a , int b){
        System.out.println(a+b);

    }

    public void show(int a , int b ){
        System.out.println("I'm in MathCalc)))");
    }
    

}

public class MainCalc
{
    public static void main(String[] args) {
        BaseCalc bek = new MathCalc();
        bek.add(6, 8);
        MathCalc obj = new MathCalc();
        obj.sqrt(8);
        bek.add(89, 11);
        bek.show(0, 0);

    
        
    } 
} 