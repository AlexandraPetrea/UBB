; b) Write a function to return the product of all numerical atoms in a list, at any level.

(defun prod (l)
    (cond 
        ((null l) 1)
        ((listp (car l)) (* (prod (car l)) (prod (cdr l))))
        ((numberp (car l)) (* (car l) (prod (cdr l))))
        (T (prod (cdr l)))
    )
)

(print (prod '(5 ( 1 2 3 (6 (8 9) 7)))))