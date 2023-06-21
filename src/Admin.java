class Admin extends User {
    private String adminId;

    public Admin(String email, String password, String adminId) {
        super(email, password);
        this.adminId = adminId;
    }

    public String getAdminId() {
        return adminId;
    }

    public void setAdminId(String adminId) {
        this.adminId = adminId;
    }

}

//Admin admin = new Admin("admin@example.com", "adminpassword", "A123");

