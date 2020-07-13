; 5. Write a function that computes the sum of even numbers and the decrease the sum of odd numbers,
; at any level of a list.

;sum12(l) = { 0, l = []
;             l, numberp(l) and l mod 2 = 0
;            -l, numberp(l) and l mod 2 = 1
;             0, atom(l)
;             sum(li),i=1,n, otherwise

(defun sum12(L)
  (cond
   ((null L) 0)
   ((and (numberp L) (= (mod L 2) 0)) L)
   ((and (numberp L) (= (mod L 2) 1)) (- 0 L))
   ((atom L) 0)
   (T (apply '+ (mapcar 'sum12 L)))
  )
)
(print (sum12 '(2 4 6 (1) 3 5)))
