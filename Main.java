//2789

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int num = Integer.parseInt(st.nextToken());
        int max = Integer.parseInt(st.nextToken());
        String arr[] = br.readLine().split(" ");

        // System.out.println(num + " " + max);
        // System.out.println(Arrays.toString(arr));
    }
}
