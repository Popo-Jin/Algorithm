//삽입정렬(Insertion_sort)
//제자리정렬, 안정정렬이라고 한다.
//1. 현재 타겟이 되는 숫자와 이전 위치에 있는 원소들을 비교한다. (첫 번째 타겟은 두 번째 원소부터 시작한다.)
//2. 타겟이 되는 숫자가 이전 위치에 있던 원소보다 작다면 위치를 서로 교환한다.
//3. 그 다음 타겟을 찾아 위와 같은 방법으로 반복한다. 
//정렬이 어느정도 되어있는 경우에 효율적
//최선의 경우 O(N), 최악의 경우 O(N^2)

package sort;
import java.util.Arrays;

public class Insertion_Sort {
    public static void main(String[] args) {
        int s[] = {8,4,2,1,5};
        insertion_sort(s, s.length);
        System.out.println(Arrays.toString(s));
    }

    public static void insertion_sort(int[] a, int size) {
        
        for (int i = 1; i < size; i++) {
            int target = a[i]; //target은 1부터
            int j=i-1; //J는 이전 원소

            while (j>=0 && target<a[j]) { //이전 원소가 0보다 크고 타겟보다 클 경우
                a[j+1] = a[j];
                j--;
            }

            a[j+1] = target;

        }
    }
}
