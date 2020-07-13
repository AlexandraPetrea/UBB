
import com.google.common.util.concurrent.AtomicDouble;
import org.javatuples.Pair;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;
import java.util.concurrent.locks.ReadWriteLock;

/**
 * handles the sales
 */
class Sale implements Callable<List<Pair<String, Integer>>> {

    private List<Pair<Product, Integer>> sale;
    private final BlockingQueue<List<Pair<String, Integer>>> bills;
    private AtomicDouble money;
    private ReadWriteLock billsLock;

    Sale(List<Pair<Product, Integer>> sale, BlockingQueue<List<Pair<String, Integer>>> bills, AtomicDouble money, ReadWriteLock billsLock) {
        this.sale = sale;
        this.bills = bills;
        this.money = money;
        this.billsLock = billsLock;
    }

    public List<Pair<String, Integer>> call() {

        ArrayList<Pair<String, Integer>> result = new ArrayList<>();

        billsLock.readLock().lock();

        sale.forEach(p ->
                {
                    Product product = p.getValue0();
                    Integer number = p.getValue1();

                    try {
                        product.sale(number);
                        result.add(Pair.with(p.getValue0().name, p.getValue1()));
                        money.addAndGet(product.price * number);
                    } catch (Exception e) {
//                                System.out.println("Not enough "+ product.name+ " !");
                    }
//                    finally {
//                                System.out.println("Sold "+p.getValue1()+" "+p.getValue0().name);
//                    }


                }
        );

        this.bills.add(result);

        billsLock.readLock().unlock();

        return null;

    }

}
