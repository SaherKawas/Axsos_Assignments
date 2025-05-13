public class CafeJava {
    public static void main(String[] args) {
      
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        
        double mochaPrice = 3.5;
        double dripCoffee = 2.5;
        Integer latte = 3;
        double cappuccino = 3.2;
    
        String customer1 = "Shatha";
        String customer2 = "Ahmad";
        String customer3 = "Sali";
        String customer4 = "Adam";
    
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = false;
    
        
        System.out.println(generalGreeting + customer1); 
        System.out.println(customer3 + readyMessage);

        if(isReadyOrder2){
            System.out.println(customer2 + readyMessage);
            System.out.println(displayTotalMessage + cappuccino);
        }
        System.out.println(displayTotalMessage + latte*2);

        if(!isReadyOrder3){
            System.out.println(customer3 + pendingMessage);
        }
        System.out.println(displayTotalMessage + (dripCoffee-latte));
        
    }
}
