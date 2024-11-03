
/*
Person.java
Defines a simple class with a method.
*/

class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    public void sayHello() {
        System.out.println("Hello, my name is " + name);
    }

    public static void main(String[] args) {
        Person person = new Person("Alice");
        person.sayHello();
    }
}
