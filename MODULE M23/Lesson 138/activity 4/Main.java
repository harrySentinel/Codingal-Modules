class BankAccount {
    private double balance;
    private String owner;
    public String accountType;
    protected String branch;

    BankAccount(String owner, double balance, String branch) {
        this.owner = owner;
        this.balance = balance;
        this.branch = branch;
        this.accountType = "Savings";
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited ₹" + amount + ". New Balance: ₹" + balance);
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrew ₹" + amount + ". New Balance: ₹" + balance);
        } else {
            System.out.println("Insufficient funds!");
        }
    }

    public double getBalance() {
        return balance;
    }

    public void display() {
        System.out.println("Owner   : " + owner);
        System.out.println("Type    : " + accountType);
        System.out.println("Branch  : " + branch);
        System.out.println("Balance : ₹" + balance);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Aditya Srivastava", 50000, "Mumbai");
        acc.display();

        acc.deposit(10000);
        acc.withdraw(5000);
        acc.withdraw(100000);

        System.out.println();
        System.out.println("Final Balance: ₹" + acc.getBalance());
    }
}
