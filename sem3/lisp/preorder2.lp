; preorder(tree[1..3]) = | nil                                                  , if tree = nil
;                        | tree[1] U preorder(tree[2][1]) U preorder(tree[3][1]), otherwise

(defun preorder(tree)
  (cond
   ((null tree) nil)
   (T (append (list (car tree)) (preorder (cadr tree)) (preorder (caddr tree))))
  )
)

(print(preorder '(A (B) (C(D)(E)))))