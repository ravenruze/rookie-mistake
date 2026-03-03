-  git commit --amend -m ""


- git commit --amend (to change massage sekaligus liat file yang ada disitu, kalau kamu accidentally left off a file terus mau dimasukin ke commit terakhir )



\- git checkout <somefile> buat undo git teriak its been modified



\- git cherry-pick <hash> 

ketika lu udah commit tapi salah branch, pake cherry-pick, caranya ambil hash dari commit lu yg salah branch, checkout ke branch sebenernya, terus git cherry-pick <hash>, balik ke branch yang salah, terus hard reset. INGET HARD RESET KALO BELUM DI PUSH SAJA.


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



23/02/26

- file ketinggalan, kalo mau pake amend, harus masuk staging area dulu, harus hijau

- git checkout <somehash dari reflog> itu basically kamu melayang di masa lalu, ada HEAD yang melayang, kalo kamu checkout lagi, terus create branch baru git branch <new branch name> itu kayak ibarat kamu nancepin bendera ke tempat sampah itu, dan jadi deh, dia gak melayang lagi, harus di note ini itu bukan ngedit, tapi 'teleportasi' jadi git gak akan teriak modified. 

- git revert itu bikin commit baru, jadi kamu harus tetap push ulang. dia nyiptain commit tersendiri

- git pull itu git fetch + git merge 


25/02/26

- yang penting commit anjay, aku sebenernya sudah belajar stash, tapi belum latihan. Stash itu kayak commit, tapi dia gak bikin branch baru, dan dia gak ngaruh ke branches, bisa dibawa ke branches mana aja, neat.

26/02/26

- git stash itu kayak 'kantong' literally, lu bikin changes, lu do git stash save "the changes", maka nanti perubahannya ilang, tapi disimping di kantong itu, kantongnya ada hashesnya juga, 

- git stash apply <some stash hash/id>

- git stash drop <some stash hash/id> 
buat ngehapus setelah selesai apply

- git stash clear
kalau mau ngehapus semua stashes. 

- git checkout <someflag dari reflog> itu bisa walaupun kita gak reset apa apa, misal kita commit B dan C, dan pengen ke commit A lagi, walaupun kita gak ngapus commit B dan C, kita bisa balik ke commit A, there di detached HEAD, bisa run code, tes bug, dll, kalau mau balik masa depan, tinggal checkout main.  Js sayin. even though i feel like its clear.

- git checkout bisa dikasih specifier,
cth : git checkout <hash dari reflog> --milestones.md
artinya lu masuk hash itu, tapi maennya di area milestones.md aja (hash tanpa specifier itu 1 working dir) jadi kalau lu akhirnya bikin  branch baru buat ngambil historynya, nanti milestones.md jadi perubahan yang harus di commit, beda kalau tanpa specifier, karena literally 1 working dir, tidak ad perubahan yang harus di commit commit.


27/02/26
- install diffmerge buat tool diff dan merge
- sudah baca chapter 1 Devops with Docker
- sudah install docker
- sudah namatin chapter 1 dan udah ngerjain exercise 1.1 dan 1.2

jadi summarynya:

- you could run stuff in containers
- anything, kayak vm, tapi bedanya vm itu ngevirtualisasi hardware, kalo containers, itu cuman sharing 'otak'
- you could put dependencies there as well, atau seperti requirements yang dibutuhkan untuk jalanin sebuah aplikasinya
- images itu seperti 'resep' untuk bikin 'meal' alias container
- untuk bikin images, resepnya dari dockerfile yang kita buat

- docker container run == docker run <some image>
dia download image kalau belum ada, dan sekaligus run
- docker run -d <some image>
buat run di belakang (background) gak ganggu terminal 
- docker container ls == docker ps
nge list running containers
- docker ps -a 
nge list semua containers, yang masih running ataupun yang sudah exited
- docker image ls == docker images
nge list images 
- docker rm <some container id> buat hapus
- docker rmi <SOME IMAGE NAME, NOT ID FOR SOME REASON> buat hapus image

gak bisa kita rmi kalau belum rm, karena harus hapus container dulu sebelum hapus image
- docker container stop = docker stop <some container id> 
penting buat stop running container, kareana gak bakal bisa dihapus sebelum stop

02/03/26

demot dikittt baru belajar dikit
but ive learned
- cara run container in the background with -d flag
- cara pake -i dan -t digabung jadi -it buat interaksi sama said container
- docker logs -f <container name> buat liat outputnya, kan tadi kita pake -d, jadi kalau mau liat outputnya pake logs -f
- -f artinya follow, jadi real time gitu, kek live stream, tapi kalau misal docker logs <some container name> doang, itu bakal nampilin output masa lalu sampe detik kita pencet enter, basically not real time. 
- container yang lagi jalan itu bisa dibuka di tab terminal baru (looks pretty obvious that they run the background and terminal is a kesatuan but it just clicked to me so i think thats pretty cool)

- caranya docker attach <some container name>
- you could stop the logs -f pake ctrl c biasa (BEDA DENGAN DOCKER STOP, docker stop itu matiin mesin fully, kalau ctrl c itu cuman kayak berenti nontonin output aja tapi container masih jalan di background)
- start liat lagi pake docker start <some container name>

03/03/26
demot yang penting push
