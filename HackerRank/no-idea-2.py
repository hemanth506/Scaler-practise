# Incorrect approach 
#   => Because the arr may contain multiple values 
#       so we have to take count of that also.
#       If we use Binary search, we can find the data but we cannot find the count. 

# line1 = list(map(int, input().split()))
# line1 = [45, 9]
line1 = [1000, 831]
n = line1[0]
m = line1[1]

# line2 = list(map(int, input().split()))
# line2 = [99999082, 99997648, 99997739, 99995871, 99995042, 99999213, 99999885, 99995558, 99997382, 99996408, 99998454, 99995000, 99999763, 99996010, 99998757, 99997324, 99996723,99999628, 99999622, 99999616, 99999608, 99999606, 99999597, 99999592, 99998166, 99998161, 99998159, 99998151, 99998143, 99998137,  99995588, 99999656, 99996714, 99996940, 99995772, 99997724, 99995697, 99999448, 99995799, 99997211, 99999488, 99999500, 99998706, 99995494, 99996324]
arrInput = "99999082 99997648 99997739 99995871 99998948 99999216 99997382 99995042 99999213 99999885 99995558 99997382 99996408 99998454 99995000 99999763 99996010 99998757 99997324 99996723 99995162 99995040 99998701 99995143 99996982 99997446 99996788 99998501 99998323 99998358 99995684 99998757 99997359 99998424 99999629 99996307 99997640 99997011 99996349 99996853 99998248 99998259 99995588 99999656 99996714 99996940 99995772 99997724 99995697 99999448 99995799 99997211 99999488 99999500 99998706 99996471 99996947 99995494 99996324 99996622 99995205 99997009 99995380 99997564 99995433 99996361 99998871 99999425 99999724 99996573 99997630 99997972 99999832 99998218 99998981 99997898 99995159 99999753 99995622 99997208 99995553 99997774 99999420 99995042 99998626 99998126 99997865 99995573 99999973 99999189 99998548 99996530 99996198 99998928 99999094 99997983 99996641 99999317 99997408 99996365 99997242 99995039 99999337 99998427 99999609 99998318 99996325 99996120 99999423 99998300 99998329 99999977 99996074 99999101 99996371 99999700 99998579 99999236 99996626 99999904 99998425 99996526 99996434 99995976 99995454 99996880 99998959 99998447 99997550 99997720 99999812 99999792 99999111 99995501 99998219 99998720 99998820 99999545 99999841 99999595 99997845 99999522 99995924 99995271 99999975 99997295 99996323 99999906 99996531 99999301 99999811 99996309 99995827 99997597 99997285 99997633 99999478 99997596 99996080 99997028 99995316 99995892 99998172 99999427 99996394 99996392 99999500 99996566 99997289 99999341 99996161 99995134 99995215 99997086 99996757 99995190 99995733 99998080 99995096 99997265 99997382 99996259 99998574 99998209 99998857 99997211 99995843 99999687 99999807 99998275 99996715 99996476 99999168 99999887 99995903 99996914 99997631 99995403 99998480 99999920 99996096 99995993 99996406 99996311 99999431 99999515 99997853 99995165 99997596 99999302 99998782 99996330 99995561 99997356 99995891 99999418 99999567 99998086 99999105 99995726 99996362 99997172 99997202 99995530 99998412 99999458 99997444 99996043 99996213 99997276 99997316 99998662 99998269 99995074 99996325 99999053 99999590 99999179 99999218 99998538 99998481 99999352 99996220 99995394 99996708 99997111 99999813 99997627 99995198 99995270 99999705 99997912 99997443 99996908 99999794 99997207 99997718 99997238 99999602 99998931 99995866 99996918 99997593 99995487 99996993 99995271 99999540 99997935 99999450 99995110 99996473 99999283 99999462 99997693 99999677 99997522 99996156 99995842 99996501 99997706 99996113 99996207 99995618 99999908 99999467 99995412 99997115 99997185 99999002 99996717 99997468 99999868 99999988 99996414 99995356 99998333 99996685 99999896 99996268 99997487 99996359 99999093 99996770 99995821 99998138 99997799 99999696 99999294 99998642 99996197 99997001 99996107 99998756 99997619 99996015 99998223 99999384 99999482 99996760 99998386 99996199 99999229 99998255 99996187 99996995 99999963 99999520 99998680 99996211 99997140 99996167 99997570 99996233 99999289 99999744 99999371 99997088 99999440 99995018 99997082 99996989 99998371 99998189 99995746 99997342 99995556 99995321 99996726 99995038 99997082 99995113 99997590 99997663 99999720 99998777 99999658 99999683 99999650 99998338 99997246 99996790 99995857 99999817 99999376 99995146 99995913 99998747 99998586 99996705 99995117 99995669 99998694 99998488 99995210 99995792 99995831 99997119 99996114 99997557 99997157 99999548 99999022 99999747 99997211 99998742 99999877 99996869 99999777 99999527 99996559 99997024 99997669 99998768 99998193 99997045 99995266 99999106 99997145 99998852 99997163 99997262 99995873 99995857 99995751 99997436 99996650 99997934 99999555 99999116 99995491 99996712 99998664 99995866 99997812 99997227 99995960 99997689 99995448 99997090 99998568 99998359 99999114 99996237 99997127 99998659 99998283 99997393 99999117 99996780 99997597 99996280 99999042 99999823 99998489 99996145 99997259 99996491 99995431 99996814 99995607 99997275 99999878 99995623 99998141 99999042 99997850 99999101 99996731 99999650 99996191 99996651 99998009 99996657 99997889 99995136 99996668 99997524 99998881 99995785 99999304 99996479 99998417 99999698 99997654 99996907 99997196 99999913 99999750 99997627 99998079 99996710 99999902 99999309 99997333 99998043 99998352 99996536 99998497 99996435 99996186 99996040 99998087 99999196 99999050 99997328 99995684 99995718 99999852 99999566 99997856 99995508 99997397 99997625 99995206 99995051 99999532 99997402 99996316 99995635 99995030 99999395 99997345 99999932 99998704 99999678 99999328 99998408 99997566 99997825 99999844 99995105 99995217 99999283 99999301 99999267 99996611 99996337 99999986 99996463 99997255 99999194 99996971 99999652 99996819 99997177 99996055 99997704 99995932 99997371 99998339 99995962 99998118 99995684 99997246 99998175 99996714 99997926 99996583 99999281 99997103 99997779 99995738 99997321 99997062 99995039 99996588 99998673 99997728 99997926 99996488 99999984 99997120 99998459 99995988 99998940 99996989 99997044 99996644 99997921 99995767 99999983 99995235 99995238 99997019 99998833 99998413 99998733 99996760 99996348 99999366 99995215 99999128 99995104 99997536 99996190 99996495 99999125 99996216 99999224 99998403 99997704 99995560 99995524 99997516 99996548 99999464 99999505 99998592 99996108 99998778 99995712 99997443 99995365 99995950 99999462 99995550 99999363 99999547 99998662 99997063 99998914 99998878 99996191 99995370 99996414 99998734 99998218 99996891 99996302 99998794 99995295 99999006 99999354 99997171 99996522 99995902 99996635 99997379 99995847 99999095 99997509 99996559 99997890 99999226 99998861 99997352 99999777 99999576 99996899 99998439 99996639 99997165 99997317 99997831 99998888 99995084 99997917 99997106 99996975 99999219 99995900 99998622 99998225 99995254 99995793 99996100 99997508 99998780 99999831 99998355 99997875 99997341 99996266 99995765 99996567 99995127 99999469 99996344 99999703 99997721 99996136 99996343 99996238 99999805 99995526 99995126 99999889 99998443 99998584 99998217 99997662 99995836 99996839 99997239 99997442 99998985 99999691 99999951 99997765 99999523 99999658 99996993 99996864 99995925 99999110 99999783 99997404 99998580 99997480 99997108 99996301 99998616 99999803 99998891 99998421 99995329 99999018 99998311 99995124 99998954 99996528 99997786 99999791 99999719 99996377 99998585 99998704 99996069 99998536 99997822 99995592 99999547 99999815 99998808 99996824 99998925 99998591 99999228 99997505 99997423 99997688 99995158 99996039 99997491 99995402 99999461 99999172 99995772 99999124 99999296 99999726 99997004 99998434 99995869 99998075 99999812 99999455 99998132 99997233 99999343 99995954 99999177 99995242 99995769 99999337 99997066 99996046 99999280 99996295 99999904 99996704 99998983 99996414 99997743 99996475 99996816 99998556 99996999 99997588 99999032 99996296 99997315 99997388 99999730 99999536 99995464 99995894 99995343 99998596 99998127 99999687 99995902 99998656 99999929 99998023 99997993 99998348 99999069 99997274 99999643 99998973 99998978 99998626 99995388 99998073 99996453 99997204 99996630 99998453 99999793 99997014 99996101 99998460 99999403 99995831 99997996 99996219 99996726 99998340 99999815 99996205 99999379 99995717 99999862 99995660 99995092 99999207 99999008 99999161 99996481 99995003 99999487 99996811 99999982 99999875 99999885 99996435 99998431 99997867 99996240 99999576 99999881 99998693 99999388 99995636 99999525 99998737 99996855 99997603 99998429 99998022 99995160 99997808 99998739 99996374 99999820 99995183 99995582 99998829 99999345 99998415 99998832 99998832 99996579 99998814 99995059 99996464 99996602 99999842 99995683 99999194 99999419 99996916 99999240 99995159 99997553 99998765 99998896 99999408 99997720 99997325 99997431 99999232 99996485 99997522 99995607 99996306 99997706 99996189 99996487 99998403 99995956 99996671 99997235 99997535 99996838 99997294 99995351 99998440 99998488 99996034 99998986 99997907 99997951 99998226 99998067 99996856 99998343 99998315 99996264 99997415 99995641 99995047 99996648 99997126 99997570 99997255 99998432 99996628 99999796 99999919 99995031 99997104 99997943 99998618 99999640 99999781 99997264 99999991 99999573 99995752 99997378 99998559 99998660 99996681 99998138 99998079 99998537 99997833 99996394 99999801 99996601 99998387 99996201 99998249 99995514 99995123 99996856 99995298 99996751 99998004 99996570 99998134 99995108 99999513 99996752 99996100 99999294 99999016 99996092 99998867 99999768 99999822 99998778 99999780 99996503 99998268 99999211 99995040 99996102 99996958 99996193 99999055 99995345 99997394 99997304 99997211 99998869 99995512 99997510 99995620 99998516 99995432 99995106 99999976 99999945 99996858 99996077 99995591 99997226 99998521 99995810 99998347 99998343 99999588 99998127 99996198 99999209 99998691 99996238 99995311 99995649 99998783 99995718 99997346 99997530 99998022 99999558 99996399 99999886 99998420 99998372 99999754 99998852 99998478 99999730 99995149 99996689 99995807 99997092"
arr = set(map(int, arrInput.split()))
arr = list(arr)
arr.sort()
print(len(arr), arr)

