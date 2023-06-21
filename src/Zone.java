//import org.json.*;

public class Zone {
    private String name;
    private Triangle trianglePosition;

    public Zone(String name, Triangle trianglePosition) {
            this.name = name;
            this.trianglePosition = trianglePosition;
        }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Triangle getTrianglePosition() {
        return this.trianglePosition;
    }

    public void setTrianglePosition(Triangle trianglePosition) {
        this.trianglePosition = trianglePosition;
    }

}
