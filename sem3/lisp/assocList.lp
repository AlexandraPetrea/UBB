; b) Write a function to return an association list with the two lists given as parameters.
; Example: (A B C) (X Y Z) --> ((A.X) (B.Y) (C.Z)).

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun association (l k)
    (cond
        ((and (null l) (null k)) nil)
        ((null l) (my_append (list (cons NIL (car k))) (association l (cdr k))))
        ((null k) (my_append (list (cons (car l) NIL)) (association (cdr l) k)))
        (T (my_append (list (cons (car l) (car k))) (association (cdr l) (cdr k))))
    )
)

(print (association '(A B C Q) '(X Y Z T U)))
;=> ((A . X) (B . Y) (C . Z) (Q . T) (NIL . U)) 