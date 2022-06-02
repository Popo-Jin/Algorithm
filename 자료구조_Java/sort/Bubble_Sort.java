// 버블 정렬(Bubble Sort)
// 1. 앞에서부터 현재 원소와 바로 다음의 원소를 비교한다.
// 2. 현재 원소가 다음 원소보다 크면 원소를 교환한다.
// 3. 다음 원소로 이동하여 해당 원소와 그 다음원소를 비교한다.
// 구현이 쉽고 안정정렬이 가능하지만 교환 과정이 많아 많은 시간을 소비

package sort;

import java.util.Arrays;

public class Bubble_Sort {
    public static void main(String[] args) {
        int[] s = {4,20,15,6,9};
        bubble_sort(s, s.length);
        System.out.println(Arrays.toString(s));
    }

    public static void bubble_sort(int[] a, int size) {
        for (int i = 1; i < size; i++) {
            for (int j = 0; j < size-i; j++) {
                if(a[j] > a[j+1]) {
                    swap(a, j, j+1);
                }
            }
        }
    }

    public static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
