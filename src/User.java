import java.util.*;

// Clase User que representa a los usuarios del sistema
class User {
    private String email;
    private String password;
    private Set<String> roles;

    public User(String email, String password) {
        this.email = email;
        this.password = password;
        this.roles = new HashSet<>();
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return this.password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Set<String> getRoles() {
        return this.roles;
    }

    public void setRoles(Set<String> roles) {
        this.roles = roles;
    }

    public void addRole(String role) {
        this.roles.add(role);
    }
    
    public void removeRole(String role) {
        this.roles.remove(role);
    }

}

// Clase principal que controla el acceso al mapa
class MapAccessController {
    private static List<User> users = new ArrayList<>();

    public static void main(String[] args) {
       
        // Crear usuarios
        User user1 = new User("user1@example.com", "password1");
        User user2 = new User("user2@example.com", "password2");
        User admin = new User("admin@example.com", "adminpassword");

        // Asignar roles a los usuarios
        user1.addRole("user");
        user2.addRole("user");
        admin.addRole("admin");

        // Agregar usuarios a la lista
        users.add(user1);
        users.add(user2);
        users.add(admin);

        // Simulación de inicio de sesión
        User loggedInUser = login("user1@example.com", "password1");
        
        // Verificar el acceso al mapa según el rol del usuario
        if (loggedInUser != null) {
            if (loggedInUser.getRoles().contains("admin")) {
                System.out.println("Acceso completo al mapa");
                // Aquí iría el código para mostrar el mapa completo
            } else if (loggedInUser.getRoles().contains("user")) {
                System.out.println("Acceso limitado al mapa");
                // Aquí iría el código para mostrar un mapa con acceso limitado
            } else {
                System.out.println("Acceso denegado al mapa");
                // Aquí iría el código para mostrar un mensaje de acceso denegado
            }
        } else {
            System.out.println("Inicio de sesión fallido");
            // Aquí iría el código para mostrar un mensaje de inicio de sesión fallido
        }
    }

    // Método para realizar el inicio de sesión
    public static User login(String email, String password) {
        for (User user : users) {
            if (user.getEmail().equals(email) && user.getPassword().equals(password)) {
                return user;
            }
        }
        return null; // Si no se encuentra el usuario o las credenciales son incorrectas
    }
}
