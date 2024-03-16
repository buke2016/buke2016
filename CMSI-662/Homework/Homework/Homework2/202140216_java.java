// OBJ11-J. Be wary of letting constructors throw exceptions
// Compliant example:
public class Resource {
  private final int resource;


  public Resource() {
      try {
          resource = initializeResource();
      } catch (Exception e) {
          throw new RuntimeException("Failed to initialize", e);
      }
  }

  private int initializeResource() {
      // Initialization logic that might throw an exception
      return 1;
  }
}


// Non-compliant example:
public class MyClass {
  private final String name;


  public MyClass(String name) {
    if (name == null) {
      throw new IllegalArgumentException("Name cannot be null");
    }
    if (name.isEmpty()) {
      throw new IllegalArgumentException("Name cannot be empty");
    }
    this.name = name;
  }
}

// EXP00-J. Do not ignore values returned by methods:
// Compliant Example:
public class CheckReturn {
  public static void main(String[] args) {
      String str = "Hello, World!";
      boolean result = str.isEmpty();  // Use the return value
      if (!result) {
          System.out.println("String is not empty");
      }
  }
}

// Non-compliant example:
public class NonCompliantCheckReturn {
  public static void main(String[] args) {
    String str = "Hello, World!";
    str.isEmpty(); // Ignoring the return value
    System.out.println("String is not empty"); // Assuming str is not empty
  }
}

// NUM09-J. Do not use floating-point variables as loop counters:
//  Compliant Example:
import java.math.BigDecimal;
public class PreciseComputation {
    public static void main(String[] args) {
        BigDecimal a = new BigDecimal("0.1");
        BigDecimal b = new BigDecimal("0.2");
        BigDecimal c = a.add(b);  // Precise computation
        System.out.println(c);  // Outputs "0.3"
    }
}

// Non-compliant Example:
public class NonPreciseComputation {
  public static void main(String[] args) {
    double a = 0.1;
    double b = 0.2;
    double c = a + b; // Unpredictable precision due to floating-point limitations
    System.out.println(c); // Output might not be exactly 0.3
  }
}
