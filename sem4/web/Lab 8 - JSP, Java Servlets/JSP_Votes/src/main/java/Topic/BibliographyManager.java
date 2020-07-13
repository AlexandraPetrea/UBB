package Topic;

import Auth.AuthManager;
import DB.DBManager;
import Model.BibliographyEntry;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class BibliographyManager {
    public static ArrayList<BibliographyEntry> getAllBiblioBySubstring(String text){
        List<BibliographyEntry> bibliographyEntries = new ArrayList<>(  );
        try {
            String sql = "select * from BibliographyEntry";
            PreparedStatement statement = DBManager.getConnection().prepareStatement( sql );
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()){
                bibliographyEntries.add( new BibliographyEntry(resultSet.getInt( 1 ),
                        resultSet.getString( 2 ),
                        resultSet.getString( 3 ),
                        resultSet.getString( 4 ),
                        resultSet.getInt(5)

                ));
            }

            bibliographyEntries = bibliographyEntries.stream().filter( b -> b.getTitle().contains( text ) || b.getAuthor().contains( text ) ).collect(Collectors.toList());
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return (ArrayList<BibliographyEntry>) bibliographyEntries;
    }
    public static ArrayList<BibliographyEntry> getAll(){
        List<BibliographyEntry> bibliographyEntries = new ArrayList<>(  );
        try {
            String sql = "select * from \"BibliographyEntry\"";
            PreparedStatement statement = DBManager.getConnection().prepareStatement( sql );
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()){
                bibliographyEntries.add( new BibliographyEntry(resultSet.getInt( 1 ),
                        resultSet.getString( 2 ),
                        resultSet.getString( 3 ),
                        resultSet.getString( 4 ),
                        resultSet.getInt(5)

                ));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return (ArrayList<BibliographyEntry>) bibliographyEntries;
    }

    public static void add(BibliographyEntry b) {
        int aux = 2;
            try {
                aux = aux+1;
                String sql = "insert into \"BibliographyEntry\"(author, title, text, votes) values ('" + b.getAuthor() + "', '" + b.getTitle() + "', '" + b.getText()+ "', '" + b.getVotes().toString() + "');";
                PreparedStatement statement = DBManager.getConnection().prepareStatement(sql);
                statement.execute();
            } catch (SQLException e) {
                e.printStackTrace();
            }

    }
    public static void update(String title, String mail) {

        try {
            BibliographyEntry b = getByTitle(title);

            Integer b1 = b.getVotes() + 1;
            String sql = "update \"BibliographyEntry\" set votes = '" + b1 +"' where title = '"+ b.getTitle() +"' and author != '" + mail +"';";
            PreparedStatement statement = DBManager.getConnection().prepareStatement(sql);
            statement.execute();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public static void deleteByTitle(String title, String mail) {
        try {
            String role = AuthManager.getUserIdByMail(mail);
            System.out.println(role);
            System.out.println(role.equals("2"));
            if(role.equals("2")){
            String sql = "delete from \"BibliographyEntry\" where title='" + title + "'; ";
            PreparedStatement statement = DBManager.getConnection().prepareStatement( sql );
            statement.execute();
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static BibliographyEntry getByTitle(String title){
        try{
            String sql = "select * from \"BibliographyEntry\" where title = '" + title + "';";
            PreparedStatement stmt = DBManager.getConnection().prepareStatement( sql );
            ResultSet resultSet = stmt.executeQuery();

            while(resultSet.next()){
                Integer id = resultSet.getInt( 1 );
                String author = resultSet.getString( 2 );
                String title1 = resultSet.getString( 3 );
                String text = resultSet.getString( 4 );
                Integer votes = resultSet.getInt( 5 );
                BibliographyEntry b = new BibliographyEntry(author, title1, text, votes);
                b.setId(id);
                return b;
            }
            return null;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static Boolean isTitleUnique(String title) {
        try {
            String sql = "SELECT * FROM \"BibliographyEntry\" where title = '" + title +"';";
            PreparedStatement stmt = DBManager.getConnection().prepareStatement(sql);
            ResultSet results = stmt.executeQuery();

            while(results.next()) {
                return false;
            }
            return true;

        } catch(SQLException e) {
            e.printStackTrace();
        }

        return false;
    }




}
