import java.util.Scanner;


class Product {
    String name;
    int price;
    int amount;

    public Product(String name, int price, int amount) {
        this.name = name;
        this.price = price;
        this.amount = amount;
    }

    public void displayCost(int count) {
        System.out.println("Total cost for " + count + " " + name + "(s): " + (price * count));
    }

    public void setAmount(int count) {
        this.amount -= count;
    }

    public boolean isAvailable(int count) {
        return count <= this.amount;
    }

    public String toString() {
        return name + " - Price: " + price + ", Available: " + amount;
    }
}
 











class Shop {
    Product[] products;

    public Shop() {
        products = new Product[3];
        products[0] = new Product("Cola", 55, 5);
        products[1] = new Product("Sprite", 75, 3);
        products[2] = new Product("Bozo", 90, 7);
    }

    public void displayProducts() {
        System.out.println("Available products:");
        for (int i = 0; i < products.length; i++) {
            System.out.println((i + 1) + ". " + products[i]);
        }
    }

    public Product getProduct(String productName) {
        for (Product product : products) {
            if (product.name.equalsIgnoreCase(productName)) {
                return product;
            }
        }
        return null;
    }
}










public class ProductMain {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        Shop shop = new Shop();

        shop.displayProducts();

        System.out.println("Enter the product name you want to buy:");
        String name = scan.nextLine();

        System.out.println("Enter the quantity:");
        int count = scan.nextInt();
        scan.close();

        Product selectedProduct = shop.getProduct(name);
        if (selectedProduct != null) {
            if (selectedProduct.isAvailable(count)) {
                selectedProduct.displayCost(count);
                selectedProduct.setAmount(count);
                System.out.println("After purchase, remaining: " + selectedProduct.amount + " " + selectedProduct.name + "(s)");
            } else {
                System.out.println("Sorry, not available.");
                System.out.println("Rerun a program to choose smth new :)");
            }
        } else {
            System.out.println("Product not found.");
            System.out.println("Rerun a program to choose that product that we have in our shop :)");
        }
    }
    
}
