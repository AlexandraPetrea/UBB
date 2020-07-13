; 10.
; a) Write a function to return the product of all the numerical atoms from a list, at superficial level.

(defun productL (l)
    (cond
        ((null l) 1)
        ((numberp (car l)) (* (car l) (productL (cdr l))))
        (T (productL (cdr l)))
    )
)

(print (productL '(1 A 2 3 (3 4 5) T)))
;=> 6
