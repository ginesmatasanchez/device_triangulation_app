//import org.json.*;

public class Triangle {
    private Point pointA;
    private Point pointB;
    private Point pointC;

    public Triangle(Point pointA, Point pointB, Point pointC) {
            this.pointA = pointA;
            this.pointB = pointB;
            this.pointC = pointC;
        }

    public Point getPointA() {
        return this.pointA;
    }

    public void setPointA(Point pointA) {
        this.pointA = pointA;
    }

    public Point getPointB() {
        return this.pointB;
    }

    public void setPointB(Point pointB) {
        this.pointB = pointB;
    }

    public Point getPointC() {
        return this.pointC;
    }

    public void setPointC(Point pointC) {
        this.pointC = pointC;
    }
}
