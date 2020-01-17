### Template Method Pattern  
The template method pattern defines the steps of an algorithm and allows subclasses to provide the implementation for one or more steps.  

** A template for this pattern**  
```java
abstract class AbstractClass {
  final void templateMethod() {
    primitiveOperation1();
    primitiveOperation2();
    concreteOperation();
    hook();
  }
  
  // these are abstract and implemented by concrete subclasses
  abstract void primitiveOperation1(); 
  abstract void primitiveOperation1(); 

  // This one is shared by all subclasses and  declared final so that subclass can't override it.
  // It may be used in the template method directly or used by subclass.
  final void concreteOperation() {
    // implementation here
  }
  
  // A hook gives subclasses the ability to "hook into" the algorithm at various points, if they wish.
  void hook() {}
}
```

**About Hook**  
Hook provides a way for a subclass to implement an optional part of an algorithm, or if it isn't important to the subclass' implementation, it can skip it. 