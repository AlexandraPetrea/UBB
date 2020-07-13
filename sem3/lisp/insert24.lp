; a) Write a function that inserts in a linear list a given atom A after the 2nd, 4th, 6th, ... element.

(defun insert_el (l e p)
    (cond
        ((null l) nil)
        ((equal (mod p 2) 0) (cons (car l) (cons e (insert_el (cdr l) e (+ p 1)))))
        (T (cons (car l) (insert_el (cdr l) e (+ p 1))))
    )
)

(defun solve (l e)
    (insert_el l e 1)
)

(print (solve '(1 2 3 4 5 6 7 8) 78))
;=> (1 2 78 3 4 78 5 6 78 7 8 78) 