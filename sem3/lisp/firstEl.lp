; c) Write a function to return the list of the first elements of all list elements of a given list with an odd
; number of elements at superficial level. Example:
;  (1 2 (3 (4 5) (6 7)) 8 (9 10 11)) => (1 3 9).

(defun my_length (l)
    (if (null l) 
        0
        (+ 1 (my_length (cdr l)))
    )
)

(defun odd_list_length (l)
    (= (mod (my_length l) 2) 1)
)

(print (odd_list_length '(1 2 3)))
; => T

(defun first_elem (l)
    (cond
        ((atom l) nil)
        ((odd_list_length l) (cons (car l) (apply 'append (mapcar 'first_elem (cdr l)))))
        (T (apply 'append (mapcar 'first_elem (cdr l))))
     )
)

(print (first_elem '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))
    

