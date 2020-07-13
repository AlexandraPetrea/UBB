; d) Write a function to transform a linear list into a set.

(defun transform_set (l)
    (cond
        ((null l) nil)
        (T (cons (car l) (transform_set (remove_apparences (cdr l) (car l)))))
    )
)

(defun remove_apparences (l e)
    (cond
        ((null l) nil)
        ((= (car l) e) (remove_apparences (cdr l) e))
        (T (cons (car l) (remove_apparences (cdr l) e)))
    )
)

(print (transform_set '(1 2 3 44 2 4  5 2 3 3 3 3 4 4 5 77)))