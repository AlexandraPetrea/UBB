package Topic;
import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.sql.*;
@WebServlet(name = "DisplayfServlet")
public class DisplayFor extends HttpServlet {
    @Override

    public void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
        PrintWriter out = res.getWriter();
        String primit =  req.getParameter( "id" );
        System.out.println(primit);
        System.out.println(VersionManager.getAllBiblioById(Integer.parseInt(primit)));

        //req.getSession().setAttribute( "id", title );
       // String mail = req.getSession().getAttribute("mail").toString();

        res.setContentType("text/html");
        out.println("<html><link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n" +
                "<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n" +
                "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n" +
                "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n" +
                "\n" +
                "<body>");
        Connection connection;
        try {

            String url = "jdbc:postgresql://localhost:5432/exam";
            Class.forName( "com.mysql.jdbc.Driver" );
            connection = DriverManager.getConnection( url, "postgres", "admin" );
            Statement stmt = connection.createStatement();

            ResultSet rs = stmt.executeQuery("select * from \"versions\" where idobject = '1' ");
            out.println("<table class=\"table table-hover\">");
            out.println("<tr><th>ID</th><th>Author</th><th>Title</th><th>Text</th><th>Votes</th><tr>");
            while (rs.next()) {
                int idversion = rs.getInt("idversion");
                int idobject = rs.getInt("idobject");
                int iduser = rs.getInt("iduser");
                String content = rs.getString("content");
                // int votes = rs.getInt("votes");
                // Date date = new Date("26/05/2019");
                Date date = rs.getDate("time");
                out.println("<tr><td>" + idversion + "</td><td>" + idobject + "</td><td>" + iduser + "</td><td>" + content + "</td><td>" +
                        date + "</td></tr>");
            }
            out.println("</table>");
            out.println("</html></body>");
            connection.close();
        }
        catch (Exception e) {
            out.println("error");

        }
    }
}
