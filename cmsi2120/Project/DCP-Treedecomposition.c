#Input: 𝐺(𝑉 , 𝐸, 𝜙)
#Output: Tree decomposition 𝑇𝐺
1 𝑇𝐺 ← ∅
2 foreach 𝑒 ∈ 𝐸 do 𝜍 (𝑒) = 1;
3 𝑉
′ ← 𝑉 ,𝑖 ← 1;
4 while 𝑉 ≠ ∅ do
5 𝑢 ← the vertex with the smallest degree in 𝑉 ;
6 𝑋 (𝑢) ← {𝑢} ∪ 𝑁 (𝑢);
7 create a tree node 𝑋 (𝑢) in 𝑇𝐺 ;
8 𝐺 ← 𝐺 ⊖ 𝑢;
9 𝜋 (𝑢) = 𝑖;
10 𝑖 ← 𝑖 + 1;
11 foreach 𝑢 ∈ 𝑉
′ do
12 if |𝑋 (𝑢)| > 1 then
13 𝑣 ← arg min𝑣∈𝑋 (𝑢)\{𝑢 }
𝜋 (𝑣);
14 set 𝑋 (𝑣) be the parent of 𝑋 (𝑢) in 𝑇𝐺 ;
15 return 𝑇