【单选】 以下哪个选项的 getTypeString 函数，没有 bug？

A.
```java

public class Type {

    public enum TypeEnum {
        ZERO,
        ONE
    }

    private TypeEnum type;

    public TypeEnum getType() {
        return type;
    }

    public void setType(TypeEnum type) {
        this.type = type;
    }

    public String getTypeString() {
        switch (type) {
            case ZERO:
                return "ZERO";
            case ONE:
                return "ONE";
            default:
                return "OTHER";
        }
    }
}
```

B.
```java

public class Type {

    private String type;

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getTypeString() {
        switch (type) {
            case "0":
                return "ZERO";
            case "1":
                return "ONE";
            default:
                return "OTHER";
        }
    }
}
```

C.
```java

public class Type {

    private int type;

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public String getTypeString() {
        switch (type) {
            case 0:
                return "ZERO";
            case 1:
                return "ONE";
            default:
                return "OTHER";
        }
    }
}
```

D.
```java

public class Type {

    private Integer type;

    public Integer getType() {
        return type;
    }

    public void setType(Integer type) {
        this.type = type;
    }

    public String getTypeString() {
        switch (type) {
            case 0:
                return "ZERO";
            case 1:
                return "ONE";
            default:
                return "OTHER";
        }
    }
}
```

