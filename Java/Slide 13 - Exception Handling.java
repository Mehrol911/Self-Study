// Declaring exceptions
// Every method must state the types of checked exceptions it might throw. This is known as declaring exceptions. 

public void myMethod()
   throws IOException
public void myMethod()
   throws IOException, OtherException

//-----------------------------------------
/** Set a new radius */
// Throwing exception
  public void setRadius(double newRadius) 
      throws IllegalArgumentException 
{
    if (newRadius >= 0)
      radius =  newRadius;
    else
      throw new IllegalArgumentException(
        "Radius cannot be negative");
}

//-----------------------------------------
//Catching exceptions
try {
  statements;  // Statements that may throw exceptions
}
catch (Exception1 exVar1) {
  handler for exception1;
}
catch (Exception2 exVar2) { 
  handler for exception2;
}
...
catch (ExceptionN exVar3) {
  handler for exceptionN;
} 

