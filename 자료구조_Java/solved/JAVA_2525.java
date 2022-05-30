package solved;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class JAVA_2525 {
    public static void main(String[] args) throws IOException { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(br.readLine());
        if((b+c)/60 > 0) {
            if((a+(b+c)/60) >= 24) {
                a += (b+c)/60;
                b = (b+c)%60;
                a -= 24;
            }
            else {
                a += (b+c)/60;
                b = (b+c)%60;
            }
        }
        else {
            b = (b+c)%60;
        }
        System.out.println(a + " " + b);
    }
}
