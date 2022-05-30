//2789

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int num = Integer.parseInt(st.nextToken());
        int max = Integer.parseInt(st.nextToken());
        int max_result = 0;
        String arr[] = br.readLine().split(" ");
        for(int i=0;i<arr.length;i++) {
            for (int j = i+1; j < arr.length; j++) {
                for (int k = j+1; k < arr.length; k++) {
                    int result = Integer.parseInt(arr[i])+Integer.parseInt(arr[j])+Integer.parseInt(arr[k]);
                    if(result > max_result && result <= max ) {
                        max_result = result;
                    }
                }
            }
        }
        System.out.println(max_result);
        // System.out.println(num + " " + max);
        // System.out.println(Arrays.toString(arr));
    }
}
