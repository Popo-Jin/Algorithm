package solved;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class JAVA_2750 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] Arr = new Integer[N];

        try {
            for(int i=0;i<N;i++) {
                Arr[i] = Integer.parseInt(br.readLine());
            }    
            Arrays.sort(Arr);
            for(int i=0;i<N;i++) {
                System.out.println(Arr[i]);
            }
        } catch (Exception e) {
            System.out.println("Wrong IO");
        }
    }
}