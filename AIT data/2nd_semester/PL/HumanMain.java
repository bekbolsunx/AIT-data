
class Human {
  String name;
  int age;

  public Human(String name, int age) {
      this.name = name;
      this.age = age;
  }

  public void show() {
      System.out.println(name + " " + age);
  }

  public String getName() {
      return name;
  }

  public int getAge() {
      return age;
  }
}

class Student extends Human {
  String universityName;
  int sid;

  public Student(String universityName, int sid, String name, int age) {
      super(name, age);
      this.universityName = universityName;
      this.sid = sid;
  }

  public String getUniversityName() {
      return universityName;
  }

  public int getSid() {
      return sid;
  }

  @Override
  public void show() {
      super.show();
      System.out.println(universityName + " " + sid);
  }
}

class Employee extends Human {
  int salary;
  String workN;

  public Employee(String workN, int salary, String name, int age) {
      super(name, age);
      this.workN = workN;
      this.salary = salary;
  }

  public void changeSalary(int newSalary) {
      this.salary = newSalary;
  }

  public int getSalary() {
      return salary;
  }

  public String getWorkN() {
      return workN;
  }

  @Override
  public void show() {
      super.show();
      System.out.println(workN);
      System.out.println(salary);
  }
}

public class HumanMain {
  public static void main(String[] args) {
    System.out.println("### Student INFO ###");
      Student student1 = new Student("Ait", 1, "Bekbolsun", 17);
      student1.show();
System.out.println("--------------------------------------------------------");
    System.out.println("### Employee INFO ###");
      Employee employee1 = new Employee("Proger", 200, "Kira", 32);
      employee1.show();
  }
}


















