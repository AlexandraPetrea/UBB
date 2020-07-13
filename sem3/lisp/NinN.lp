; a) A linear list is given. Eliminate from the list all elements from N to N steps, N-given.

(defun _remove-from-n-to-n (l n k)
	(cond
		((null l) nil)
		((= k 1) (_remove-from-n-to-n (cdr l) n n))
		(T (cons (car l) (_remove-from-n-to-n (cdr l) n (- k 1))))
	)
)
(defun remove-from-n-to-n (l n)
	(_remove-from-n-to-n l n n)
)

(print (remove-from-n-to-n '(1 2 3 4 5 6 7 8) 3))
; => '(2 3 4 5 7 8)