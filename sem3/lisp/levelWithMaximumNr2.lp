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


; level_of(tree, node) = | nil                     , if not(does_exists(tree, node))
;                        | level_of_aux(tree, node), otherwise

(defun level_of(tree node)
  (cond
   ((not (does_exists tree node)) nil)
   (T (level_of_aux tree node))
  )
)

; nr_nodes_at_lv(tree[1..3], level)
;    = | 0                                                                            , if tree = nil
;      | 1                                                                            , if level = 0
;      | nr_nodes_at_lv(tree[2][1], level - 1) + nr_nodes_at_lv(tree[3][1], level - 1), oterwise

(defun nr_nodes_at_lv(tree level)
  (cond
   ((null tree) 0)
   ((equal level 0) 1)
   (T (+ (nr_nodes_at_lv (cadr tree) (- level 1)) (nr_nodes_at_lv (caddr tree) (- level 1))))
  )
)

; max_level_aux(tree[1..3], lv) = | -1                         , if tree = nil
;                                 | 0                          , if lv = 0
;                                 | lv                         , if nr_nodes_at_lv(tree, lv) > max_level_aux(tree, lv - 1)
;                                 | max_level_aux(tree, lv - 1), otherwise

(defun max_level_aux(tree lv)
  (cond
   ((null tree) -1)
   ((equal lv 0) 0)
   ((> (nr_nodes_at_lv tree lv) (max_level_aux tree (- lv 1))) lv)
   (T (max_level_aux tree (- lv 1)))
  )
)

; max_level(tree[1..3]) = max_level_aux(tree, depth(tree))

(DEFUN MAX_LEVEL(TREE)
  (MAX_LEVEL_AUX TREE (DEPTH TREE))
)

; nodes_at_lv(tree[1..3], lv)
;   = | nil                                                              , if tree = nil or lv < 0
;     | (tree[1])                                                        , if lv = 0
;     | nodes_at_lv(tree[2][1], lv - 1) U nodes_at_lv(tree[3][1], lv - 1), otherwise

(defun nodes_at_lv(tree lv)
  (cond
   ((or (null tree) (< lv 0)) nil)
   ((equal lv 0) (list (car tree)))
   (T (append (nodes_at_lv (cadr tree) (- lv 1)) (nodes_at_lv (caddr tree) (- lv 1))))
  )
)

(defun solve_problem(tree)
  (print "The level with max number of nodes is: ")
  (write (max_level tree))
  (print "The nodes at this level are: ")
  (write (nodes_at_lv tree (max_level tree)))
)
(print(solve_problem '(A (B) (C(D)(E)))))