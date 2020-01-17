###Singleton Pattern  
The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.  

**Creation**  
```java
public class Singleton {
  private static Singleton uniqueInstance;
  // other useful instance variables here
  private Singleton() {} // make constructor private
  public static Singleton getInstance() {
    if (uniqueInstance == null) {
      uniqueInstance = new Singleton();
    }
    return uniqueInstance;
  }
  // other useful methods here
}
```

**Dealing with multithreading**  
To avoid two threads access the uniqueInstance at the same time, we can
1. Add **synchronized** keyword to getInstance() method, but doing this will create unneeded overhead since 
every time we call getInstance() 'synchronized' is also called, this leads to performance issue.
2. Create Singleton eagerly, like this
    ```java
    public class Singleton {
      private static Singleton uniqueInstance = new Singleton();
      private Singleton() {}
      public static Singleton getInstance() {
        return uniqueInstance;  
      }
    }
    ```
3. Use "double-checked locking" to reduce the use of synchronization in getInstance(). Note that we only synchronize
the first time through.  
    ```java
    public class Singleton {
      private volatile static Singleton uniqueInstance;
      private Singleton() {}
      public static Singleton getInstance() {
        if (uniqueInstance == null) {
          synchronized (Singleton.class) {
            if (uniqueInstance == null) {
              uniqueInstance = new Singleton();
            }
          }
        }
        return uniqueInstance;
      }
    }
    ```
