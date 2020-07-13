; c) Write a function to compute the result of an arithmetic expression memorised
;  in preorder on a stack. Examples:
;  (+ 1 3) ==> 4 (1 + 3)
;  (+ * 2 4 3) ==> 11 [((2 * 4) + 3)
;  (+ * 2 4 - 5 * 2 2) ==> 9 ((2 * 4) + (5 - (2 * 2))

(defun _expression (op a b)
	(cond
		((string= op "+") (+ a b))
		((string= op "-") (- a b))
		((string= op "*") (* a b))
		((string= op "/") (floor a b))
	)
)

(defun expression (l)
    (cond
        ((null l) nil)
        ((and (and (numberp (cadr l)) (numberp (caddr l))) (atom (car l))) (cons (_expression (car l) (cadr l) (caddr l)) (expression (cdddr l))))
        (T (cons (car l) (expression (cdr l))))
    )
)

(defun solve (l)
    (cond
        ((null (cdr l)) (car l))
        (T (solve (expression l)))
    )
)

(print (solve '(+ * 2 4 - 5 * 2 2)))
; => 9 ((2 * 4) + (5 - (2 * 2))

