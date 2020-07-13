package com.sample.repositories;

import com.sample.model.User;

import java.sql.*;

public class UserRepository {
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:postgresql://localhost:5432/postgres";

    static final String DbUser = "postgres";
    static final String DbPassword = "alex";

    public User getUser(String username)
    {
        Connection conn = null;
        Statement stmt = null;

        try {
            Class.forName("com.mysql.jdbc.Driver");

            conn = DriverManager.getConnection(DB_URL, DbUser, DbPassword);

            stmt = conn.createStatement();
            String sql = "SELECT * FROM User WHERE username = '" + username + "'";
            ResultSet rs = stmt.executeQuery(sql);

            if (!rs.next()) {
                return null;
            }

            User user = new User();
            user.Id = rs.getInt("id");
            user.Username = rs.getString("username");
            user.Password = rs.getString("password");

            rs.close();
            stmt.close();
            conn.close();

            return user;
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        finally {
            try {
                if (stmt != null) {
                    stmt.close();
                }
            } catch (SQLException ex2) {}
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException ex2) {}
        }

        return null;
    }
}