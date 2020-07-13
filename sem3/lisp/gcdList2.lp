; d) Write a function to return the greatest common divisor of all numbers in a linear list.

(defun _gcd (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        ((equal b 0) a)
        (T (_gcd b (mod a b)))
    )
)

(defun list_gcd (l)
    (cond
        ((and (atom (car l)) (null (cdr l))) (car l))
        ((listp (car l)) (_gcd (list_gcd (car l)) (list_gcd (cdr l))))
        (T (_gcd (car l) (list_gcd (cdr l))))
    )
)

(print (list_gcd '(24 ( 16 (12 A B)) 72)))
;=> 4