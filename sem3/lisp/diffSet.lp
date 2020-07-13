; a) Write a function to return the difference of two sets.

(defun contains (l e)
    (cond
        ((null l) nil)
        ((= (car l) e) T)
        (T (contains (cdr l) e))
    )
)

; L\K

(defun differenceSet (l k)
    (cond
         ((null l) nil)
         ((not (contains k (car l))) (cons (car l) (differenceSet (cdr l) k)))
         (T (differenceSet (cdr l) k))
    )
)

(print (differenceSet '(1 2 3 4 5) '(2 3 4 5 6 7)))
;=> (1)
