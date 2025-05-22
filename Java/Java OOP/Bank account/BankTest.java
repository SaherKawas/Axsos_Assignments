public class BankTest {
    public static void main(String[] args){
        // Create 3 bank accounts
        BankAccount acc1= new BankAccount(3000.0, 2500.0);
        BankAccount acc2= new BankAccount(4000.0, 3200.0);
        BankAccount acc3= new BankAccount(5000.0, 4500.0);
        // Deposit Test
        // - deposit some money into each bank account's checking or savings account and display the balance each time
        // - each deposit should increase the amount of totalMoney
        System.out.println("--- Deposit Tests ---");
        System.out.println(acc1.deposit(10000.0));
        System.out.println(acc2.deposit(14000.0));
        System.out.println(acc3.deposit(1000.0));

        System.out.println("\n--- Account Balances ---");
        System.out.println("Account 1: " + acc1.getBalance());
        System.out.println("Account 2: " + acc2.getBalance());
        System.out.println("Account 3: " + acc3.getBalance());

        // Withdrawal Test
        // - withdraw some money from each bank account's checking or savings account and display the remaining balance
        // - each withdrawal should decrease the amount of totalMoney
        System.out.println("\n--- Withdrawal Tests ---");
        System.out.println(acc1.withdraw(500.0));
        System.out.println(acc2.withdraw(10000.0));
        System.out.println(acc3.withdraw(-100.0));
        // Static Test (print the number of bank accounts and the totalMoney)
        System.out.println("\n--- Bank Statistics ---");
        System.out.println("Total accounts: " + BankAccount.getAccounts());
        System.out.println("Total money in bank: $" + BankAccount.getTotalMoney());
    }
}