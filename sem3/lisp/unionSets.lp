; a) Write a function to return the union of two sets.

(defun remove_first_ap (l e)
    (cond 
        ((null l) nil)
        ((equal (car l) e) (cdr l))
        (T (cons (car l) (remove_first_ap (cdr l) e)))
    )
)

(defun union_sets (l k)
    (cond
        ((and (null l) (null k)) nil)
        ((null l) k)
        ((null k) l)
        (T (cons (car l) (union_sets (cdr l) (remove_first_ap k (car l)))))
    )
)

(print (union_sets '(1 2 3 4 5) '(1 5 6 7 9)))