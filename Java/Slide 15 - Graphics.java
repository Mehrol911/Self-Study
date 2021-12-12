// Drawing Strings
drawString(String s, int x, int y);
// Drawing Lines
drawLine(int x1, int y1, int x2, int y2);

// Drawing Rectangles 
drawRect(int x, int y, int w, int h); // weight // height
fillRect(int x, int y, int w, int h); 
// Drawing Rounded Rectangles
drawRoundRect(int x, int y, int w, int h, int aw, int ah);
fillRoundRect(int x, int y, int w, int h, int aw, int ah);

// Drawing Ovals
drawOval(int x, int y, int w, int h);
fillOval(int x, int y, int w, int h);

// Drawing Arcs
drawArc(int x, int y, int w, int h, int angle1, int angle2);
fillArc(int x, int y, int w, int h, int angle1, int angle2);

// Drawing Polygons
int[] x = {40, 70, 60, 45, 20};
int[] y = {20, 40, 80, 45, 60};
g.drawPolygon(x, y, x.length);

// Using Polygons
Polygon polygon = new Polygon();
    polygon.addPoint(40, 59);
    polygon.addPoint(40, 100);
    polygon.addPoint(10, 100);
    g.drawPolygon(polygon);

// Displaying Image icons
ImageIcon icon = new ImageIcon("image/us.gif");
JLabel jlblImage = new JLabel(imageIcon);
Image image = imageIcon.getImage();

