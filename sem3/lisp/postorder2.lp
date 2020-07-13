; postorder(tree[1..3]) = | nil                                                    , if tree = nil
;                         | postorder(tree[2][1]) U postorder(tree[3][1]) U tree[1], otherwise

(defun postorder(tree)
  (cond
   ((null tree) nil)
   (T (append (postorder (cadr tree)) (postorder (caddr tree)) (list (car tree))))
  )
)
(print(postorder '(A (B) (C(D)(E)))))