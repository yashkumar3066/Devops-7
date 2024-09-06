import java.util.Arrays;
import java.util.Random;

public class SearchSort {

    public static void main(String[] args) {
        int arr[] = getRandomArray(10);
        printArray(arr);
        Arrays.sort(arr);
        System.out.println("Sorted Array");
        printArray(arr);
    }

    private static void printArray(int[] arr) {
        // TODO Auto-generated method stub
        System.out.println(Arrays.toString(arr));
    }

    private static int[] getRandomArray(int i) {
        // TODO Auto-generated method stub

        Random random = new Random();
        int[] arr = new int[i];
        for (int j = 0; j < i; j++) {
            arr[j] = random.nextInt(100);
        }
        return arr;

    }
}
