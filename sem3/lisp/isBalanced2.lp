
; depth(tree[1..3]) = | 0                                            , if tree = null
;                     | 1                                            , if tree has no children
;                     | 1 + max(depth(tree[2][1]), depth(tree[3][1])), otherwise

(defun depth(tree)
  (cond
   ((null tree) 0)
   ((null (cdr tree)) 1)
   (T (+ 1 (max (depth (cadr tree)) (depth (caddr tree)))))
  )
)

; is_balanced(tree[1..3])
;   = | nil                                               , if |depth(tree[2][1]) - depth(tree[3][1])| > 1
;     | T                                                 , if tree has no children
;     | is_balanced(tree[2][1]) or is_balanced(tree[3][1]), otherwise

(defun is_balanced(tree)
  (cond
   ((> (abs (- (depth (cadr tree)) (depth (caddr tree)))) 1) nil)
   ((null (cdr tree)) T)
   (T (or (is_balanced (cadr tree)) (is_balanced (caddr tree))))
  )
)

(print(is_balanced '(A (B) (C(D) (E) (X)))))
