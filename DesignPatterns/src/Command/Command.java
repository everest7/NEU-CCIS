package Command;

import Command.BankAccountCommand.Action;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

interface Commands {
  void call();
  void undo();
}

class BankAccountCommand implements Commands{
  private BankAccount account;
  private boolean succeeded; // flag indicating whether the action was successful

  @Override
  public void call() {
    switch (action) {
      case DEPOSIT:
        succeeded = true;
        account.deposit(amount);
        break;
      case WITHDRAW:
        succeeded = account.withdraw(amount);
        break;
    }
  }

  @Override
  public void undo() {
    if (!succeeded) return;
    switch (action) {
      case DEPOSIT:
        account.withdraw(amount);
        break;
      case WITHDRAW:
        account.deposit(amount);
        break;
    }
  }

  public enum Action {DEPOSIT, WITHDRAW}
  private Action action;
  private int amount;

  public BankAccountCommand(BankAccount account, Action action, int amount) {
    this.account = account;
    this.action = action;
    this.amount = amount;
  }
}

class BankAccount {
  private int balance;
  private int overdraftLimit = -500;

  public void deposit(int amount) {
    balance += amount;
    System.out.println("Deposited " + amount + ", balance is now " + balance);
  }

  public boolean withdraw(int amount) {
    if (balance - amount >= overdraftLimit) {
      balance -= amount;
      System.out.println("Withdrew " + amount + ", balance is now " + balance);
      return true;
    }
    return false;
  }

  @Override
  public String toString() {
    return "BankAccount{balance=" + balance + "}";
  }
}

public class Command {

  public static void main(String[] args) {
    BankAccount ba = new BankAccount();
    System.out.println(ba);

    List<BankAccountCommand> commands  = new ArrayList<BankAccountCommand>();
    commands.add(new BankAccountCommand(ba, Action.DEPOSIT, 100));
    commands.add(new BankAccountCommand(ba, Action.WITHDRAW, 1000));

    for (BankAccountCommand c : commands) {
      c.call();
      System.out.println(ba);
    }
    Collections.reverse(commands);
    for (BankAccountCommand c : commands) {
      c.undo();
      System.out.println(ba);
    }
  }
}
