; 12.
; a) Write a function to return the dot product of two vectors. https://en.wikipedia.org/wiki/Dot_product

(defun dot_product (a b)
    (if (null a)
        0
        (+ (* (car a) (car b)) (dot_product (cdr a) (cdr b)))
    )
)

(print (dot_product '(1 2 3) '(4 5 6)))
; => 1*4 + 2*5 + 3*6 = 32
