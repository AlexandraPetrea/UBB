; a) Write a function to insert an element E on the n-th position of a linear list.

(defun insertN (l e n)
    (cond
        ((equal n 1) (cons e l))
        (T (cons (car l) (insertN (cdr l) e (- n 1))))
    )
)

(print (insertN '(1 2 3 4) 'A '2))
