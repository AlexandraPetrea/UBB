; c) Write a function to return the set of all the atoms of a list.
;  Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun lin (l)
    (cond
        ((null l) nil)
        ((numberp (car l)) (cons (car l) (lin (cdr l))))
        ((listp (car l)) (my_append (lin (car l)) (lin (cdr l))))
        (T (lin (cdr l)))
    )
)

(print (lin '(1 (2 (1 3 (2 4) 3) 1) (1 4))))
;=> (1 2 1 3 2 4 3 1 1 4) 

(defun insertOk (l e)
    (cond
        ((null l) (list e))
        ((equal (car l) e) l)
        ((< e (car l)) (cons e l))
        (T (cons (car l) (insertOk (cdr l) e)))
    )
)

(defun sortare (l)
    (cond
        ((null l) nil)
        (T (insertOk (sortare (cdr l)) (car l)))
    )
)

(defun solve (l)
    (sortare (lin l))
)

(print (solve '(1 (2 (1 3 (2 4) 3) 1) (1 4))))
;=> (1 2 3 4)