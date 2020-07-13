; d) Write a function that deletes from a linear list of all occurrences of the minimum element.

(defun min_nb (a b)
    (if (< a b) a b)
)


(defun min_num (l)
    (cond
        ((null l) 999999)
        ((and (null (cdr l)) (numberp (car l))) (car l))
        ((numberp (car l)) (min_nb (car l) (min_num (cdr l))))
        ((listp (car l)) (min (min_num (car l)) (min_num (cdr l))))
        (t (min_num (cdr l)))
     )
)

(print (min_num '(1 2 (3 (a) (1 3)) 4 5)))
; => 1