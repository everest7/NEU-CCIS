package SOLID;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

enum Relationship {PARENT, CHILD, SIBLING}

class Person{
  public String name;

  public Person(String name) {
    this.name = name;
  }
}

class Triplet{
  Person p1;
  Relationship rl;
  Person p2;

  public Triplet(Person p1, Relationship rl, Person p2) {
    this.p1 = p1;
    this.rl = rl;
    this.p2 = p2;
  }
}

class Relationships implements RelationshipBrowser{ // low level, shouldn't be exposed to users
  private List<Triplet> relations = new ArrayList<>();

  public void addParentAndChild(Person parent, Person child) {
    relations.add(new Triplet(parent, Relationship.PARENT, child));
    relations.add(new Triplet(child, Relationship.CHILD, parent));
  }

  public List<Triplet> getRelations() {
    return relations;
  }

  @Override
  public List<Person> findAllChildrenOf(String name) {
    return null;
  }
}

/**
 * Abstraction we can depend on.
 */
interface RelationshipBrowser {
  List<Person> findAllChildrenOf(String name);
}

/**
 * Research is high level module therefore it violates the principle: High level shouldn't depend on
 * low level module.
 */
class Research {
  // Before modifying
  public Research (Relationships relationships) {
    List<Triplet> relations = relationships.getRelations();

    // Using filter to find the relationship we want
    relations.stream();



  }
  // After modifying:
  public Research (RelationshipBrowser browser) {
    List<Person> children = browser.findAllChildrenOf("Jogn");
    // ... more operation
  }
}

public class DependencyInversion {

  public static void main(String[] args) {

  }
}
