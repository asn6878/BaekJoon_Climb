package silver;

import java.io.*;
import java.util.*;

public class II2512 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] budgets = new int[N];
        for (int i = 0; i < N; i++){
            budgets[i] = Integer.parseInt(st.nextToken());
        }
        int budget = Integer.parseInt(br.readLine());

        Arrays.sort(budgets);

        int lim = 1;
        int tmpSum = 0;
        for (int i = 0; i < N; i++){
            if ((tmpSum + (budgets[i] * (N - i))) < budget){
                lim++;
                tmpSum += budgets[i];
            } else if ((tmpSum + (budgets[i] * (N - i))) > budget){
                break;
            } else{
                System.out.println(budgets[i]);
                return;
            }
        }

        if (lim == 1){
            System.out.println(budget / N);
        } else if (lim < N) {
            int tmpLim = budget - (tmpSum + budgets[lim-2] * (N - lim + 1));
            int left = tmpLim / (N - lim + 1);
            System.out.println(budgets[lim-2] + left);
        } else{
            System.out.println(budgets[N - 1]);
        }
    }
}
