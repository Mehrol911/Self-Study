/*** 1. Consider following database design (any database product i.e. MySql, Sqlite, MsSQL,,,,,,)
Database Name : MobileDB
Table Name : Mobile ***/
import java.sql.*;
public class JdbcSelectTest_insert
{
public static void main(String[] args) throws SQLException
{
Connection conn = DriverManager.getConnection ("jdbc:mysql://localhost/MobileDB?autoReconnect=true&useSSL=false", "root", "abhijit12345");
PreparedStatement stmt=conn.prepareStatement("insert into mobile values(?,?,?)");
stmt.setInt(1,3);
stmt.setString(2,"Redmi POCO");
stmt.setInt(3,250);
int i=stmt.executeUpdate();
conn.close();
}
}
