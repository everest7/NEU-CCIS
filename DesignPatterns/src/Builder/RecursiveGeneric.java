package Builder;


public class RecursiveGeneric {

  public static void main(String[] args)
  {
    EmployeeBuilder eb = new EmployeeBuilder()
        .withName("Tony")
        .worksAs("Iron Man");
    System.out.println(eb.build());
  }

}

class Person {
  public String name;

  public String position;

  @Override
  public String toString()
  {
    return "Person{" +
        "name='" + name + '\'' +
        ", position='" + position + '\'' +
        '}';
  }
}

class PersonBuilder<SELF extends PersonBuilder<SELF>>
{
  protected Person person = new Person();

  // critical to return SELF here
  public SELF withName(String name)
  {
    person.name = name;
    return self();
  }

  // create a method here so that it can be inherited
  protected SELF self()
  {
    // unchecked cast, but actually safe
    // proof: try sticking a non-PersonBuilder
    //        as SELF parameter; it won't work!
    return (SELF) this;
  }

  public Person build()
  {
    return person;
  }
}

class EmployeeBuilder extends PersonBuilder<EmployeeBuilder>
{
  public EmployeeBuilder worksAs(String position)
  {
    person.position = position;
    return self();
  }

  @Override
  protected EmployeeBuilder self()
  {
    return this;
  }
}
