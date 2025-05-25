import java.util.ArrayList;

public class Order {
    private String name;
    private boolean ready;
    private ArrayList<Item> items;

    public Order() {
        this.name="Guest";
        this.items= new ArrayList<item>;

    }
    
    public Order(String name) {
        this.name = name;
        
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

    public String getStatusMessage() {
        if (this.ready) {
            return "Your order is ready.";
        } else {
            return "Thank you for waiting. Your order will be ready soon.";
        }
    }

    public double getOrderTotal() {
        double total = 0.0;
        for (Item fo : this.items) {
            total += fo.getPrice(); 
        }
        return total;
    }

    public void display() {  
        System.out.println("Customer Name: " + this.name);
        for (Item item : this.items) {
            System.out.printf("%s - $%.2f%n", item.getName(), item.getPrice());
        }
        System.out.printf("Total: $%.2f%n", this.getOrderTotal());
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }

    public ArrayList<Item> getItems() {
        return new ArrayList<>(items);
    }

    public void setItems(ArrayList<Item> items) {
        this.items = new ArrayList<Item>(items);  // Added missing semicolon
    }
}