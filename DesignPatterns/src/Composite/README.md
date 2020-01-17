### Composite Pattern  
The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. It allows clients
treat individual objects and compositions of objects uniformly.  

We can break the pattern down into:  
**Component:** is the base interface for all the objects in the composition. It should be either an interface or an abstract class with the common methods to manage the child composites.  
1. **Leaf:** implements the default behavior of the base component. It does not contain a reference to the other objects.  
2. **Composite:** has leaf elements. It implements the base component methods and defines the child-related operations.    

**Client:** uses the component interface to manipulate the objects in the composition.

**Structure**
![alt text] [logo]

[logo]: https://howtodoinjava.com/wp-content/uploads/2015/10/composite-design-pattern.png, "Facade working principle "  

Using a composite structure, we can apply the same operations over both composites and leaf objects. 

**Implementing the Component**  
```java
public abstract class MenuComponent {
  public void add(MenuComponent menuComponent) {
    // Some operation make sense for the Composite, some make sense for the leaf
    // the default implementation is UnsupportedOperationException.
    throw new UnsupportedOperationException(); 
  }

  public void remove(MenuComponent menuComponent) {}
  public MenuComponent getChild(int i) {}
  public void print() {}
  // ...
}
```  
**Implementing the MenuItem(Leaf)**  
```java
public class MenuItem extends MenuComponent {
  String name;
  String description;
  public MenuItem(String name, String description) {
    this.name = name;
    this.description = description;
  }
  public void print() {}
  // some operation make sense for MenuItem
}
```  
**Implementing the Menu(Composite)**  
Note that some methods both exist in Menu and MenuItem should be implemented in a recursive way.
```java
public class Menu extends MenuComponent {
  ArrayList menuComponent = new ArrayList();
  String name;
  String description;
  // some operation make sense for Menu

  // We should implement the print() method in a recursive way
  // During this iteration, if we encounter another Menu Object, 
  // its print() method will start another iteration, and so on. 
  public void print() {
    System.out.println(getName());
    System.out.println(getDescription());
    Iterator itr = menuComponent.iterator();
    while (itr.hasNext()) {
      MenuComponent menuComponent = (MenuComponent) itr.next();
      menuComponent.print();
    }
  }
}
```

