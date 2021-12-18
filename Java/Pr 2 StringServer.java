import java.io.*;
import java.net.*;
import java.util.*;
public class ServerAB
{
public static void main(String[] args)
{
new ServerAB();
}
public ServerAB()
{
try
{
ServerSocket serverSocket = new ServerSocket(8000);
Socket socket = serverSocket.accept();
DataInputStream inputFromClient = new DataInputStream(
socket.getInputStream());
while (true)
{
String str = inputFromClient.readUTF();
System.out.println(str.length());
}
}
catch(IOException ex)
{
System.err.println(ex);
}
}
}
