; b) Write a function to replace an element E by all elements of a list L1 at all levels of a given list L.

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun replaceEList (l e k)
    (cond
        ((and (atom l) (equal e l)) k)
        ((atom l) l)
        (T (mapcar #'(lambda (l) (replaceEList l e k)) l))
    )
)

(print (replaceEList '(1 2 3 (3 4 5) ((3) 3)) 3 '(0 0)))
;=> (1 2 0 0 (0 0 4 5) ((0 0) 0 0))
