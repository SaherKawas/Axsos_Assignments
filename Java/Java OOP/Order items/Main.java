public class Main{
    public static void main(String[] args){
        // Menu items
                Item item1 = new Item("mocha", 3.5);
                Item item2 = new Item("latte", 2.5);
                Item item3 = new Item("drip coffee", 3);
                Item item4 = new Item("cappuccino", 4);
                // Order variables -- order1, order2 etc.
                Order order1 = new Order("Rami");
                Order order2 = new Order("Jimmy");
                Order order3 = new Order("Noah");
                Order order4 = new Order("Sam");
                // Application Simulations

                // Use this example code to test various orders' updates
                System.out.printf("Name: %s\n", order1.name);
                System.out.printf("Total: %s\n", order1.total);
                System.out.printf("Ready: %s\n", order1.ready);

                order2.addItem(item1);
                order3.addItem(item4);
                order4.addItem(item2);
                order1.setReady();
                order4.addItem(item2);
                order2.setReady();
    }
}