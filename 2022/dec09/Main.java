import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("sample.txt"));
        String line, direction;
        int amount;
        String[] motion;
        Rope rope = new Rope();
        // 8903 too high
        while (reader.ready()) {
            line  = reader.readLine().trim();
            motion = line.split(" ");
            direction = motion[0];
            amount = Integer.parseInt(motion[1]);
            rope.move(direction, amount);
        }
        rope.printVisited();
        System.out.println(rope.amountVisited());
    }
}
