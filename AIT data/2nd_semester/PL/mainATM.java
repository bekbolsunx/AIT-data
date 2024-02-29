// import java.util.Scanner;

// class User {
//     String name, currency;
//     int balance;

//     public User() {
//         this.name = "";
//         this.currency = "";
//         this.balance = 0;
//     }

//     public User(String name, String currency, int balance) {        
//         this.name = name;
//         this.currency = currency;
//         this.balance = balance;
//     }

//     public void show() {
//         String info = "Name: " + name + "\n" + "Currency: " + currency + "\n" + "Balance: " + balance;
//         System.out.println();
//         System.out.println(info);
//         System.out.println();
//     }

//     public void updateBalance() {
//         if (this.currency.equalsIgnoreCase("dollar")) {
//             this.balance = this.balance * 89;
//         }
//         if (this.currency.equalsIgnoreCase("euro")) {
//             this.balance = this.balance * 95;
//         }
//         // Add more currencies as needed
//     }
// }

// class ATM {
//     int totalTransactions = 0;

//     public void withdraw(User user, String currency, int amount) {
//         switch (currency.toLowerCase()) {
//             case "dollar":
//                 if (user.balance >= amount) {
//                     user.balance -= amount;
//                     System.out.println("Withdrawal successful. New balance: " + user.balance);
//                     totalTransactions++;
//                 } else {
//                     System.out.println("Insufficient balance.");
//                 }
//                 break;
//             case "euro":
//                 if (user.balance >= amount) {
//                     user.balance -= amount;
//                     System.out.println("Withdrawal successful. New balance: " + user.balance);
//                     totalTransactions++;
//                 } else {
//                     System.out.println("Insufficient balance.");
//                 }
//                 break;
//             // Add more cases for different currencies
//             default:
//                 System.out.println("Invalid currency.");
//         }
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         User user1 = new User("John Doe", "dollar", 1000);
//         user1.show();

//         ATM atm = new ATM();
//         atm.withdraw(user1, "dollar", 500);
//         user1.updateBalance();
//         user1.show();
//     }
// }

// import java.util.Scanner;

class User {
    String name, currency;
    int balance;

    public User() {
        this.name = "";
        this.currency = "";
        this.balance = 0;
    }

    public User(String name, String currency, int balance) {
        this.name = name;
        this.currency = currency;
        this.balance = balance;
    }

    public void show() {
        String info = "Name: " + name + "\n" + "Currency: " + currency + "\n" + "Balance: " + balance;

        System.out.println();
        System.out.println(info);
        System.out.println();
    }

    public void updateBalance() {
        if (this.currency.equalsIgnoreCase("dollar")) {
            this.balance = this.balance * 89;
        }
        if (this.currency.equalsIgnoreCase("euro")) {
            this.balance = this.balance * 95;
        }
        //add more currencies as needed
    }
}

class ATM {
    int totalTransactions = 0;

    public void withdraw(User user, String currency, int amount) {
        switch (currency.toLowerCase()) {
            case "dollar":
                if (user.balance >= amount) {
                    user.balance -= amount;
                    System.out.println("(Withdrawal)New balance: " + user.balance);
                    totalTransactions =+ 1;
                } else {
                    System.out.println("ERROR");
                }
                break;
            case "euro":
                if (user.balance >= amount) {
                    user.balance -= amount;
                    System.out.println("(Withdrawal)New balance: " + user.balance);
                    totalTransactions =+ 1;
                } else {
                    System.out.println("ERROR");
                }
                break;
            //add more cases for different currencies
            default:
                System.out.println("Invalid currency.");
        }
    }
}

public class mainATM {
    public static void main(String[] args) {
        User user1 = new User("Bekbolsun Ibragimov", "dollar", 10000);
        user1.show();

        ATM atm = new ATM();
        atm.withdraw(user1, "dollar", 500);
        user1.updateBalance();
        user1.show();
    }
}