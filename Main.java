import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] k = new String[N];
        for (int i = 0; i < k.length; i++) {
            k[i] = br.readLine();
        }
        System.out.println("Before : " + Arrays.toString(k));
        quicksort(k);
        System.out.println("After : " + Arrays.toString(k));

    }

    public static void quicksort(String s[]) {
        int start = 0;
        int end = s.length;
        int pivot = start;
        String temp = "";
        System.out.println(s.length);
        for (int i = 0; i < s.length; i++) {
            if (s[start+i].length() < s[end-1-i].length()) {
                return;
            }
            if (s[start+i].length() == s[end].length()) {
                if (s[start+i].compareTo(s[end]) > 0) {
                    temp = s[end];
                    s[end] = s[start+i];
                    s[start+i] = temp;
                } else {
                    return;
                }
            }
            if (s[start+i].length() > s[end].length()) {
                temp = s[end];
                s[end] = s[start+i];
                s[start+i] = temp;
            }
            System.out.println("s[start+i].length : " + s[start+i].length());
            System.out.println("s[start+i].length : " + s[end].length());
        }
    }
}
