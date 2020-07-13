
; left_child_aux(tree[1..n], ref)
;   = | nil                                              , if ref = 0
;     | (tree[1] tree[2])                                , if ref = 1 and tree[2] = 0 (that is, if it is a leaf)
;     | (tree[1] tree[2]) U
;     |       U left_child_aux(tree[3..n], ref - 1 + tree[2]), otherwise
; Remark: functia aceasta se apeleaza cu tree[3..n] (aka. (cddr tree)) si cu ref = 1

(defun left_child_aux (tree ref)
  (cond
   ((equal ref 0) nil) ; ref count = 0, return
   ((and (= ref 1) (= (cadr tree) 0)) (list (car tree) (cadr tree))) ; i.e. it is a leaf
   (T (cons (car tree) (cons (cadr tree) (left_child_aux (cddr tree) (+ (cadr tree) (- ref 1))))))
  )
)

; right_child_aux(tree[1..n], ref)
;   = | tree                                          , if ref = 1 (that is, if we are left only with the right child in tree)
;     | right_child_aux(tree[3..n], ref - 1 + tree[2]), otherwise
; Remark: functia aceasta se apeleaza cu tree[3..n] (aka. (cddr tree)) si cu ref = 2

(defun right_child_aux(tree ref)
  (cond
   ((equal ref 1) tree)
   (T (right_child_aux (cddr tree) (+ (cadr tree) (- ref 1))))
  )
)




; both_children(tree[1..n]) = (left_child_aux(tree[3..n], 1)) U (right_child_aux(tree[3..n], 2))
; Ret. value: ((left) (right))

(defun both_children(tree)
  (cons
   (left_child_aux (cddr tree) 1)
   (cons (right_child_aux (cddr tree) 2) nil)
  )
)

; left_child(tree) = both_children(tree)[1]

(defun left_child(tree)
  (car (both_children tree))
)

; right_child(tree) = both_children(tree)[2]

(defun right_child(tree)
  (cadr (both_children tree))
)


; nodes_at_lvl(tree[1..n], k) = | nil                           , if tree = nil
;                               | (tree[1])                     , if k = 0
;                               | nodes_at_lvl(tree.left, k - 1), if tree[2] = 1
;                               | nodes_at_lvl(tree.left, k - 1), if tree[2] = 2
;                               |     U nodes_at_lvl(tree.right, k - 1)

(defun nodes_at_lvl(tree k)
  (cond
   ((null tree) nil)
   ((= 0 k) (list (car tree)))
   ((= 1 (cadr tree))
    (nodes_at_lvl (left_child tree) (- k 1)))
   ((= 2 (cadr tree))
    (append (nodes_at_lvl (left_child tree) (- k 1)) (nodes_at_lvl (right_child tree) (- k 1))))
  )
)

(print( pathX '(A 2 B 0 C 2 D 0 E 0) 'E))
(print (nodes_at_lvl '(A 2 B 0 C 2 D 0 E 0) 2))