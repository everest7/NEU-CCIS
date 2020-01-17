package SOLID;


class Document {

}

interface Machine {
  void print(Document d);
  void fax(Document d);
  void scan(Document d);
}

class MultifunctionPrinter implements Machine {

  @Override
  public void print(Document d) {

  }

  @Override
  public void fax(Document d) {

  }

  @Override
  public void scan(Document d) {

  }
}

/**
 * An old fashioned printer that can only do print.
 * How do we deal with the fax and scan?
 */
class OldFashionPrinter implements Machine {

  @Override
  public void print(Document d) {

  }

  @Override
  public void fax(Document d) {

  }

  @Override
  public void scan(Document d) {

  }
}

public class InterfaceSegregation {

}
