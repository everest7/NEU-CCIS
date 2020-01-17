### State Pattern   
The State Pattern allows an object to alter its behavior when its internal state changes. The pattern 
encapsulates state into separate classes and delegates to the object representing the current state.

**Difference between State and Strategy Pattern**  
With the State Pattern, a set of behaviors are encapsulated in state Object; at any time the context is 
delegating to one of those states.
With Strategy, while the pattern provides the flexibility to change the strategy object at runtime, often there is a strategy object
that is most appropriate for a context object. 

![alt text](https://pic002.cnblogs.com/images/2012/358984/2012050411054690.png "Logo Title Text 1")

**Implementation**   

The methods in the interface map directly to actions that could happen to the Gumball Machine.
```java
interface State {
  void insertQuarter();
  void ejectQuarter();
  void turnCrank();
  void dispense();
}
```
Implement state class:
```java
public class NoQuarterState implements State {
  GumballMachine gumballMachine;

  public NoQuarterState(GumballMachine gumballMachine) {
    this.gumballMachine = gumballMachine; // pass the reference
  }

  public void insertQuarter() {
    System.out.println("You inserted a quarter"); // change state
    gumballMachine.setState(gumballMachine.getHasQuarterState()); 
  }

  public void ejectQuarter() {
    System.out.println("You haven't inserted a quarter.");
  }
  
  // other behaviors
}
```

Implement Context:
```java
public class GumballMachine {
 
	State soldOutState;
	State noQuarterState;
	State hasQuarterState;
	State soldState;
 
	State state;
	int count = 0;
 
	public GumballMachine(int numberGumballs) {
		soldOutState = new SoldOutState(this);
		noQuarterState = new NoQuarterState(this);
		hasQuarterState = new HasQuarterState(this);
		soldState = new SoldState(this);

		this.count = numberGumballs;
 		if (numberGumballs > 0) {
			state = noQuarterState;
		} else {
			state = soldOutState;
		}
	}
 
	public void insertQuarter() {
		state.insertQuarter();
	}
 
	public void ejectQuarter() {
		state.ejectQuarter();
	}
 
	public void turnCrank() {
		state.turnCrank();
		state.dispense();
	}
  
  // other behaviors

}
```