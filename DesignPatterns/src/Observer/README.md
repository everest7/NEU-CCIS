###Observer Pattern   
The Observer Pattern is a design that lets one or more objects watch the state of one or more other objects.  
* The watcher is referred to as the **Observer**
* The watched object is referred to as the **Subject**
* The pattern’s design centers around two phases:
    * Registration: The Observer registers with the Subject, by calling a registration method on the subject (named something like register, or addObservers).  In that method, the Subject adds the Observer to its list of Observers.
    * Notification: Whenever the Subject’s state changes, it notifies the observers by calling its own notify (or similarly named) method.  The notify method then iterates through the list of observers, calling update (or a similarly named method) on each one.  The Subject may send an argument with this method to indicate the change (the push model), or may send a reference to itself so that the Observer can call back to find out what changed for itself (the pull model).   
    
![alt text](http://blog.lukaszewski.it/wp-content/uploads/2013/02/observer_pattern.png "Logo Title Text 1")
