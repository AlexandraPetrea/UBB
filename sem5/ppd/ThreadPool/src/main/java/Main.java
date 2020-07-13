
import model.Matrix;
import runnables.Addition;
import runnables.Multiplication;
import runnables.Operation;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import static java.lang.Math.min;

enum OperationEnum{
    ADD, MULTIPLY
}
public class Main {

    private static Matrix operation(OperationEnum op, Matrix a, Matrix b, int taskCount, int threadCount) throws Exception {
        int rowCount = min(a.getRowsNumber(), b.getRowsNumber());
        int colCount = min(a.getColsNumber(), b.getColsNumber());

        Matrix sum = new Matrix(rowCount, colCount);

        List<Operation> tasks = new ArrayList<>();

        switch (op){
            case ADD:
                for (int i = 0; i < taskCount; i++){
                    tasks.add(new Addition(a, b, sum));
                }
                break;
            case MULTIPLY:
                for (int i = 0; i < taskCount; i++){
                    tasks.add(new Multiplication(a, b, sum));
                }
                break;
            default:
                throw new Exception("MatrixOperationEnum not recognized");
        }

        for (int row = 0; row < sum.getRowsNumber(); row++){
            for(int col = 0; col < sum.getRowsNumber(); col++){
                tasks.get(sum.index(row, col) % taskCount).addPointToWorkload(row, col);
            }
        }

        ExecutorService pool = Executors.newFixedThreadPool(threadCount);

        for (Operation task : tasks){
            pool.execute(task);
        }

        pool.shutdown();

        return sum;
    }


    public static void main(String[] args) throws Exception {

        Matrix a = new Matrix(2, 2);
        Matrix b = new Matrix(2, 2);

        float start =  System.nanoTime() / 1000000;
        System.out.println("Time for add: ");
        operation(OperationEnum.ADD, a, b, 200, 500);

        float end = System.nanoTime() / 1000000;

        System.out.println(end - start);


        float start1 =  System.nanoTime() / 1000000;
        System.out.println("Time for multiply: ");
        System.out.println(a);
        System.out.println(b);
        Matrix aux = operation(OperationEnum.MULTIPLY, a, b, 200, 500);
        System.out.println(aux);
        Matrix c = new Matrix(2, 2);
        Matrix aux2 = operation(OperationEnum.MULTIPLY, aux, c, 200, 500);
        System.out.println(aux2);
        float end1 = System.nanoTime() / 1000000;

        System.out.println(end1 - start1);
    }
}
