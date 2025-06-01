package silver;

import java.io.*;
import java.util.*;

public class V20055 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] belt = new int[2 * N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < 2 * N; i++) {
            belt[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> robots = new ArrayList<>();
        int zeroCount = 0;
        int step = 0;

        while (zeroCount < K) {
            step++;

            int last = belt[2 * N - 1];
            for (int i = 2 * N - 1; i > 0; i--) {
                belt[i] = belt[i - 1];
            }
            belt[0] = last;

            for (int i = 0; i < robots.size(); i++) {
                robots.set(i, (robots.get(i) + 1) % (2 * N));
            }

            robots.removeIf(pos -> pos == N - 1);

            for (int i = 0; i < robots.size(); i++) {
                int cur = robots.get(i);
                int next = (cur + 1) % (2 * N);
                if (!robots.contains(next) && belt[next] > 0) {
                    robots.set(i, next);
                    belt[next]--;
                }
            }
            robots.removeIf(pos -> pos == N - 1);

            if (belt[0] > 0 && !robots.contains(0)) {
                robots.add(0);
                belt[0]--;
            }

            zeroCount = 0;
            for (int i = 0; i < 2 * N; i++) {
                if (belt[i] == 0) {
                    zeroCount++;
                }
            }
        }

        System.out.println(step);
    }
}
