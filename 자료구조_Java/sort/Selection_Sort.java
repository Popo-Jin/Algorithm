//선택 정렬(Selection_Sort)
// 1. 주어진 리스트에서 최솟값을 찾는다.
// 2. 최솟값을 맨 앞 자리의 값과 교환한다.
// 3. 맨 앞 자리를 제외한 나머지 값들 중 최솟값을 찾아 위와 같은 방법으로 반복한다. 
// 시간복잡도가 O(N^2)


package sort;

import java.util.Arrays;

public class Selection_Sort {
    public static void main(String[] args) {
        int[] s = {4,6,2,10,5};
        selection_sort(s, s.length);
        System.out.println(Arrays.toString(s));
    }

    public static void selection_sort(int[] a, int size) {
        
        for (int i = 0; i < a.length; i++) {
            int min_index = i;

            for (int j = i+1; j < size; j++) {
                if(a[j] < a[min_index]) {
                    min_index = j;
                }
            }

            swap(a, min_index, i);
            
        }
        
    }

    public static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
