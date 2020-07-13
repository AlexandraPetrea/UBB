package Topic;

import DB.DBManager;
import Model.BibliographyEntry;
import Model.Version;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class VersionManager {

    public static ArrayList<Version> getAllBiblioById(int id){
        List<Version> versions = new ArrayList<>(  );
        try {
            String sql = "select * from \"versions\" where idobject = '" + id + "';";
            PreparedStatement statement = DBManager.getConnection().prepareStatement( sql );
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()){
                versions.add( new Version(resultSet.getInt( 1 ),
                        resultSet.getInt( 2 ),
                        resultSet.getInt( 3 ),
                        resultSet.getString( 4 ),
                        resultSet.getDate(5)

                ));
            }

            versions = versions.stream().filter( b -> b.getIdobject() == id ).collect(Collectors.toList());
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return (ArrayList<Version>) versions;
    }


    public static Version getByTitle(String title){
        try{
            String sql = "select * from \"Versions\" where title = '" + title + "';";
            PreparedStatement stmt = DBManager.getConnection().prepareStatement( sql );
            ResultSet resultSet = stmt.executeQuery();

            while(resultSet.next()){
                Integer id = resultSet.getInt( 1 );
                Integer author = resultSet.getInt( 2 );
                Integer title1 = resultSet.getInt( 3 );
                String text = resultSet.getString( 4 );
                Date data = resultSet.getDate( 5 );
                Version b = new Version(id, author, title1, text, data);
                //b.setId(id);
                return b;
            }
            return null;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void add(Version b) {
       // int aux = 2;
        try {
           // aux = aux+1;
            String sql = "insert into \"versions\"(idobject, iduser, content, time) values ('" + b.getIdobject() + "', '" + b.getIduser() + "', '" + b.getContent()+ "', '" + b.getDate().toString() + "');";
            PreparedStatement statement = DBManager.getConnection().prepareStatement(sql);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

}

