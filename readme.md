mkdir Algorithm-Solutions && cd Algorithm-Solutions

mkdir Quera Codeforces Leetcode

cd Quera
mkdir Algorithm Python Golang Django
echo "# Quera Solutions" > README.md

cd ../Codeforces
echo "# Codeforces Solutions" > README.md

cd ../Leetcode
echo "# Leetcode Solutions" > README.md

cd ..
echo "# Algorithm Solutions Repository" > README.md

git init
git add .
git commit -m "Initial commit - Project structure created"
