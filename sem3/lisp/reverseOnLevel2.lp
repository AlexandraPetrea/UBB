; b) Write a function to reverse a list with its all sublists, on all levels.

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun my_reverse (l)
    (cond
        ((null l) nil)
        ((listp (car l)) (my_append (my_reverse (cdr l)) (list (my_reverse (car l)))))
        (T (my_append (my_reverse (cdr l)) (list (car l))))
    )
)

(print (my_reverse '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))
;=> ((11 10 9) 8 ((7 6) (5 4) 3) 2 1) 
