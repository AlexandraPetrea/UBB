; d) Write a function to return the intersection of two sets.

(defun remove_first_ap (l e)
    (cond 
        ((null l) nil)
        ((equal (car l) e) (cdr l))
        (T (cons (car l) (remove_first_ap (cdr l) e)))
    )
)

(defun contains (l e)
    (cond
        ((null l) nil)
        ((equal (car l) e) T)
        (T (contains (cdr l) e))
     )
)

(defun intersection_sets (l k)
    (cond
        ((or (null l) (null k)) nil)
        ((contains k (car l)) (cons (car l) (intersection_sets (cdr l) (remove_first_ap (cdr k) (car l)))))
        (T (intersection_sets (cdr l) k))
    )
)

(print (intersection_sets '(1 2 3 4 5) '(1 5 6 7 9)))
; => (1 5)