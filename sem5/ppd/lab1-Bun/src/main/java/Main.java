import com.google.common.util.concurrent.AtomicDouble;
import org.javatuples.Pair;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static final int SALES = 50000;
    private static final int MIN_SALE_QUANTITY = 1;
    private static final int MAX_SALE_QUANTITY = 20;
    private static final int CHECK_FREQUENCY = 30;

    public static void main(String[] args) throws InterruptedException {

        ExecutorService executor = Executors.newFixedThreadPool(500);
        ScheduledExecutorService scheduledExecutorService = new ScheduledThreadPoolExecutor(1);

        ReadWriteLock billsLock = new ReentrantReadWriteLock();

        ArrayList<Product> products = new ArrayList<>();
        ArrayBlockingQueue<List<Pair<String, Integer>>> bills = new ArrayBlockingQueue<>(SALES);

        AtomicDouble money = new AtomicDouble(0);

        products.add(new Product("sugar", 2.1, 1200));
        products.add(new Product("flour", 5.0, 2300));
        products.add(new Product("mango", 1.5, 6780));
        products.add(new Product("gem", 2.2, 2000));
        products.add(new Product("oil", 2.1, 2500));


        ArrayList<Sale> callables = new ArrayList<>();


/**
 * Random generation of sales
 */
        for (int i = 0; i < SALES; i++) {

            List<Pair<Product, Integer>> sale = new ArrayList<>();

            for (Product product : products) {
                sale.add(Pair.with(product, (int) (Math.random() * (MAX_SALE_QUANTITY - MIN_SALE_QUANTITY) + MIN_SALE_QUANTITY)));
            }
            Sale saleProcessor = new Sale(sale, bills, money, billsLock);
            callables.add(saleProcessor);
        }


        long start2 = System.nanoTime();

        BillCheck billCheck = new BillCheck(products, bills, money, billsLock);
        scheduledExecutorService.scheduleAtFixedRate(billCheck, 0, CHECK_FREQUENCY, TimeUnit.MILLISECONDS);

        executor.invokeAll(callables);

        System.out.println("DONE!");
        executor.submit(billCheck);

        scheduledExecutorService.shutdown();


        System.out.println("Completed in:" + ((System.nanoTime() - start2) / 1000000));

    }
}
