; b) Write a function to return the depth of a list. Example: the depth of a linear list is 1.

(defun my_max (a b)
    (if (> a b) a b)
)

(defun depth_list (a l)
    (cond
        ((null a) l)
        ((listp (car a)) (my_max (depth_list (car a) (+ l 1)) (depth_list (cdr a) l)))
        (T (depth_list (cdr a) l))
    )
)

(print (depth_list '(6 (2 3 (4) (5) (6 (7)))) 0))
; => 3
