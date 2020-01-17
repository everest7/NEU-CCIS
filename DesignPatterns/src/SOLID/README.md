### SOLID Principle

S - Single responsibility principle  
One class, one responsibility. We say that a module or class has high cohesion when it is designed around a set of related functions.    

O - Open closed principle  
Open for extension, it's okay to inherit class or implement interfaces,
but it's closed for modification
    
L - Liskov substitution principle  
Derived classes must be substitutable for their base classes.   In our example,
if Square is a subclass of Rectangle, all methods that work fine for Rectangle should 
also work fine for Square, but it didn't.  
Solution: Factory Pattern 

    
I - Interface segregation principle  
Client should not be forced to implement the methods it does not use. How to split interfaces into
smaller interfaces.   In our example, what if we have an old fashioned printer that can only do print. 
How do we deal with the fax and scan? Split the interface.   
Solution: 1. let interface extend to other interfaces. 2. Decorator Pattern
    
D - Dependency inversion principle  
Details should depend on abstraction , not the other way around.   
In our example, Research is high level module therefore it violates the principle: High level shouldn't depend on 
low level module.