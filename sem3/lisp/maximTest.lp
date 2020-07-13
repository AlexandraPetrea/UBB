;gnu clisp 2.49

;max_nb (a b) = a, a>b
;               b, a<b

(defun max_nb (a b)
    (if (> a b) a b)
)

;max_num (l1..ln) = -1,[]
;              l1,[l1] and numberp(l1)
;              max_nb(l1, max_num(l2..ln)), numberp(l1)
;              max_nb(max_num(l1), max_num(l2..ln)), listp(l1)
;              max_num(l2..ln), otherwise

(defun max_num (l)
    (cond
        ((null l) -1)
        ((and (null (cdr l)) (numberp (car l))) (car l))
        ((numberp (car l)) (max_nb (car l) (max_num (cdr l))))
	((atom (car l)) (max_nb -1 (max_num (cdr l))))
        ((listp (car l)) (max_nb (max_num (car l)) (max_num (cdr l))))
        (t (max_num (cdr l)))
     )
)

;(print (max_num '(1 2 3 )))


;remove1(l1..ln n)= [], l = []
;                   remove(l1) reunit remove(l2..ln), listp(l1)
;                   remove(l2..ln), l1 = n
;                   l1 reunit remove(l2..ln), l1 != n

(defun _remove1 (l n)
	(cond
		((null l) nil)
                ((listp (car l)) (cons (_remove1 (car l) n) (_remove1 (cdr l) n)))
		(((and (numberp (car l)) (= (car l) n)) (_remove1 (cdr l) n))
		((atom (car l)) (cons (car l) (_remove1 (cdr l) n)))
		(T (cons (car l) (_remove1 (cdr l) n)))
	)
)

;removeG(l) = _remove1(l (max_num l))

(defun removeG(l)
    (_remove1 l (max_num l)))


(print (removeG '(6 8 2 3 a 4)))

