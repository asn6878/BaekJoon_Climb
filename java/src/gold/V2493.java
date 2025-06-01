package gold;

import java.util.*;
import java.io.*;

public class V2493 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        Stack<Tower> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++){
            int height = Integer.parseInt(st.nextToken());
            Tower t = new Tower(i+1, height);

            while(true){
                if (stack.isEmpty()){
                    sb.append("0 ");
                    stack.push(t);
                    break;
                }

                Tower p = stack.peek();
                if (t.height < p.height){
                    sb.append(p.idx + " ");
                    stack.push(t);
                    break;
                } else{
                    stack.pop();
                }
            }
        }
        System.out.println(sb.toString().trim());
    }
}

class Tower{
    public int idx;
    public int height;

    public Tower(int idx, int height){
        this.idx = idx;
        this.height = height;
    }
}
