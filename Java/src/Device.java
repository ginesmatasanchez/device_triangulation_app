public class Device {
    private String deviceType;
    private int batteryLevel;


    public Device(String deviceType, int batteryLevel) {
        this.deviceType = deviceType;
        this.batteryLevel = batteryLevel;
    }

    public String getDeviceType() {
        return this.deviceType;
    }

    public void setDeviceType(String deviceType) {
        this.deviceType = deviceType;
    }

    public int getBatteryLevel() {
        return this.batteryLevel;
    }

    public void setBatteryLevel(int batteryLevel) {
        this.batteryLevel = batteryLevel;
    }





}
