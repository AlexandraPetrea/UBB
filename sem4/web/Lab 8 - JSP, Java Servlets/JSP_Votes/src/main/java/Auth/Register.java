package Auth;
import DB.DBManager;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.annotation.WebServlet;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

@WebServlet(name = "RegisterServlet")
public class Register extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String mail = req.getParameter("mail");
        String name = req.getParameter("name");
        String password = req.getParameter("password");
        String repeatPassword = req.getParameter("repeatPassword");
        String role = "1";
        if (mail != "" && name != "" && password != "" && repeatPassword != ""
        && password.equals(repeatPassword) //&& AuthManager.isMailUnique(mail)
         ){
        // {
            // Password are not equal

            // Encrypt the password
            String encryptedPassword = AuthManager.encrypt(password);

            // Save the password to database
            AuthManager.addUserToDataBase(mail,encryptedPassword);

            // Login the user
            Login.loginUser(req.getSession(), mail);

            // Redirect the user to /
            resp.sendRedirect("components/auth/login.jsp");
        }
    }


}
