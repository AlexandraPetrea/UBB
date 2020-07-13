package Topic;


import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "EditServlet")
public class Edit extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String id = req.getParameter( "id" );
        String mail = req.getSession().getAttribute("username").toString();
        if (!id.equals("") && !mail.equals("")) {
            VersionManager.getAllBiblioById(1);
            resp.sendRedirect("components/edit.jsp");
        }

    }

}
