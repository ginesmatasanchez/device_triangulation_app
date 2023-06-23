import java.util.ArrayList;
import java.util.List;

public class Building {
    private String name;
    private double latitude, longitude;
    private List<Floor> floors;


        public Building(String name, double latitude, double longitude) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
            this.floors = new ArrayList<>();
        }


    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getLatitude() {
        return this.latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public double getLongitude() {
        return this.longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public List<Floor> getFloors() {
        return this.floors;
    }

    public void setFloors(List<Floor> floors) {
        this.floors = floors;
    }

        


}
