import model.Matrix;
import thread.MatrixAdditionThread;
import thread.MatrixMultiplicationThread;
import thread.MatrixOperationThread;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.lang.Math.min;

enum MatrixOperation {
    ADD, MULTIPLY
}

public class Main {

    private static Matrix operation(MatrixOperation op, Matrix a, Matrix b, int threadCount) throws Exception {
        int rowCount = min(a.getRowsNumber(), b.getRowsNumber());
        int colCount = min(a.getColsNumber(), b.getColsNumber());

        Matrix result = new Matrix(rowCount, colCount);

        List<MatrixOperationThread> threads = new ArrayList<>();

        switch (op){
            case ADD:
                for (int i = 0; i < threadCount; i++){
                    threads.add(new MatrixAdditionThread(a, b, result));
                }
                break;
            case MULTIPLY:
                for (int i = 0; i < threadCount; i++){
                    threads.add(new MatrixMultiplicationThread(a, b, result));
                }
                break;
            default:
                throw new Exception("Invalid operation");
        }

        for (int row = 0; row < result.getRowsNumber(); row++){
            for(int col = 0; col < result.getRowsNumber(); col++){
                threads.get(result.index(row, col) % threadCount).addPointToWorkload(row, col);
            }
        }

        for (int i = 0; i < threadCount; i++){
            threads.get(i).start();
        }


        for (int i = 0; i < threadCount; i++){
            threads.get(i).join();
        }
        return result;
    }


    public static void main(String[] args) throws Exception {

        Matrix a = new Matrix(500, 500);
        Matrix b = new Matrix(500, 500);

        float start =  System.nanoTime() / 1000000;
        operation(MatrixOperation.ADD, a, b, 500);
        float end = System.nanoTime() / 1000000;

        System.out.println("Time for add:");
        System.out.println(end - start);

        //Checks
        /*
        Matrix a1 = new Matrix(2, 2);
        List list = Arrays.asList(1, 2);
        List list2 = Arrays.asList(2,3);
        List list3 = Arrays.asList(1, 1);

        a1.setRow(0, list);
        a1.setRow(1, list2 );
        System.out.println(a1);

        Matrix a2 = new Matrix(2,2);
        a2.setRow(0, list3);
        a2.setRow(1, list3);

        System.out.println(a2);

        //   Matrix aux = new Matrix(2,2);
        System.out.println(operation(MatrixOperation.MULTIPLY, a1, a2, 4));

         */

        /*thread count:1 -> 4325
        //             10 -> 2240
        //             100 -> 1024
        //             1000 -> 2624

        Multiply : thread count: 1 -> 128.0
                                 10 -> 192.0
                                 100 -> 256.0
                                 500 -> 320.0
                                 1000 -> 448.0
         */
        float start1 =  System.nanoTime() / 1000000;
         operation(MatrixOperation.MULTIPLY, a, b, 500);
        float end1 = System.nanoTime() / 1000000;

        System.out.println("Time for multiply:");
        System.out.println(end1 - start1);




    }
}
