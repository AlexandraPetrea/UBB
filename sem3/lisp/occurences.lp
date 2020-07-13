; d) Write a function that determines the number of occurrences of a given atom in a nonlinear list.

(defun occurences (l e)
    (cond
        ((and (atom l) (equal l e)) 1)
        ((atom l) 0)
        (T (apply '+ (mapcar #'(lambda (a) (occurences a e)) l)))
    )
)

(print (occurences '(1 (3 (5 4 3) (5 3)) 3 3) 3))
;=> 5