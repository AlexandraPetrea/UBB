package Topic;


import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "VoteServlet")
public class Vote extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String title = req.getParameter( "title" );
        String mail = req.getSession().getAttribute("mail").toString();
        if (!title.equals("") && !mail.equals("")){
            BibliographyManager.update(title, mail);
            resp.sendRedirect("components/user.jsp");
        }

    }
}
