import javax.swing.*;
import java.awt.*;
public class GUI
{
public static void main(String[] args)
{
JLabel jbl1 = new JLabel("Monk's Calculator");
JRadioButton r1=new JRadioButton("+");
JRadioButton r2=new JRadioButton("-");
JRadioButton r3=new JRadioButton("*");
JRadioButton r4=new JRadioButton("/");
ButtonGroup bg=new ButtonGroup();
bg.add(r1);
bg.add(r2);
bg.add(r3);
bg.add(r4);
JButton jbt= new JButton("Ok");
JPanel pan1 = new JPanel();
pan1.add(r1);
pan1.add(r2);
pan1.add(r3);
pan1.add(r4);
JPanel pan2 = new JPanel();
pan2.add(new JLabel("Value1"));
pan2.add(new JLabel("Value2"));
JPanel pan3 = new JPanel();
pan3.add(new JTextField(5));
pan3.add(new JTextField(5));
JFrame frame = new JFrame();
frame.setLayout(new GridLayout(5,1));
frame.add(jbl1);
frame.add(pan2);
frame.add(pan3);
frame.add(pan1);
frame.add(jbt);
frame.setSize(300,300);
frame.setVisible(true);
}
}
