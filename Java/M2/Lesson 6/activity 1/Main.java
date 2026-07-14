interface MyInterface {
    /* compiler will treat these as:
     * public abstract void method1();
     * public abstract void method2();
     */
    public void method1();
    public void method2();
}

class Main implements MyInterface {
    /* This class must have to implement both the abstract methods
     * else you will get compilation error
     * try removing one method and see the error
     */
    public void method1() {
        System.out.println("Implementation of method1");
    }

    public void method2() {
        System.out.println("Implementation of method2");
    }

    public static void main(String args[]) {
        MyInterface obj = new Main();
        obj.method1();
        obj.method2();
    }
}
