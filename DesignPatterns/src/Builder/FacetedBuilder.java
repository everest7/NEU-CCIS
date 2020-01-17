package Builder;

public class FacetedBuilder {

}

class Person2 {
  // address
  public String streetAdd, postcode, city;
  // employment
  public String company, position;
  public int annualIncome;

  @Override
  public String toString() {
    return super.toString();
  }
}

class Person2Builder {
  protected Person2 person = new Person2();
  public Person2 build() {
    return person;
  }
}

class PersonAddressBuilder extends Person2Builder {

  public PersonAddressBuilder(Person2 person2) {
    this.person = person2;
  }
}
