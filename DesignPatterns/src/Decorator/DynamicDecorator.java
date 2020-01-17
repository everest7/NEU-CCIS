package Decorator;

import java.util.function.Supplier;

interface Shape {
  String info();
}

class Circle implements Shape {
  private float radius;

  public Circle() {}

  public Circle(float radius) {
    this.radius = radius;
  }

  void resize(float factor) {
    radius *= factor;
  }

  @Override
  public String info() {
    return "A circle of radius " + radius;
  }
}

class Square implements Shape {
  private float side;

  public Square() {}

  public Square(float side) {
    this.side = side;
  }

  @Override
  public String info() {
    return "Square has side of " + side;
  }
}

/**
 * Static Decorator with generic
 */
class ColoredShape<T extends Shape> implements Shape {
  private Shape shape;
  private String color;

  public ColoredShape(Supplier<? extends T> constructor, String color) {
    shape = constructor.get();
    this.color = color;
  }

  @Override
  public String info() {
    return shape.info() + " has the color " + color;
  }
}

class TransparentShape<T extends Shape> implements Shape {
  private Shape shape;
  private int transparency;

  public TransparentShape(Supplier<? extends T> constructor, int transparency) {
    shape = constructor.get();
    this.transparency = transparency;
  }

  @Override
  public String info() {
    return shape.info() + " hash " + transparency + " % transparency.";
  }
}

// Static Decorator
//==========================//

// Want to add new functionality: color of shape
// Dynamic Decorator
//class ColoredShape implements Shape {
//  private Shape shape;
//  private String color;
//
//  public ColoredShape(Shape shape, String color) {
//    this.shape = shape;
//    this.color = color;
//  }
//
//  @Override
//  public String info() {
//    return shape.info() + " has the color " + color;
//  }
//}

//class TransparentShape implements Shape {
//  private Shape shape;
//  private int transparency;
//
//  public TransparentShape(Shape shape, int transparency) {
//    this.shape = shape;
//    this.transparency = transparency;
//  }
//
//  @Override
//  public String info() {
//    return shape.info() + " hash " + transparency + " % transparency.";
//  }
//}

public class DynamicDecorator {

  public static void main(String[] args) {

    // Dynamic Decorator
//    Circle circle = new Circle(10);
//    System.out.println(circle.info());
//
//    ColoredShape blueSquare = new ColoredShape(new Square(20), "blue");
//    System.out.println(blueSquare.info());
//
//    TransparentShape myCircle = new TransparentShape(
//        new ColoredShape(new Circle(5), "green"), 50);
//    System.out.println(myCircle.info());


    // Static Decorator
    ColoredShape<Square> blueSquare = new ColoredShape<Square>(
        () -> new Square(20), "blue"
    );
    System.out.println(blueSquare.info());

//    TransparentShape<ColoredShape<Circle>> myCircle =
//        new TransparentShape<Circle>(() -> {
//          return new ColoredShape<Circle>(() -> new Circle(5), "green");
//        }, 50);

  }
}
