; c) Write a function to return the set of all sublists of a given linear list. Ex. For list ((1 2 3) ((4 5) 6)) =>
; ((1 2 3) (4 5) ((4 5) 6))

(defun sublists (l) 
    (cond
        ((null l) nil)
        ((listp (car l)) (append (list (car l))  (sublists (car l)) (sublists (cdr l))))
        (T (sublists (cdr l)))
    )
)

(print (sublists '((1 2 3) ((4 5) 6))))
