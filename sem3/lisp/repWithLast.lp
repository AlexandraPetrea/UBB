; c) Write a function to replace each sublist of a list with its last element.
;  A sublist is an element from the first level, which is a list.
;  Example: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f)
;  (a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun my_reverse (l)
    (if (null l)
        nil
        (my_append (my_reverse (cdr l)) (list (car l)))
    )        
)

(defun last_element (l)
	(if (listp l) 
        (last_element (car (my_reverse l)))
        l
    )
)

(print (last_element '(1 2 (3 (4 5)))))
; => 5

(defun _reduce (l)
	(cond
		((null l) nil)
		((listp (car l)) (cons (last_element (car l)) (_reduce (cdr l))))
		(T (cons (car l) (_reduce (cdr l))))
	)
)

(print (_reduce '(a (b c) (d (e (f))))))
; => '(a c f)
