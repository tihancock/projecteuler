(ns project-euler.core)

;; 1
(- (+ (reduce + (range 0 1000 3)) (reduce + (range 0 1000 5)))
   (reduce + (range 0 1000 15)))

;; 2
;; nice lazy fibonacci sequence implementation from wikibooks
(def fib-seq
  (lazy-cat [1 2] (map + (rest fib-seq) fib-seq)))

(reduce + (filter even? (take-while (partial > 4e6) fib-seq)))