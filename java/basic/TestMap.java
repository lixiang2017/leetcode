import java.util.HashMap;
import java.util.Map;
import java.util.Hashtable;

public class TestMap {
    public static void main(String[] args) {
        // Map<String, Integer> map = new HashMap<> ();         // ok
        // HashMap<String, Integer> map = new HashMap<> ();     // ok
        // Hashtable<String, Integer> map = new HashMap<> ();   // TestMap.java:9: error: incompatible types: cannot infer type arguments for HashMap<>
        Hashtable<String, Integer> map = new Hashtable<> ();    // ok 
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);
        System.out.println(map);
    }
}