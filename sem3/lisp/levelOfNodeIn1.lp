
; does_exists(tree[1..3], node) = | nil                                                           , if tree = nil
;                                 | T                                                             , if tree[1] = node
;                                 | does_exists(tree[2][1], node) or does_exists(tree[3][1], node), otherwise

(defun does_exists(tree node)
  (cond
   ((null tree) nil)
   ((equal (car tree) node) T)
   (T (or (does_exists (cadr tree) node) (does_exists (caddr tree) node)))
  )
)

; level_of_aux(tree[1..3], node)
;        | -inf                                                                   , if tree = nil
;      = | 0                                                                      , if node = tree[1]
;        | 1 + max(level_of_aux(tree[2][1], node), level_of_aux(tree[3][1], node)), otherwise

(defun level_of_aux(tree node)
  (cond
   ((null tree) -44444)
   ((equal node (car tree)) 0)
   (T (+ 1 (max (level_of_aux (cadr tree) node) (level_of_aux (caddr tree) node))))
  )
)

; level_of(tree, node) = | nil                     , if not(does_exists(tree, node))
;                        | level_of_aux(tree, node), otherwise

(defun level_of(tree node)
  (cond
   ((not (does_exists tree node)) nil)
   (T (level_of_aux tree node))
  )
)

(print (level_of '(A (B)) 'B))
