package Factory;

enum CoordinateSystem {CARTESIAN, POLAR}

class Point {
  private double x, y;

  private Point(double x, double y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Constructor has to decide which concrete constructor to choose
   */
  private Point(double a, double b, CoordinateSystem cs) {
    switch (cs) {
      case CARTESIAN:
        this.x = a;
        this.y = b;
        break;
      case POLAR:
        this.x = a * Math.cos(b);
        this.y = a * Math.sin(b);
        break;
    }
  }

  static class PointFactory {
    /**
     * After making our constructor private, it is our client's responsibility to decide which kind
     * of Point they want
     * @param x
     * @param y
     * @return
     */
    public static Point newCartesianPoint(double x, double y) {
      return new Point(x, y);
    }

    public static Point newPolarPoint(double rho, double theta) {
      return new Point(rho * Math.cos(theta), rho * Math.sin(theta));
    }
  }


}



public class FactoryMethod {

  public static void main(String[] args) {
//    Point point1 = Point.newCartesianPoint(2, 3);
//    Point point2 = Point.newPolarPoint(4, 30);

    // After we put all the methods in factory in a nested class
    Point point1 = Point.PointFactory.newCartesianPoint(2, 3);
    Point point2 = Point.PointFactory.newPolarPoint(2, 30);

  }
}
