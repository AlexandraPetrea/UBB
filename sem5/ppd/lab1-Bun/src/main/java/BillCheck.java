
import com.google.common.util.concurrent.AtomicDouble;
import org.javatuples.Pair;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.locks.ReadWriteLock;

/**
 * This runnable performs the stock checks and prints the result
 */
public class BillCheck implements Runnable {

    private final List<Product> initial_products;

    private List<Product> products;

    private BlockingQueue<List<Pair<String, Integer>>> bills;

    private static BlockingQueue<List<Pair<String, Integer>>> allBills = new ArrayBlockingQueue<>(Main.SALES);

    private AtomicDouble money;

    private ReadWriteLock billsLock;

    BillCheck(List<Product> products, BlockingQueue<List<Pair<String, Integer>>> bills, AtomicDouble money, ReadWriteLock billsLock) {
        this.products = products;
        this.bills = bills;
        this.money = money;
        this.billsLock = billsLock;
        this.initial_products = new ArrayList<>();
        products.forEach(p -> initial_products.add(new Product(p)));
    }

    @Override
    public void run() {

        HashMap<String, Integer> record = new HashMap<>();
        products.forEach(product -> record.put(product.name, 0));
        AtomicDouble sum = new AtomicDouble(0);

        billsLock.writeLock().lock();

        Double tempMoney = money.get();
        bills.drainTo(allBills);


        allBills.forEach(bill -> bill.forEach(pair -> {
            String product = pair.getValue0();
            Integer number = pair.getValue1();
            number += (Integer) record.get(product);
            record.put(product, number);
        }));


        System.out.println("Number of sales " + allBills.size());
        record.forEach((product, number) -> {
            sum.addAndGet(initial_products.stream().filter(p -> p.name.equals(product)).findFirst().get().price * (Integer) number);
            System.out.println("Sold in total " + number + " " + product + "s!");
        });
        System.out.printf("Expected: %.2f," +
                "\nGot:      %.2f\n", sum.get(), tempMoney);


         billsLock.writeLock().unlock();
    }
}
