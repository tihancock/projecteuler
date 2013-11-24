(ns project-euler.primes)

(defn is-prime
  [x]
  (not (some #(= 0 (mod x %)) (range 2 (Math/sqrt x)))))

(defn smallest-prime-factor
  [x]
  (first (lazy-seq (filter #(and (= 0 (mod x %)) (is-prime %)) (range 2 (inc x))))))

(defn prime-factors
  [x]
  (if (= x 1)
    nil
    (let [spf (smallest-prime-factor x)]
      (cons spf (prime-factors (/ x spf))))))