//10815

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.file.FileStore;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{

        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // int N = Integer.parseInt(br.readLine());
        // int[] arrN = new int[N];
        // StringTokenizer st = new StringTokenizer(br.readLine());
        // for (int i = 0; i < arrN.length; i++) {
        //     arrN[i] = Integer.parseInt(st.nextToken());
        // }
        // int M = Integer.parseInt(br.readLine());
        // int[] arrM = new int[M];
        // for (int i = 0; i < arrM.length; i++) {
        //     arrM[i] = Integer.parseInt(st.nextToken());
        // }
        int[] arr_test = {4,20,49,1,5,8,3,6};
        System.out.println(Arrays.toString(arr_test));
        mergesort(arr_test);
        System.out.println(Arrays.toString(arr_test));

    }

    private static void mergesort(int[] arr) {
        int tmp[] = new int[arr.length];
        mergesort(arr, tmp, 0, arr.length-1);
    }

    private static void mergesort(int[] arr, int[] tmp, int start, int end) {
        if(start < end) {
            int mid = (start + end) / 2;
            mergesort(arr, tmp, start, mid);
            mergesort(arr, tmp, mid+1, end);
            merge(arr, tmp, start, mid, end);

        }
    }

    private static void merge(int[] arr, int[] tmp, int start, int mid, int end) {
        int left = start;
        int right = mid+1;
        int index = start;

        // for(int i=left;i)
        if (arr[left] > arr[right]) {
            tmp[index] = arr[left];
            left++;
        } else {
            tmp[index] = arr[right];
            right++;
        }
        index++;

        for (int i = index; i < mid; i++) {
            tmp[index] = arr[left];
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = tmp[i];
        }
    }
}