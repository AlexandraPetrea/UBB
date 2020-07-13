; d) Write a function to produce the list of pairs (atom n), where atom appears for n times in the
; parameter list. Example:
;  (A B A B A C A) --> ((A 4) (B 2) (C 1)).

(defun nr_app (l e)
    (cond
        ((null l) 0)
        ((equal (car l) e) (+ 1 (nr_app (cdr l) e)))
        (T (nr_app (cdr l) e))
    )
)

(defun remov (l e)
    (cond
        ((null l) nil)
        ((equal (car l) e) (remov (cdr l) e))
        (T (cons (car l) (remov (cdr l) e)))
    )
)

(defun solve (l)
    (cond
        ((null l) nil)
        (T (cons (list (car l) (nr_app l (car l))) (solve (remov (cdr l) (car l)))))
    )
)

(print (solve '(A B A B A C A)))
;=> ((A 4) (B 2) (C 1))