import java.util.ArrayList;
import java.util.List;

public class Dumbo {
    private int val;
    private List<Dumbo> neighbours = new ArrayList<>();
    private boolean flashed = false;
    private Integer flashes = 0;

    public Dumbo(int val) {
        this.val = val;
    }

    public void step() {
        if (++val > 9)
            flash();
    }

    public void endTurn() {
        if (flashed)
            val = 0;
        flashed = false;
    }

    private void react() {
        if (++val > 9 && !flashed) {
            flash();
        }
    }

    public boolean flashedThisTurn() {
        return this.flashed;
    }

    public void setNeighbours(List<Dumbo> neighbours) {
        this.neighbours = neighbours;
    }

    public void addNeighbour(Dumbo d) {
        neighbours.add(d);
    }

    private void flash() {
        flashed = true;
        for (Dumbo d : neighbours) {
            d.react();
        }
        val = 0;
        flashes++;
    }

    public Integer getFlashes() {
        return this.flashes;
    }

    public int getVal() {
        return this.val;
    }

}