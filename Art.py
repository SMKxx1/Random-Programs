def art():
    print('''

                                                                                                    `-+/                                                                                                                                                  
                                                                                                `/syyo:                                                                                                                                                   
                                                                                                -:                                                                                                                                                      
                                                                                                                                                                 .++`                                                                                     
                                                                                                oo-``                                                           :dsM+                                                                                     
                         +-                                           `o`            ``        .MMMNh                                                           /NhN-                                   //                                     -`         
                       `yMy                                          .dMo           /mh+`      -yMMNs                                                           .yhhy                                 `oMm                                    +MNh/       
                       -mMN`              ++-`                       /NMd          `ymMh.        hMs`                                                        `-ss:  `                                 .dMM-                                   +hmd.:-`    
                        .NM-             +MMMs                        :MM`           .:`         -Mm`                                                        `.`                                       `mM+                                   ::-./NMms   
          .hy/.          yM/             .:oy`                         mM.                        hM/                                                                                          /o-      +Mo                                  /NMmy:ohd-   
          smMN/          +M+                                           yM-         `:+o/.         /My                                                                                          yMNh-    :My                                  -+hd-   `    
           .::           /Mo           `...`                           oM:        .hMMMMm:        `Mm                                                                                          :odMN/   .My              `.`                    `         
                    ++   -Ms         -ymmNmmh+-                        +M/        dMs/oNMm`        md    .-/ossso:`                           `-/ossso/.            ./ss`                        `:mN-   Mh            `+dNm-                         `:  
    `              :NN:  `My        -hhddNMMMMNh/`                     :M+       .MM:` -NM/        mo`:ohmNMMMMMMMm:      //               ./hmNMMMMMMMNo         :ymmmMd.                         .Ny   Nm           -dhomMs          `s`        s`  sMo 
   .y`             +MMh   Nm`       `` ``.-/ymMMMmo.                   .Mh       `hMNmhymM+       -MdmNdyo+/:/+smMMN`     oN-           ./hNmds+/:/+sdMMM:      .yNm:``yMm.                         oN   hM.         :m+``yM/          `Ms        m+  `yN 
  `h:               oMm   yMo                `:smMMNy:`                 dM/       `:oyhdNMo   `.:smds/.`       .oMMM.    `yMNo.    `-/ohdho:.`      `:MMMo   `-sNMMNs/-.mMy              ::         :M`  +My`       :No/oys:           :MMy-     -NN/` -M`
  yo                 mN   -MMmddddddddddddddddddmMMMMMmd/               /MNdddddddddddmNMMmddmmNMMNmdddddddddmmNMMMMddddmmMMMMNmddmNNMMMmddddddddddmmNMMMNddmmNMMmNMMMNmNMN              hNmddddddddmM.  `NMmdddddddNMNMNmddddddddddddmNMMMNmdddmNMMMmmNM`
 :N`                 yN    /dNNMMNNNNNNNNNNNNNNNNNNNNNNN+                +dNNMMNNNNNNNNNNMMNNNNNNNNNNNNNNNNNNNNNNNMMNNNNNmh+ydNNNNNNNNNNNNNNNNNNNNNNNNNNMMNNNNdy/``:shmNNNN              :hmNNNNNNNNNN.   -hNNNMNNNMMNMMMMNNNNNNMMNNNNNdsohmNNNNNds+hmNNN`
 yN`                .mm     `````````````````````````````                 ````````````````````````````````````````````````   ``````````````````````````````````       `````                ```````````      ```````sN../ymmo.```````````   ```````   ```` 
 dMs`             .omMs                                                                                                                                                                                            /Ms   `+Nh`                            
 oMMNy+:--.--:/oymNMMh`                                                                                                                                                                                            `yMmo/::dM:                            
  +mMMMMMMMMMMMMMMNh/                                                                                                                                                                                                /hMMMMMN.                            
    ./osyyhhyys+/-                                                                                                                                                                                                     `:/++`                             
''')

def clear():
    print("\n"*70)


import random


def main():
    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        art()
        print("Rolling the dices...")

        print("The values are....")

        print(random.randint(min, max))

        print(random.randint(min, max))

        roll_again = input("Roll the dices again?")
        clear()

main()
