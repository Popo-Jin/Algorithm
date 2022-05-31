import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class JAVA_TEST {
    public static void main(String[] args) throws IOException {
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String s = br.readLine();
        // int i = Integer.parseInt(br.readLine());
        // System.out.println(s + i);
        String[] s = new String("im").split("");
        String a = "im";
        System.out.println(Arrays.toString(s));
        // for(int i=0;i<s.length;i++) {
            byte[] bytes = a.getBytes(StandardCharsets.US_ASCII);
            System.out.println(bytes[1]);
        // }
        int a_a = 'i';
        System.out.println(a_a);
        
    }
    
}
