; d) Write a function to test whether a linear list is a set.

(defun contains (l e)
    (cond
        ((null l) nil)
        ((= (car l) e) T)
        (T (contains (cdr l) e))
    )
)

(defun checkSet (l)
    (cond
        ((null l) T)
        ((contains (cdr l) (car l)) nil)
        (T (checkSet (cdr l)))
    )
)

(print (checkSet '(1 2 3 4)))
;=> T

(print (checkSet '(1 2 2 3 4)))
;=> nil