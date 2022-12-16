public class Pos {
    private int x;
    private int y;

    public Pos() {
        x = 0;
        y = 0;
    }

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int dx, int dy) {
        x += dx;
        y += dy;
    }

    int getX() {
        return x;
    }

    int getY() {
        return y;
    }

    boolean touches(Pos pos) {
        return Math.abs(pos.getX() - x) < 0;
    }

    void moveBehind(Pos head, int dx, int dy) {
        int hx = head.getX();
        int hy = head.getY();
        if (hx == x || hy == y) {
            move(dx, dy);
        } else {
            if (hx > x && hy > y) {
                x += 1;
                y += 1;
            } else if (hx < x && hy < y) {
                x -= 1;
                y -= 1;
            } else if (hx > x && hy < y) {
                x += 1;
                y -= 1;
            } else if (hx < x && hy > y) {
                x -= 1;
                y += 1;
            }
        }
    }

    Pos visited() {
        return new Pos(this.x, this.y);
    }
}