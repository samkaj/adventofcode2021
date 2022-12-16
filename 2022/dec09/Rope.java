import java.util.HashSet;
import java.util.Set;

public class Rope {
    Pos head, tail;
    Set<Pos> visited;
    public Rope() {
        head = new Pos();
        tail = new Pos();
        visited = new HashSet<>();
        visited.add(tail);
    }

    public void move(String direction, int amount) {
        int dx = 0, dy = 0;
        switch(direction) {
            case "R" -> dx = 1;
            case "L" -> dx = -1;
            case "U" -> dy = 1;
            case "D" -> dy = -1;
        }
        System.out.printf("= %s %d =\n", direction, amount);
        for (int i = 0; i < amount; i++) {
            for (int y = 0; y < 6; y++) {
                for (int x = 0; x < 6; x++) {
                    if (head.getX() == x && head.getY() == y)
                        System.out.print("H");
                    else if (tail.getX() == x && tail.getY() == y) {
                        System.out.print("T");
                    } else {
                        System.out.print(".");
                    }
                }
                System.out.println();
            }
            System.out.println();
            head.move(dx, dy);
            if (!head.touches(tail)) {
                tail.moveBehind(head, dx, dy);
                visited.add(tail.visited());
            }
        }

    }

    public void printVisited() {
        for (Pos p : visited) {
            System.out.printf("(%d, %d)%n", p.getX(), p.getY());
        }
    }
    public int amountVisited() {
        return visited.size();
    }
}
