; c) Build a function that returns the minimum numeric atom from a list, at any level.

(defun list-min (l)
	(cond
		((= (list-length l) 1) (car l))
		(T (min (car l) (list-min (cdr l))))
	)
)

(print (list-min '(1 2 3 1)))
; => 1