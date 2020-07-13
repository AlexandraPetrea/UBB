; c) Write a function to sort a linear list with keeping the double values.

(defun insertOk (l e)
    (cond
        ((null l) (list e))
        ((or (equal (car l) l) (< e (car l))) (cons e l))
        (T (cons (car l) (insertOk (cdr l) e)))
    )
)

(defun sortare (l)
    (cond
        ((null l) nil)
        (T (insertOk (sortare (cdr l)) (car l)))
    )
)

(print (sortare '(1 3 2 5 6 7 7 3 9)))