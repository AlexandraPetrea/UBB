package Topic;

import Model.BibliographyEntry;
import Model.Version;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Date;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

@WebServlet(name = "AddServlet")
public class Add extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String id = req.getParameter("idobject");
        int idN = Integer.parseInt(id);
        int iduser = Integer.parseInt(req.getParameter( "iduser" ));
       // System.out.println(title);
        String content = req.getParameter( "text" );
       System.out.println(content);
        String dataa = req.getParameter("date");
        //Date date1=new SimpleDateFormat("dd/MM/yyyy").parse(dataa);

           // SimpleDateFormat formatter = new SimpleDateFormat("dd-MMM-yyyy");
           // Date data = (Date)"12/12/2019";
            //Date data = new Date("2018-05-05");
            java.sql.Date date = new java.sql.Date(Calendar.getInstance().getTime().getTime());
          //  int author = Integer.parseInt(req.getSession().getAttribute("mail").toString());
           // System.out.println(author);

            if ( content.equals( "" )){

                Version b = new  Version(idN, iduser, content, date);
                VersionManager.add(b);
            }






        resp.sendRedirect("components/user.jsp");
    }
}
