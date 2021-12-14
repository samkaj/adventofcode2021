import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

class Dec11 {
    public static void main(String[] args) {
        partOne(getDumbos());
        partTwo(getDumbos());
    }

    private static void partOne(List<List<Dumbo>> dumbos) {
        int steps = 100;
        for (int i = 0; i < steps; i++) {
            dumbos.forEach(d -> d.forEach(Dumbo::step));
            dumbos.forEach(d -> d.forEach(Dumbo::endTurn));
        }

        System.out.println();
        int sum = 0;
        for (List<Dumbo> list : dumbos)
            for (Dumbo d : list)
                sum += d.getFlashes();

        System.out.println(String.format("Flashes after %d steps: %d", steps, sum));
    }

    private static void partTwo(List<List<Dumbo>> dumbos) {
        int steps = 0;
        boolean flashed = false;
        while (!flashed) {
            dumbos.forEach(d -> d.forEach(Dumbo::step));
            flashed = allFlashed(dumbos);
            dumbos.forEach(d -> d.forEach(Dumbo::endTurn));
            steps++;
        }
        System.out.println(String.format("All octopuses flashed simultaneously at step %d", steps));
    }

    private static boolean allFlashed(List<List<Dumbo>> dumbos) {
        for (List<Dumbo> list : dumbos)
            for (Dumbo d : list)
                if (!d.flashedThisTurn())
                    return false;
        return true;
    }

    private static List<List<Dumbo>> getDumbos() {
        String thisLine;
        List<List<Dumbo>> dumbos = new ArrayList<>();
        try {
            BufferedReader br = new BufferedReader(new FileReader("input.txt"));

            while ((thisLine = br.readLine()) != null) {
                dumbos.add(dumboLine(thisLine));
            }

            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        for (int i = 0; i < dumbos.size(); i++) {
            for (int j = 0; j < dumbos.get(i).size(); j++) {
                setNeighbours(dumbos, dumbos.get(i).get(j), i, j);
            }
        }

        return dumbos;
    }

    private static void setNeighbours(List<List<Dumbo>> dumbos, Dumbo d, int x, int y) {
        int maxX = dumbos.size() - 1;
        int maxY = dumbos.get(0).size() - 1;
        if (x > 0) {
            d.addNeighbour(dumbos.get(x - 1).get(y));
            if (y > 0)
                d.addNeighbour(dumbos.get(x - 1).get(y - 1));
            if (y < maxY)
                d.addNeighbour(dumbos.get(x - 1).get(y + 1));
        }
        if (x < maxX) {
            d.addNeighbour(dumbos.get(x + 1).get(y));
            if (y > 0)
                d.addNeighbour(dumbos.get(x + 1).get(y - 1));
            if (y < maxY)
                d.addNeighbour(dumbos.get(x + 1).get(y + 1));
        }
        if (y > 0)
            d.addNeighbour(dumbos.get(x).get(y - 1));
        if (y < maxY)
            d.addNeighbour(dumbos.get(x).get(y + 1));

    }

    private static List<Dumbo> dumboLine(String line) {
        List<Dumbo> dumbos = new ArrayList<>();
        for (char c : line.toCharArray())
            dumbos.add(new Dumbo(Character.getNumericValue(c)));
        return dumbos;
    }
}