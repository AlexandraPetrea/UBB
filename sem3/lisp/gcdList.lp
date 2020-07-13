; 11.
; a) Determine the least common multiple of the numerical values of a nonlinear list.

(defun _lcm (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        (T (/ (* a b) (_gcd a b)))
    )
)

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
        ((listp (car l)) (_lcm (list_gcd (car l)) (list_gcd (cdr l))))
        (T (_lcm (car l) (list_gcd (cdr l))))
    )
)

(print (list_gcd '(24 ( 16 (12 A B)) 72)))
;=> 144

