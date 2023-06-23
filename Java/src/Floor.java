import java.util.ArrayList;
import java.util.List;

public class Floor {
        private int floorNumber;
    private List<Zone> zones;

    public Floor(int floorNumber) {
        this.floorNumber = floorNumber;
        this.zones = new ArrayList<>();
            
}

    public int getFloorNumber() {
        return this.floorNumber;
    }

    public void setFloorNumber(int floorNumber) {
        this.floorNumber = floorNumber;
    }

    public List<Zone> getZones() {
        return this.zones;
    }

    public void setZones(List<Zone> zones) {
        this.zones = zones;
    }

    public void addZone(Zone zone) {
        this.zones.add(zone);
    }
}
