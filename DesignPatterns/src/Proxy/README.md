### Proxy Pattern   
Proxy Pattern is used when we need to create a wrapper to cover the main object's complexity from the client. **It controls 
and manages access to the object they are protecting.**  
An example would be: a check or credit card is a proxy for what is in our bank account. It can be used in place of cash,
and provides a means of accessing that cash when required. 

**Steps for Proxy Pattern**  
1.To support plug-compatibility between the wrapper and target, create a socket. Usually an interface.
```java
interface SocketInterface {
    String readLine();
    void  writeLine(String str);
    void  dispose();
}
```
2.Create a "wrapper" for a remote, or expensive, or sensitive target. Encapsulate the complexity/overhead of the target in the target.
```java
class SocketProxy implements SocketInterface {
    // 1. Create a "wrapper" for a remote,
    // or expensive, or sensitive target
    private Socket socket;
    private BufferedReader in;
    private PrintWriter out;

    public SocketProxy(String host, int port, boolean wait) {
        try {
            if (wait) {
                // 2. Encapsulate the complexity/overhead of the target in the wrapper
                ServerSocket server = new ServerSocket(port);
                socket = server.accept();
            } else {
                socket = new Socket(host, port);
            }
            in  = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch(IOException e) {
            e.printStackTrace();
        }
    }

    public String readLine() {
        String str = null;
        try {
            str = in.readLine();
        } catch( IOException e ) {
            e.printStackTrace();
        }
        return str;
    }

    public void writeLine(String str) {
        // 4. The wrapper delegates to the target
        out.println(str);
    }

    public void dispose() {
        try {
            socket.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```
3.The client deals with the wrapper.  
```java
public class ProxyDemo {
    public static void main( String[] args ) {
        // 3. The client deals with the wrapper
        SocketInterface socket = new SocketProxy( "127.0.0.1", 8080, args[0].equals("first") ? true : false );
        String  str;
        boolean skip = true;
        while (true) {
            if (args[0].equals("second") && skip) {
                skip = !skip;
            } else {           
                str = socket.readLine();
                System.out.println("Receive - " + str);
                if (str.equals(null)) {
                    break;
                }
            }
            System.out.print( "Send ---- " );
            str = new Scanner(System.in).nextLine();
            socket.writeLine( str );
            if (str.equals("quit")) {
                break;
            }
        }
        socket.dispose();
    }
}
```

 