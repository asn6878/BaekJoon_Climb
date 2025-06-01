package silver;

import java.io.*;
import java.util.*;

public class II2805 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] NM = new int[2];
        for (int i = 0; i<2; i++){
            NM[i] = Integer.parseInt(st.nextToken());
        }

        int[] trees = new int[NM[0]];
        st = new StringTokenizer(br.readLine(), " ");
        int right = 0;
        for (int i = 0; i< NM[0]; i++){
            trees[i] = Integer.parseInt(st.nextToken());
            if (trees[i] > right){
                right = trees[i];
            }
        }

        int left = 0;
        int result = 0;

        while (left <= right){
            int mid = (left + right) / 2;
            long tmpSum = 0;
            for (int height: trees){
                if (height > mid){
                    tmpSum += height - mid;
                }
            }

            if (tmpSum >= NM[1]){
                result = mid;
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }

        System.out.println(result);
    }
}
