import org.javatuples.Pair;
import org.thavam.util.concurrent.blockingMap.BlockingHashMap;

import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    static final int size = 5;
    static final boolean print = true;

    public static void main(String[] args) throws InterruptedException {

        BlockingHashMap<Pair<Integer, Integer>, Integer> m1 = new BlockingHashMap<>();
        BlockingHashMap<Pair<Integer, Integer>, Integer> m2 = new BlockingHashMap<>();
        BlockingHashMap<Pair<Integer, Integer>, Integer> m3 = new BlockingHashMap<>();
        Integer[][] m_result_m = new Integer[size][size];
        long avg=0;
        int it=250;

            BlockingHashMap<Pair<Integer, Integer>, Integer> m_result = new BlockingHashMap<>();
            BlockingHashMap<Pair<Integer, Integer>, Integer> m_partial_result = new BlockingHashMap<>();

            for (int aux = 0; aux < it; aux++) {
                long start = System.nanoTime();
                int nrthreads = size*size;

                ArrayList<Pair<Integer, Integer>> positions = new ArrayList<>();
                ArrayList<ArrayList<Pair<Integer, Integer>>> multiplier_list = new ArrayList<>();

                for (int i = 0; i < nrthreads; i++) {
                    multiplier_list.add(new ArrayList<>());
                }

                for (int i = 0; i < size; i++) {
                    for (int j = 0; j < size; j++) {
                        positions.add(Pair.with(i, j));
                        m1.put(Pair.with(i, j), i+j);
                        m2.put(Pair.with(i, j), 1);
                        m3.put(Pair.with(i, j), 1);
                    }
                }

                positions.forEach(p -> multiplier_list.get(positions.indexOf(p) % nrthreads).add(positions.get(positions.indexOf(p))));

                ArrayList<Multiplier> multipliers = new ArrayList<>();
                ArrayList<Multiplier> multipliers2 = new ArrayList<>();

                for (int i = 0; i < nrthreads; i++) {
                    multipliers.add(new Multiplier(m1, m2, m_partial_result, multiplier_list.get(i)));
                }
                for (int i = 0; i < nrthreads; i++) {
                    multipliers2.add(new Multiplier(m_partial_result, m3, m_result, multiplier_list.get(i)));
                }

                ExecutorService executorService = Executors.newFixedThreadPool(5);

                executorService.invokeAll(multipliers);
                ExecutorService executorService2 = Executors.newFixedThreadPool(5);

                executorService2.invokeAll(multipliers2);

                IntStream.range(0, size).mapToObj(iii -> IntStream.range(0, size).mapToObj(jjj -> m_result_m[iii][jjj] = m_result.get(Pair.with(iii, jjj))).collect(Collectors.toList())).collect(Collectors.toList());


                if (print) {
                    for (int i = 0; i < size; i++) {
                        for (int j = 0; j < size; j++) {
                            System.out.print(m_result_m[i][j] + "\t");
                        }
                        System.out.print("\n");
                    }
                }
//                System.out.println("Multiplied in:" + ((System.nanoTime() - start) / 1000000) + " ms ");
                avg+=((System.nanoTime() - start) );
            }
            System.out.println("Done avg. of "+it+" runs: "+avg/it/1000000);
        }

    }
