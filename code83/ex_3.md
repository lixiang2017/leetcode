【单选】以下哪段代码，调用 getHelper 的过程，不是线程安全的

A.
```java

public class LazyInitDemo {
    
    private static Helper HELPER = null;
    
    public static synchronized Helper getHelper() {
        if (HELPER == null) {
            HELPER = new Helper();
        }
        return HELPER;
    }
}
```

B.
```java

public class LazyInitDemo {
    
    private Helper helper = null;

    public Helper getHelper() {
        if (helper == null) {
            synchronized (this) {
                if (helper == null) {
                    helper = new Helper();
                }
            }
        }
        return helper;
    }
}
```

C.
```java

public class LazyInitDemo {  
    
    private static class HelperHolder {  
        private static final Helper HELPER = new Helper();  
    }  
    
    public static final Helper getHelper() {  
        return HelperHolder.HELPER; 
    }  
}
```

D.
```java

public class PreInitDemo{

    private static final Helper HELPER = new Helper();
    
    public static Helper getHelper(){
        return HELPER;
    }
}
```
