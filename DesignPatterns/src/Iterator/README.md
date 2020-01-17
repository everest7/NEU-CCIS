### Iterator Pattern  
The Iterator Pattern allows the access for elements of an aggregate object sequentially without exposing its underlying representation.  

**Example**  
Say we have lunchMenu represented as ArrayList and dinnerMenu represented as Array. If a waitress wants to print our all the items in 
lunchMenu and dinnerMenu, she needs to use at least two for loop to iterate two menus. 

**Better Solution?**  
__Encapsulate the iteration. Programming to an interface, not an implementation.__ In this way, the waitress has no idea how the menus hold their collection of the menu items and she just needs to use an interface(iterator). The iterator allows the waitress to be decoupled from the actual implementation of the concrete classes.
It shifts the responsibility of traversing elements from the aggregate object to the iterator object.
```java
public class Waitress {
  Menu lunchMenu;
  Menu dinnerMenu;

  public Waitress(Menu lunchMenu, Menu dinnerMenu) {
  this.lunchMenu = lunchMenu;
  this.dinnerMenu = dinnerMenu;  
  }

  public void printMenu() {
    Iterator lunchIterator = lunchMenu.createIterator();
    Iterator dinnerIterator = dinnerMenu.createIterator();
    System.out.println("Menu\n");
    printMenu(lunchIterator);
    printMenu(dinnerIterator);
  }

  public void printMenu(Iterator iterator) {
    while (iterator.hasNext()) {
      MenuItem item = (MenuItem) iterator.next();
      System.out.print(iter.getName() + " ");
      System.out.println(iter.getDecsription() + " ");
    }
  }
}
```

```java
public interface Menu {
  public Iterator createIterator(); // lets clients get an iterator for the items in the menu
}
```