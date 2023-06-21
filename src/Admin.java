public class Admin extends User {
    private String role;

    public Admin(String name, String email, String pasword, String role) {
        super(name, email, pasword);
        this.role = role;
    }


    public String getRole() {
        return this.role;
    }

    public void setRole(String role) {
        this.role = role;
    }


}
