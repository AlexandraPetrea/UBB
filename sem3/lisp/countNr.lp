; d) Write a function to return the number of all numerical atoms in a list at superficial level.

(defun countNumbers (l)
    (cond
        ((null l) 0)
        ((numberp (car l)) (+ 1 (countNumbers (cdr l))))
        (T (countNumbers (cdr l)))
    )
)

(print (countNumbers '(1 2 s 5 (6) fg 5)))
;=> 4