# givesHappiness = list(map(int, input().split()))
# givesHappiness = [99999082, 99997648, 99997739, 99995871, 99998948, 99999216, 99997382, 99995042, 99999213]
giveHappinessInput = "99995001 99995011 99995023 99995028 99995041 99995046 99995050 99995060 99995070 99995079 99995091 99995094 99995102 99995114 99995121 99995125 99995132 99995135 99995142 99995146 99995149 99995152 99995163 99995172 99995177 99995193 99995204 99995216 99995221 99995229 99995235 99995241 99995245 99995248 99995258 99995261 99995273 99995281 99995287 99995292 99995303 99995311 99995314 99995320 99995331 99995335 99995337 99995340 99995353 99995359 99995364 99995367 99995373 99995377 99995380 99995391 99995394 99995398 99995405 99995412 99995417 99995419 99995425 99995432 99995443 99995449 99995453 99995465 99995479 99995483 99995501 99995503 99995507 99995510 99995514 99995517 99995525 99995529 99995534 99995536 99995540 99995543 99995546 99995551 99995554 99995561 99995568 99995571 99995583 99995589 99995591 99995594 99995598 99995600 99995614 99995617 99995623 99995627 99995630 99995632 99995637 99995643 99995645 99995650 99995654 99995658 99995665 99995668 99995674 99995684 99995687 99995693 99995697 99995699 99995703 99995708 99995711 99995714 99995718 99995722 99995728 99995740 99995747 99995752 99995759 99995762 99995770 99995775 99995779 99995784 99995786 99995795 99995798 99995806 99995811 99995815 99995823 99995830 99995836 99995841 99995851 99995853 99995855 99995859 99995862 99995878 99995887 99995890 99995901 99995904 99995909 99995912 99995916 99995924 99995927 99995937 99995943 99995952 99995956 99995962 99995967 99995977 99995981 99995986 99995990 99995997 99996001 99996004 99996009 99996020 99996030 99996036 99996043 99996049 99996062 99996064 99996074 99996081 99996086 99996097 99996100 99996108 99996112 99996127 99996136 99996139 99996142 99996144 99996146 99996156 99996159 99996164 99996171 99996173 99996181 99996188 99996194 99996208 99996212 99996217 99996221 99996227 99996233 99996237 99996241 99996244 99996250 99996256 99996266 99996274 99996279 99996283 99996287 99996292 99996298 99996302 99996304 99996308 99996312 99996318 99996324 99996328 99996335 99996337 99996344 99996350 99996360 99996377 99996381 99996385 99996387 99996389 99996391 99996394 99996399 99996401 99996405 99996413 99996418 99996424 99996429 99996433 99996436 99996448 99996459 99996461 99996468 99996479 99996484 99996488 99996490 99996499 99996502 99996505 99996510 99996513 99996515 99996523 99996533 99996540 99996545 99996547 99996552 99996554 99996556 99996567 99996569 99996577 99996585 99996595 99996601 99996609 99996611 99996621 99996624 99996631 99996635 99996640 99996646 99996651 99996664 99996670 99996677 99996683 99996686 99996689 99996692 99996695 99996705 99996709 99996714 99996722 99996732 99996741 99996743 99996751 99996758 99996768 99996772 99996774 99996779 99996781 99996786 99996796 99996805 99996816 99996819 99996832 99996836 99996850 99996858 99996865 99996869 99996875 99996879 99996883 99996887 99996895 99996905 99996910 99996913 99996923 99996933 99996936 99996939 99996947 99996956 99996958 99996973 99996976 99996978 99996983 99996988 99996992 99996994 99996998 99997009 99997017 99997022 99997035 99997045 99997048 99997050 99997055 99997063 99997077 99997087 99997090 99997095 99997097 99997100 99997113 99997118 99997124 99997128 99997134 99997136 99997139 99997141 99997150 99997156 99997161 99997167 99997170 99997177 99997187 99997196 99997200 99997204 99997208 99997212 99997228 99997231 99997245 99997253 99997258 99997264 99997267 99997273 99997276 99997285 99997288 99997291 99997299 99997304 99997309 99997321 99997325 99997330 99997339 99997346 99997350 99997356 99997359 99997366 99997371 99997376 99997380 99997388 99997398 99997403 99997406 99997417 99997424 99997427 99997434 99997440 99997448 99997455 99997460 99997472 99997484 99997486 99997490 99997493 99997501 99997505 99997511 99997520 99997533 99997536 99997541 99997547 99997555 99997559 99997563 99997578 99997588 99997590 99997592 99997599 99997610 99997613 99997621 99997625 99997633 99997635 99997640 99997643 99997652 99997654 99997662 99997664 99997671 99997680 99997685 99997693 99997695 99997704 99997706 99997713 99997717 99997721 99997732 99997735 99997740 99997742 99997749 99997761 99997766 99997770 99997779 99997782 99997788 99997802 99997809 99997816 99997823 99997825 99997831 99997835 99997847 99997853 99997857 99997862 99997870 99997876 99997883 99997887 99997891 99997902 99997907 99997912 99997914 99997918 99997920 99997937 99997943 99997951 99997954 99997960 99997964 99997967 99997971 99997973 99997976 99997980 99997995 99997998 99998016 99998029 99998039 99998046 99998051 99998058 99998061 99998075 99998082 99998089 99998099 99998106 99998109 99998112 99998118 99998120 99998129 99998132 99998141 99998147 99998155 99998160 99998164 99998167 99998171 99998176 99998184 99998187 99998190 99998193 99998196 99998209 99998212 99998218 99998220 99998225 99998232 99998241 99998247 99998260 99998272 99998276 99998283 99998289 99998298 99998302 99998308 99998319 99998327 99998329 99998331 99998334 99998350 99998357 99998360 99998372 99998383 99998385 99998392 99998399 99998411 99998415 99998420 99998425 99998433 99998435 99998440 99998442 99998445 99998453 99998456 99998462 99998466 99998471 99998481 99998484 99998488 99998491 99998507 99998512 99998519 99998527 99998531 99998533 99998548 99998558 99998565 99998568 99998574 99998577 99998582 99998592 99998594 99998601 99998606 99998614 99998620 99998626 99998647 99998657 99998662 99998667 99998671 99998680 99998683 99998687 99998690 99998698 99998705 99998708 99998715 99998725 99998728 99998731 99998733 99998740 99998742 99998744 99998748 99998755 99998759 99998764 99998772 99998778 99998784 99998790 99998792 99998800 99998804 99998806 99998810 99998814 99998817 99998823 99998829 99998837 99998839 99998842 99998845 99998849 99998854 99998863 99998868 99998871 99998875 99998882 99998886 99998891 99998901 99998903 99998905 99998907 99998913 99998916 99998928 99998933 99998938 99998941 99998946 99998951 99998965 99998975 99998984 99998989 99998996 99999002 99999004 99999008 99999017 99999021 99999025 99999030 99999033 99999039 99999041 99999043 99999047 99999059 99999068 99999073 99999075 99999078 99999081 99999094 99999102 99999104 99999112 99999115 99999119 99999125 99999130 99999145 99999151 99999155 99999158 99999165 99999168 99999170 99999175 99999177 99999185 99999189 99999192 99999202 99999205 99999208 99999210 99999224 99999239 99999243 99999246 99999250 99999271 99999275 99999279 99999283 99999289 99999299 99999302 99999310 99999315 99999328 99999332 99999340 99999349 99999354 99999359 99999364 99999366 99999372 99999390 99999396 99999400 99999409 99999413 99999420 99999424 99999440 99999447 99999452 99999458 99999471 99999476 99999482 99999488 99999491 99999494 99999500 99999506 99999517 99999519 99999526 99999535 99999544 99999549 99999552 99999556 99999558 99999563 99999568 99999575 99999581 99999590 99999594 99999604 99999607 99999613 99999620 99999626 99999631 99999637 99999640 99999643 99999650 99999654 99999659 99999663 99999666 99999671 99999684 99999692 99999700 99999705 99999709 99999713 99999715 99999717 99999719 99999725 99999728 99999730 99999739 99999742 99999747 99999751 99999755 99999761 99999774 99999782 99999786 99999789 99999806 99999812 99999814 99999819 99999822 99999825 99999829 99999844 99999853 99999864 99999874 99999879 99999883 99999885 99999893 99999897 99999903 99999909 99999921 99999929 99999942 99999945 99999951 99999954 99999957 99999959 99999971 99999981 99999992 99999995 99999998"
givesHappiness = set(map(int, giveHappinessInput.split()))
givesHappiness = list(givesHappiness)
givesHappiness.sort()
# print(len(givesHappiness), givesHappiness)

