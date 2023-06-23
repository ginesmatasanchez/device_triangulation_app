//import org.json.*;

public class Point {
    private double x;
    private double y;
    private double z;
    private Device device;


    public Point(double x, double y, double z, Device device) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.device = device;
    }

    public double getX() {
        return this.x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return this.y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getZ() {
        return this.z;
    }

    public void setZ(double z) {
        this.z = z;
    }

    public Device getDevice() {
        return this.device;
    }

    public void setDevice(Device device) {
        this.device = device;
    }

}