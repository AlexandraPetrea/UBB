package Topic;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "DeleteServlet")
public class Delete extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {

        String title =  req.getParameter( "title" );

        req.getSession().setAttribute( "title", title );
        String mail = req.getSession().getAttribute("mail").toString();

        BibliographyManager.deleteByTitle(title, mail);

        // Redirect to index
        resp.sendRedirect("components/user.jsp");
    }
}