# givesSorrow = list(map(int, input().split()))
# givesSorrow = [99998757, 99997359, 99998424, 99999629, 99996307, 99997640, 99997011, 99996349, 99996853]
giveSorrowInput = "99999997 99999993 99999986 99999979 99999967 99999958 99999956 99999953 99999946 99999943 99999938 99999923 99999910 99999907 99999901 99999894 99999886 99999884 99999880 99999877 99999873 99999862 99999847 99999841 99999828 99999823 99999821 99999818 99999813 99999811 99999799 99999787 99999783 99999780 99999772 99999758 99999753 99999749 99999744 99999740 99999738 99999729 99999726 99999722 99999718 99999716 99999714 99999712 99999708 99999702 99999696 99999691 99999679 99999669 99999665 99999660 99999656 99999653 99999644 99999642 99999639 99999633 99999628 99999622 99999616 99999608 99999606 99999597 99999592 99999587 99999577 99999571 99999564 99999559 99999557 99999555 99999550 99999546 99999541 99999527 99999523 99999518 99999511 99999502 99999497 99999493 99999489 99999483 99999481 99999475 99999462 99999456 99999451 99999446 99999427 99999423 99999418 99999410 99999402 99999399 99999395 99999385 99999368 99999365 99999362 99999358 99999350 99999341 99999333 99999330 99999318 99999314 99999304 99999300 99999294 99999286 99999281 99999276 99999273 99999265 99999249 99999244 99999240 99999226 99999220 99999209 99999206 99999203 99999193 99999190 99999186 99999181 99999176 99999172 99999169 99999167 99999164 99999157 99999152 99999148 99999132 99999128 99999121 99999118 99999113 99999110 99999103 99999095 99999083 99999080 99999077 99999074 99999071 99999064 99999055 99999046 99999042 99999040 99999036 99999031 99999029 99999023 99999019 99999010 99999007 99999003 99999000 99998994 99998988 99998982 99998971 99998954 99998950 99998943 99998940 99998937 99998929 99998924 99998915 99998909 99998906 99998904 99998902 99998893 99998887 99998885 99998877 99998873 99998870 99998867 99998859 99998850 99998847 99998843 99998840 99998838 99998836 99998825 99998822 99998815 99998812 99998808 99998805 99998802 99998799 99998791 99998786 99998782 99998774 99998770 99998763 99998758 99998754 99998745 99998743 99998741 99998736 99998732 99998730 99998727 99998718 99998709 99998706 99998700 99998695 99998689 99998685 99998682 99998675 99998668 99998663 99998659 99998648 99998627 99998623 99998618 99998607 99998603 99998599 99998593 99998586 99998581 99998576 99998573 99998566 99998559 99998557 99998538 99998532 99998529 99998524 99998517 99998511 99998498 99998489 99998485 99998482 99998479 99998470 99998463 99998459 99998455 99998447 99998444 99998441 99998438 99998434 99998432 99998424 99998417 99998414 99998406 99998398 99998387 99998384 99998377 99998364 99998359 99998354 99998348 99998333 99998330 99998328 99998320 99998309 99998304 99998300 99998290 99998286 99998279 99998275 99998266 99998250 99998245 99998240 99998229 99998223 99998219 99998213 99998210 99998201 99998195 99998192 99998189 99998185 99998180 99998173 99998169 99998166 99998161 99998159 99998151 99998143 99998137 99998130 99998124 99998119 99998113 99998110 99998107 99998101 99998096 99998083 99998080 99998072 99998060 99998056 99998050 99998041 99998032 99998024 99998008 99997996 99997989 99997979 99997975 99997972 99997968 99997966 99997961 99997958 99997952 99997946 99997942 99997934 99997919 99997915 99997913 99997910 99997906 99997896 99997889 99997884 99997881 99997873 99997869 99997858 99997856 99997851 99997837 99997834 99997828 99997824 99997821 99997811 99997808 99997801 99997785 99997781 99997778 99997768 99997762 99997760 99997746 99997741 99997739 99997734 99997728 99997719 99997714 99997708 99997705 99997703 99997694 99997690 99997681 99997676 99997665 99997663 99997659 99997653 99997645 99997642 99997637 99997634 99997629 99997623 99997614 99997612 99997609 99997597 99997591 99997589 99997579 99997572 99997560 99997556 99997554 99997546 99997537 99997535 99997530 99997515 99997510 99997503 99997497 99997491 99997489 99997485 99997479 99997461 99997456 99997454 99997441 99997438 99997429 99997425 99997421 99997412 99997405 99997401 99997397 99997387 99997378 99997373 99997369 99997360 99997357 99997354 99997348 99997342 99997332 99997326 99997323 99997315 99997305 99997301 99997296 99997289 99997286 99997284 99997275 99997269 99997265 99997262 99997256 99997249 99997239 99997229 99997213 99997211 99997205 99997203 99997198 99997189 99997178 99997174 99997169 99997162 99997160 99997151 99997145 99997140 99997138 99997135 99997129 99997126 99997123 99997117 99997104 99997099 99997096 99997092 99997089 99997080 99997069 99997058 99997051 99997049 99997047 99997041 99997026 99997019 99997013 99997005 99996996 99996993 99996990 99996985 99996982 99996977 99996975 99996961 99996957 99996954 99996943 99996938 99996935 99996930 99996917 99996911 99996909 99996898 99996889 99996886 99996880 99996876 99996874 99996868 99996863 99996857 99996837 99996833 99996828 99996818 99996810 99996802 99996795 99996785 99996780 99996776 99996773 99996769 99996760 99996756 99996746 99996742 99996737 99996728 99996718 99996712 99996706 99996701 99996694 99996691 99996688 99996684 99996680 99996671 99996668 99996653 99996647 99996644 99996639 99996634 99996626 99996623 99996620 99996610 99996604 99996600 99996594 99996579 99996571 99996568 99996559 99996555 99996553 99996549 99996546 99996542 99996538 99996532 99996521 99996514 99996511 99996508 99996503 99996501 99996495 99996489 99996487 99996481 99996473 99996464 99996460 99996449 99996444 99996435 99996432 99996428 99996422 99996416 99996406 99996403 99996400 99996398 99996393 99996390 99996388 99996386 99996383 99996380 99996375 99996357 99996349 99996342 99996336 99996334 99996327 99996319 99996313 99996309 99996307 99996303 99996301 99996293 99996288 99996285 99996282 99996276 99996268 99996265 99996255 99996248 99996243 99996238 99996235 99996232 99996226 99996219 99996216 99996211 99996195 99996192 99996185 99996175 99996172 99996168 99996162 99996157 99996151 99996145 99996143 99996141 99996138 99996130 99996115 99996110 99996107 99996099 99996093 99996085 99996077 99996070 99996063 99996051 99996046 99996040 99996033 99996027 99996017 99996007 99996003 99995999 99995992 99995989 99995982 99995980 99995976 99995963 99995957 99995954 99995951 99995938 99995928 99995926 99995921 99995915 99995911 99995907 99995902 99995897 99995888 99995880 99995870 99995861 99995856 99995854 99995852 99995849 99995840 99995832 99995828 99995818 99995814 99995807 99995802 99995796 99995788 99995785 99995781 99995776 99995774 99995763 99995760 99995756 99995751 99995745 99995731 99995726 99995719 99995717 99995713 99995710 99995706 99995702 99995698 99995694 99995690 99995686 99995680 99995669 99995666 99995661 99995657 99995653 99995648 99995644 99995640 99995635 99995631 99995629 99995624 99995620 99995616 99995601 99995599 99995595 99995593 99995590 99995584 99995577 99995569 99995566 99995558 99995552 99995547 99995545 99995542 99995539 99995535 99995530 99995527 99995523 99995515 99995511 99995508 99995505 99995502 99995498 99995482 99995472 99995464 99995452 99995447 99995437 99995429 99995420 99995418 99995414 99995409 99995399 99995397 99995392 99995386 99995378 99995374 99995372 99995366 99995361 99995355 99995342 99995339 99995336 99995332 99995322 99995319 99995313 99995308 99995301 99995288 99995286 99995276 99995267 99995260 99995249 99995247 99995244 99995239 99995230 99995228 99995220 99995208 99995196 99995183 99995174 99995167 99995160 99995151 99995148 99995144 99995138 99995133 99995127 99995123 99995117 99995111 99995095 99995092 99995086 99995076 99995067 99995053 99995047 99995044 99995037 99995025 99995015 99995004 99995000"
givesSorrow = set(map(int, giveSorrowInput.split()))
givesSorrow = list(givesSorrow)
givesSorrow.sort()
# print(len(givesSorrow), givesSorrow)


def binarySearch(emotions, toFind):
    # print("toFind => ", toFind, emotions)
    l = 0
    h = len(emotions) - 1
    while l <= h:
        # mid = l + ((h - l) // 2)
        mid = (h + l) // 2 
        # print("mid => ", mid, emotions[mid], toFind)
        if int(emotions[mid]) < int(toFind):
            l = mid + 1
        elif int(emotions[mid]) > int(toFind):
            h = mid - 1
        else:
            return 1
    return 0


totalHappiness = 0
happy = 0
for i in range(0, len(givesHappiness)):
    if binarySearch(arr, givesHappiness[i]) == True:
        happy += 1
        totalHappiness += 1
print("only happy => ", happy)
print("totalHappiness => after happiness =>", totalHappiness)

sorrow = 0
for i in range(0, len(givesSorrow)):
    if binarySearch(arr, givesSorrow[i]) == True:
        sorrow += 1
        totalHappiness -= 1
print("only sorrow => ", sorrow)
print("totalHappiness => after sorrow =>", totalHappiness)
    