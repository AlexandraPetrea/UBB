
import java.security.InvalidParameterException;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;

class Product {
    String name;
    private AtomicInteger quantity;
    Double price;

    Product(String name, Double price, Integer quantity) {
        this.name = name;
        this.price = price;
        this.quantity = new AtomicInteger(quantity);
    }

    Product(Product p) {
        this.name = p.name;
        this.price = p.price;
        this.quantity = p.quantity;
    }


    synchronized void sale(Integer nr) throws InvalidParameterException {
        if (nr < quantity.get()) {
            quantity.addAndGet(-nr);
        } else
            throw new InvalidParameterException("Not enough Items!");
    }
}

