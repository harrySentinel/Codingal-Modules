import java.util.ArrayList;
import java.util.Scanner;

class BankAccount {
    private String owner;
    private String accountNo;
    private double balance;
    private ArrayList<String> transactions;

    BankAccount(String owner, String accountNo, double initialBalance) {
        this.owner = owner;
        this.accountNo = accountNo;
        this.balance = initialBalance;
        this.transactions = new ArrayList<>();
        transactions.add("Account opened with ₹" + initialBalance);
    }

    public void deposit(double amount) {
        if (amount <= 0) { System.out.println("Invalid deposit amount!"); return; }
        balance += amount;
        transactions.add("Deposited ₹" + amount);
        System.out.println("₹" + amount + " deposited. Balance: ₹" + balance);
    }

    public void withdraw(double amount) {
        if (amount <= 0) { System.out.println("Invalid amount!"); return; }
        if (amount > balance) { System.out.println("Insufficient funds!"); return; }
        balance -= amount;
        transactions.add("Withdrew ₹" + amount);
        System.out.println("₹" + amount + " withdrawn. Balance: ₹" + balance);
    }

    public void printStatement() {
        System.out.println("\n--- Account Statement ---");
        System.out.println("Owner      : " + owner);
        System.out.println("Account No : " + accountNo);
        System.out.println("Transactions:");
        for (String t : transactions) System.out.println("  - " + t);
        System.out.println("Current Balance: ₹" + balance);
        System.out.println("-------------------------\n");
    }

    public double getBalance() { return balance; }
    public String getOwner()   { return owner; }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        BankAccount acc = new BankAccount("Aditya Srivastava", "CBS-2024-001", 50000);

        System.out.println("Welcome to Codingal Banking Services (CBS)");
        System.out.println("Account created for: " + acc.getOwner());
        System.out.println();

        boolean running = true;
        while (running) {
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. View Statement");
            System.out.println("4. Exit");
            System.out.print("Choose option: ");

            int choice = sc.nextInt();
            System.out.println();

            switch (choice) {
                case 1:
                    System.out.print("Enter deposit amount: ₹");
                    acc.deposit(sc.nextDouble());
                    break;
                case 2:
                    System.out.print("Enter withdrawal amount: ₹");
                    acc.withdraw(sc.nextDouble());
                    break;
                case 3:
                    acc.printStatement();
                    break;
                case 4:
                    System.out.println("Thank you for banking with Codingal. Goodbye!");
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option!");
            }
            System.out.println();
        }
        sc.close();
    }
}
