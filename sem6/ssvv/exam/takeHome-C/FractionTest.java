package FractionMV;

import static org.junit.Assert.*;

import org.junit.Test;

/**
 * Unit test for simple App.
 */

public class FractionTest {

    private Fraction fc1, fc2;

    @Test
    public void testSimplify() {
        fc1 = new Fraction(12, 30);
        fc1.Simplify();
        assertEquals(2, fc1.getNumerator());
        assertEquals(5, fc1.getDenominator());
    }

    @Test
    public void test_getDenominator() {
        fc1 = new Fraction(12, 30);
        int result = fc1.getDenominator();
        assertEquals(30, result);
    }

    @Test
    public void test_setDenominator() {
        fc1 = new Fraction(12, 30);
        assertEquals(30, fc1.getDenominator());
        fc1.setDenominator(1);
        assertEquals(1, fc1.getDenominator());
    }

    @Test
    public void test_getNumerator() {
        fc2 = new Fraction(6, 30);
        int result = fc2.getNumerator();
        assertEquals(6, result);
    }

    @Test
    public void test_setNumerator() {
        fc2 = new Fraction(12, 30);
        assertEquals(12, fc2.getNumerator());
        fc2.setNumerator(6);
        assertEquals(6, fc2.getNumerator());
    }

}
