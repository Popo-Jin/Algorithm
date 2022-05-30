import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JAVA_TEST {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int i = Integer.parseInt(br.readLine());
        System.out.println(s + i);
    }
    
}
