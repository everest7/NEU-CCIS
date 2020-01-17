### Facade Pattern
The Facade Pattern provides a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem easier to use.

**Difference between Adapter and Facade**   
The intent of the Adapter Pattern is to alter an interface so that it matches one a client is expecting.  
The intent of the Facade is to provide a simplified interface to a subsystem.

![alt text] [logo]

[logo]: https://2.bp.blogspot.com/-7wnaTwo9mG0/WvfW-4gwetI/AAAAAAAACNI/g7XyQN595HA6qs-OdllfxDc6r_su0JfxACLcBGAs/s1600/facade-design-pattern.PNG, "Facade working principle "  


**Example**  
Facade class serves as the bridge between client and the subsystem. The client doesn't have to operate directly on the subsystem.  
```java
public class HomeTheaterFacade {
  Amplifier amp;
  Tuner tuner;
  DvdPlayer dvd;
  CdPlayer cd;
  Projector pj;
  Screen screen;
  PopcornPopper popper;
  public HomeTheaterFacade() {
    // constructor here
  }

  public void watchMovie(String movie) {
    System.out.println("Get ready to watch the movie..." + movie);
    popper.on();
    popper.pop();
    screen.down();
    pj.on();
    //... a sequence of operation on the subsystem
    dvd.on();
    dvd.play(movie);
  }

  public void endMovie() {
    System.out.println("Shutting movie theater down...");
    popper.off();
    // ...
    dvd.eject();
    dvd.off();
  }
}
```
Instead of letting the client call different appliance one by one, now the client can directly calls on Facade class to watch a movie:
```java
public class HomeTheaterDrive {
  public static void main(String[] args){
    HomeTheaterFacade homeTheater = new HomeTheaterFacade(amp, tuner, dvd, cd, projector);
    homeTheater.watchMovie("Avengers");
    homeTheater.endMovie();
  }
}
```