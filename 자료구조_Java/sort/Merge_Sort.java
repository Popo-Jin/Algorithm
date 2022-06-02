package sort;

import java.util.Arrays;

public class Merge_Sort {
    public static int[] src;
    public static int[] tmp;
    public static void main(String[] args) {
        src = new int[]{1,9,10,4,2,5,6,8};
        tmp = new int[src.length];
        merge_sort(0, src.length-1);
        System.out.println(Arrays.toString(src));
    }

    public static void merge_sort(int start, int end) {
        if(start < end) {
            int mid = (start+end) / 2;
            merge_sort(start, mid);
            merge_sort(mid+1, end);

            int p = start;
            int q = mid+1;
            int idx = p;

            while(p<=mid || q<=end) {
                if(q>end || (p<=mid && src[p]<=src[q])) {
                    tmp[idx++] = src[p++];
                } else {
                    tmp[idx++] = src[q++];
                }
            }

            for (int i = start; i <= end; i++) {
                src[i] = tmp[i];
            }
        }
    }
}
