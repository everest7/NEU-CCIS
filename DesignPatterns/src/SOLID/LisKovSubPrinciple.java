package SOLID;

class Rectangle {
  protected int width, height;

  public Rectangle() {
  }

  public Rectangle(int width, int height) {
    this.width = width;
    this.height = height;
  }

  public int getWidth() {
    return width;
  }

  public void setWidth(int width) {
    this.width = width;
  }

  public int getHeight() {
    return height;
  }

  public void setHeight(int height) {
    this.height = height;
  }

  @Override
  public String toString() {
    return "Rectangle{" +
        "width=" + width +
        ", height=" + height + "}";
  }

  public int getArea() {
    return width * height;
  }
}

class Square extends Rectangle {
  public Square() {}
  public Square(int size) {
    width = height = size;
  }

  @Override
  public void setWidth(int width) {
    super.setWidth(width);
    super.setHeight(width);
  }

  @Override
  public void setHeight(int height) {
    super.setHeight(height);
    super.setWidth(height);
  }
}

public class LisKovSubPrinciple {
    static void useIt(Rectangle r) {
      int width = r.getWidth();
      r.setHeight(10);
      System.out.println("Expected area of " + (width * 10) + ", got " + r.getArea());
    }

  public static void main(String[] args) {
    Rectangle r = new Rectangle(5, 10);
    useIt(r);

    Square sq = new Square(5);
    useIt(sq); // Expected area of 50, got 100
  }
}
