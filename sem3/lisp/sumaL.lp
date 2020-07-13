; b) Write a function to return the sum of all numerical atoms of a list, at any level.

(defun suma (l)
    (cond
        ((null l) 0)
        ((numberp (car l)) (+ (car l) (suma (cdr l))))
        ((listp (car l)) (+ (suma (car l)) (suma (cdr l))))
        (T (suma (cdr l)))
    )
)

(print (suma '(1 2 (3 4 (A 8) (B)))))