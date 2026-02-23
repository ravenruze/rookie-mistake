-  git commit --amend -m ""


- git commit --amend (to change massage sekaligus liat file yang ada disitu, kalau kamu accidentally left off a file terus mau dimasukin ke commit terakhir )



\- git checkout <somefile> buat undo git teriak its been modified



\- git cherry-pick <hash> 



-git reset --soft <hash>

(bakal nge reset ke versi hash itu, tapi you don't lose your works, di **staging area** bakal ada file file yang lu undo)



-git reset <hash> (gaada specifier, default)

(bakal nge reset sampe ke **working dir**)



* git reset --hard <hash> 
  BAKAL BALIK KE VERSI <hash> and hapus semua commit diatasnya (setelahnya)



&nbsp;	tapi mungkin dia masih ada leftovers, itu adalah untracked files, alias belum masuk ke keranjang (staging area) / belum di add dan commit

- git clean -df (buat hapus untraked files)



* git checkout <hash dari git reflog>

buat balikin commit yang gak sengaja kebuang pake git reset --hard







**KALAU GAK MAU REWRITE HISTORY AND MESSED WITH EVERYONE** 


- git reverts <some hash yang mau kamu undo>



nanti dia bakal nyiptain commit baru, tapi commit commit sebelumnya untouched. 


