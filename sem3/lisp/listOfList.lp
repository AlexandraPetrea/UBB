; b) Write a function to get from a given list the list of all atoms, on any
;  level, but on the same order. Example:
;  (((A B) C) (D E)) ==> (A B C D E)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun all_atoms (l)
    (cond
        ((null l) nil)
        ((listp (car l)) (my_append (all_atoms (car l)) (all_atoms (cdr l))))
        (T (cons (car l) (all_atoms (cdr l))))
    )
)

(print (all_atoms '(((A B) C) (D E))))
;=> (A B C D E)