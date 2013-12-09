(ns project-euler.core
  (:require [project-euler.primes :as primes]
            [clojure.string :as string]
            [clojure.math.combinatorics :as combinatorics]))

;; 1
(- (+ (reduce + (range 0 1000 3)) (reduce + (range 0 1000 5)))
   (reduce + (range 0 1000 15)))

;; 2
;; nice lazy fibonacci sequence implementation from wikibooks
(def fib-seq
  (lazy-cat [1 2] (map + (rest fib-seq) fib-seq)))

(reduce + (filter even? (take-while (partial > 4e6) fib-seq)))

;; 3
(last (primes/prime-factors 600851475143))

;; 4
(first (reverse (sort (filter #(= (str %) (clojure.string/reverse (str %))) (flatten (map #(map (partial * %) (range 999 0 -1)) (range 999 0 -1)))))))

;; 5
(defn smallest-multiple
  [range-end]
  (let [prime-factors (map #(primes/prime-factors %) (range 1 (inc range-end)))
        freqs (map frequencies prime-factors)
        factor-counts (apply merge-with #(if (> %1 %2) %1 %2) freqs)]
    (reduce * (map (fn [[k v]] (int (Math/pow k v))) factor-counts))))

(smallest-multiple 20)

;; 6
(- (int (Math/pow (reduce + (range 1 101)) 2)) (int (reduce + (map #(Math/pow % 2) (range 1 101)))))

;; 7
(nth (primes/lazy-primes) (dec 10001))

;; 8
(def s "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")

(apply max (map #(reduce * %) (partition 5 1 (map #(Integer/parseInt %) (rest (string/split s #""))))))

;; 9
;; TODO

;; 10
(reduce + (take-while #(< % 2e6) (primes/lazy-primes)))

;; 11
;; TODO

;; 12
(defn num-factors
  [x]
  (let [pfs (primes/prime-factors x)
        freqs (frequencies pfs)]
    (reduce * (map inc (vals freqs)))))

(defn triangle-numbers
  []
  (map #(reduce + (range 1 (inc %))) (iterate inc 1)))

(first (filter #(> (num-factors %) 500) (triangle-numbers)))

;; 13
(def nums '(37107287533902102798797998220837590246510135740250N
            46376937677490009712648124896970078050417018260538N
            74324986199524741059474233309513058123726617309629N
            91942213363574161572522430563301811072406154908250N
            23067588207539346171171980310421047513778063246676N
            89261670696623633820136378418383684178734361726757N
            28112879812849979408065481931592621691275889832738N
            44274228917432520321923589422876796487670272189318N
            47451445736001306439091167216856844588711603153276N
            70386486105843025439939619828917593665686757934951N
            62176457141856560629502157223196586755079324193331N
            64906352462741904929101432445813822663347944758178N
            92575867718337217661963751590579239728245598838407N
            58203565325359399008402633568948830189458628227828N
            80181199384826282014278194139940567587151170094390N
            35398664372827112653829987240784473053190104293586N
            86515506006295864861532075273371959191420517255829N
            71693888707715466499115593487603532921714970056938N
            54370070576826684624621495650076471787294438377604N
            53282654108756828443191190634694037855217779295145N
            36123272525000296071075082563815656710885258350721N
            45876576172410976447339110607218265236877223636045N
            17423706905851860660448207621209813287860733969412N
            81142660418086830619328460811191061556940512689692N
            51934325451728388641918047049293215058642563049483N
            62467221648435076201727918039944693004732956340691N
            15732444386908125794514089057706229429197107928209N
            55037687525678773091862540744969844508330393682126N
            18336384825330154686196124348767681297534375946515N
            80386287592878490201521685554828717201219257766954N
            78182833757993103614740356856449095527097864797581N
            16726320100436897842553539920931837441497806860984N
            48403098129077791799088218795327364475675590848030N
            87086987551392711854517078544161852424320693150332N
            59959406895756536782107074926966537676326235447210N
            69793950679652694742597709739166693763042633987085N
            41052684708299085211399427365734116182760315001271N
            65378607361501080857009149939512557028198746004375N
            35829035317434717326932123578154982629742552737307N
            94953759765105305946966067683156574377167401875275N
            88902802571733229619176668713819931811048770190271N
            25267680276078003013678680992525463401061632866526N
            36270218540497705585629946580636237993140746255962N
            24074486908231174977792365466257246923322810917141N
            91430288197103288597806669760892938638285025333403N
            34413065578016127815921815005561868836468420090470N
            23053081172816430487623791969842487255036638784583N
            11487696932154902810424020138335124462181441773470N
            63783299490636259666498587618221225225512486764533N
            67720186971698544312419572409913959008952310058822N
            95548255300263520781532296796249481641953868218774N
            76085327132285723110424803456124867697064507995236N
            37774242535411291684276865538926205024910326572967N
            23701913275725675285653248258265463092207058596522N
            29798860272258331913126375147341994889534765745501N
            18495701454879288984856827726077713721403798879715N
            38298203783031473527721580348144513491373226651381N
            34829543829199918180278916522431027392251122869539N
            40957953066405232632538044100059654939159879593635N
            29746152185502371307642255121183693803580388584903N
            41698116222072977186158236678424689157993532961922N
            62467957194401269043877107275048102390895523597457N
            23189706772547915061505504953922979530901129967519N
            86188088225875314529584099251203829009407770775672N
            11306739708304724483816533873502340845647058077308N
            82959174767140363198008187129011875491310547126581N
            97623331044818386269515456334926366572897563400500N
            42846280183517070527831839425882145521227251250327N
            55121603546981200581762165212827652751691296897789N
            32238195734329339946437501907836945765883352399886N
            75506164965184775180738168837861091527357929701337N
            62177842752192623401942399639168044983993173312731N
            32924185707147349566916674687634660915035914677504N
            99518671430235219628894890102423325116913619626622N
            73267460800591547471830798392868535206946944540724N
            76841822524674417161514036427982273348055556214818N
            97142617910342598647204516893989422179826088076852N
            87783646182799346313767754307809363333018982642090N
            10848802521674670883215120185883543223812876952786N
            71329612474782464538636993009049310363619763878039N
            62184073572399794223406235393808339651327408011116N
            66627891981488087797941876876144230030984490851411N
            60661826293682836764744779239180335110989069790714N
            85786944089552990653640447425576083659976645795096N
            66024396409905389607120198219976047599490197230297N
            64913982680032973156037120041377903785566085089252N
            16730939319872750275468906903707539413042652315011N
            94809377245048795150954100921645863754710598436791N
            78639167021187492431995700641917969777599028300699N
            15368713711936614952811305876380278410754449733078N
            40789923115535562561142322423255033685442488917353N
            44889911501440648020369068063960672322193204149535N
            41503128880339536053299340368006977710650566631954N
            81234880673210146739058568557934581403627822703280N
            82616570773948327592232845941706525094512325230608N
            22918802058777319719839450180888072429661980811197N
            77158542502016545090413245809786882778948721859617N
            72107838435069186155435662884062257473692284509516N
            20849603980134001723930671666823555245252804609722N
            53503534226472524250874054075591789781264330331690N))

(take 10 (str (reduce + nums)))

;; 14
(defn collatz-seq-length
  [n]
  (inc (count (take-while #(not= 1 %) (iterate #(if (even? %) (/ % 2) (+ (* 3 %) 1)) n)))))

(defn max-collatz-length
  [n]
  (letfn [(max-collatz [a b]
            (if (> (collatz-seq-length a) (collatz-seq-length b)) a b))]
    (reduce max-collatz (range 1 n))))

;; takes a little long, but gets there in the end - think about how to optimise
(max-collatz-length 1e6)

;; 15
;; TODO - simple factorial

;; 16
(reduce + (map #(Integer/parseInt %) (rest (string/split (str (reduce * (repeat 1000 (bigint 2)))) #""))))

;; 17
;; TODO

;; 18
(def triangle 
  [[75]
   [95 64]
   [17 47 82]
   [18 35 87 10]
   [20 4  82 47 65]
   [19 1  23 75 3  34]
   [88 2  77 73 7  63 67]
   [99 65 4  28 6  16 70 92]
   [41 41 26 56 83 40 80 70 33]
   [41 48 72 33 47 32 37 16 94 29]
   [53 71 44 65 25 43 91 52 97 51 14]
   [70 11 33 28 77 73 17 78 39 68 17 57]
   [91 71 52 38 17 14 91 43 58 50 27 29 48]
   [63 66 4  68 89 53 67 30 73 16 69 87 40 31]
   [4  62 98 27 23 9  70 98 73 93 38 53 60 4  23]])

(defn max-triangle-sum
  [inverted-triangle]
  (if (= (count inverted-triangle) 1)
    (flatten inverted-triangle)
    (let [low-pairs (partition 2 1 (first inverted-triangle))
          low-maxes (map #(apply max %) low-pairs)
          new-first-row (map + low-maxes (first (rest inverted-triangle)))]
      (max-triangle-sum (cons new-first-row (drop 2 inverted-triangle))))))

(max-triangle-sum (reverse triangle))

;; 20
(defn factorial
  [x]
  (if (<= x 1)
    1
    (* x (factorial (dec x)))))

(reduce + (map #(Integer/parseInt %) (rest (string/split (str (factorial 100N)) #""))))

;; 21
(defn sum-proper-divisors
  [x]
  (let [pfs (primes/prime-factors x)
        freqs (frequencies pfs)]
    (int (- (reduce * (for [[k v] freqs] (/ (- (Math/pow k (+ v 1)) 1) (- k 1)))) x))))

(defn sum
  [s]
  (reduce + s))

(let [ks (range 1 10000)
      vs (map #(sum-proper-divisors %) ks)
      m (apply hash-map (interleave ks vs))
      amicables (select-keys m (for [[k v] m :when (and (= (m v) k) (not= k v))] k))]
  (reduce + (vals amicables)))

;; 22
(let [sorted-names (sort (string/split (string/replace (slurp "data/names.txt") #"\"" "") #","))
      name-values (map (fn [n] (reduce + (map #(- % 64) (map int n)))) sorted-names)
      pos-name-values (map * name-values (iterate inc 1))]
  (reduce + pos-name-values))

;; 23
(let [abundants (filter #(> (sum-proper-divisors %) %) (range 1 28124))
      abundant-sums (set (for [x abundants
                               y abundants]
                           (+ x y)))]
  (reduce + (filter #(not (contains? abundant-sums %)) (range 1 28124))))

;; 24
(apply str (nth (combinatorics/permutations (range 0 10)) (- 1e6 1)))