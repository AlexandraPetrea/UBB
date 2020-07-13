package thread;

import javafx.util.Pair;
import model.Matrix;

import java.util.ArrayList;
import java.util.List;

public class MatrixOperationThread extends Thread {

    Matrix a;
    Matrix b;
    Matrix result;
    List<Pair<Integer, Integer>> work;

    MatrixOperationThread(Matrix a, Matrix b, Matrix result) {
        this.a = a;
        this.b = b;
        this.result = result;
        work = new ArrayList<>();
    }

    public void addPointToWorkload(int row, int col){
        this.work.add(new Pair<>(row, col));
    }

}
