【单选】filter 方法意图过滤传入的订单列表中不属于当前系统时间所在日期的订单，以下哪一行代码存在错误？

A.第 7 行     
B.第 8 行    
C.第 10 行    
D.第 13 行

```java

1.  public static void filter(ArrayList<Order> orders) {
2.     
3.     if (orders == null) {
4.         return;
5.     }
6.     
7.     SimpleDateFormat formatter = new SimpleDateFormat("YYYY-MM-dd")
8.     String currentDay = formatter.format(new Date());
10.    Iterator<Order> iterator = orders.iterator();
11.    while (iterator.hasNext()) {
12.        Order order = iterator.next();
13.        if (!currentDay.equals(order.getTransactionDay())) {
14.            iterator.remove();
15.        }
16.    } 
17.}
```
