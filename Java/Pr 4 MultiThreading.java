import java.lang.*;
class MyThread extends Thread
{
private String message;
public MyThread(String message)
{
this.message = message;
}
public void run()
{
for(int i=1;i<=10;i++)
System.out.println(message);
}
}
public class ThreadClassDemo
{
public static void main(String [] args)
{
MyThread dm1 = new MyThread("Abhijit");
MyThread dm2 = new MyThread("Tarawade");
dm1.start();
dm2.start();
}
}
