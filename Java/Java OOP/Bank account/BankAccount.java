public class BankAccount {
    // MEMBER VARIABLES
    private double checkingBalance;
    private double savingsBalance;

    private static int accounts;
    private static double totalMoney; // refers to the sum of all bank account checking and savings balances

    // CONSTRUCTOR
    public BankAccount( double checkingBalance, double savingsBalance){
        this.checkingBalance=checkingBalance;
        this.savingsBalance=savingsBalance;
        accounts++;
        totalMoney+= checkingBalance + savingsBalance;
    }
    // GETTERS
    // for checking, savings, accounts, and totalMoney
    public double getCheckingBalance(){
        return checkingBalance;
    }

    public double getSavingsBalance(){
        return savingsBalance;
    }

    public static int getAccounts(){
        return accounts;
    }

    public static double getTotalMoney(){
        return totalMoney;
    }

    // METHODS
    // deposit
    // - users should be able to deposit money into their checking or savings account
    public String deposit(double amount) {
        checkingBalance += amount;
        totalMoney += amount;
        return "Deposited $" + amount + ". New checking balance: $" + checkingBalance; 
    }

    // withdraw 
    // - users should be able to withdraw money from their checking or savings account
    // - do not allow them to withdraw money if there are insufficient funds
    // - all deposits and withdrawals should affect totalMoney
    public String withdraw(double amount) {
        if (amount <= 0) {
            return "Withdrawal amount must be positive!";
        }
        if (amount > checkingBalance) {
            return "Can't withdraw! Insufficient funds!";
        }
        checkingBalance -= amount;
        totalMoney -= amount;
        return "Withdrew $" + amount + ". New balance: $" + checkingBalance;
    }
    
    
    // getBalance
    // - display total balance for checking and savings of a particular bank account

    public double getBalance(){
        return checkingBalance + savingsBalance;
    }

}
