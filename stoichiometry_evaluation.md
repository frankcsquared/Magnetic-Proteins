When growing exponentially under aerobic conditions, an _E.coli_ cell contains <img src="https://tex.s2cms.ru/svg/1.2%20%5Ctimes%2010%5E6" alt="1.2 \times 10^6" /> atoms of iron... However, only ∼1% of these atoms (~<img src="https://tex.s2cms.ru/svg/10%5E4" alt="10^4" />) can be found in the free or loosely bound state. [Citation](https://academic.oup.com/femsre/article/27/2-3/215/614497)

If we assume that the rest is in ferritin, this puts an upper bound of ~300 ferritin per normal cell. I don't know what happens if we overexpress it, if you suppose that you can get even 0.1% of the [total number of proteins per cell](http://book.bionumbers.org/how-many-proteins-are-in-a-cell/) of <img src="https://tex.s2cms.ru/svg/2.36%5Ctimes10%5E6" alt="2.36\times10^6" />, you can get a 8-fold increase to 2360 ferritin per cell.

For HP: You can calculate the cost per mols removed (and use that to figure out cost to purify something). In this application, culture medium represents [30% of total cost](https://www.sciencedirect.com/science/article/pii/S151783821730134X#bib0270). If we assume that the cost of medium is on the order of magnitude of [$4.2/litre](https://www.thermofisher.com/search/browse/category/ca/en/99201), the cost per volume bacteria required is $12/litre. But a wet lab person would know more about the costs of growing bacteria, lysing them, then eluting the magnetic stuff...


## Volume of bacteria required per mol removed

<img src="https://tex.s2cms.ru/svg/R" alt="R" />: mols of substance removed (variable)

<img src="https://tex.s2cms.ru/svg/N_A" alt="N_A" />: avogadro's constant (<img src="https://tex.s2cms.ru/svg/6.02%5Ctimes%2010%5E%7B23%7D" alt="6.02\times 10^{23}" /> atoms/mol)

<img src="https://tex.s2cms.ru/svg/AF" alt="AF" />: atoms bound per ferritin (24+ atoms/ferritin)

<img src="https://tex.s2cms.ru/svg/FB" alt="FB" />: ferritin per bacterium (300-2360 ferritin/cell)

<img src="https://tex.s2cms.ru/svg/D" alt="D" />: density (<img src="https://tex.s2cms.ru/svg/1%5Ctimes%2010%5E%7B8%7D%20" alt="1\times 10^{8} " /> bacteria/mL = <img src="https://tex.s2cms.ru/svg/1%5Ctimes%2010%5E%7B11%7D%20" alt="1\times 10^{11} " /> bacteria/L)

<img src="https://tex.s2cms.ru/svg/V_b" alt="V_b" />: volume of bacteria required (L)

<img src="https://tex.s2cms.ru/svg/V_b%20%5C%20(L)%20%3D%20%5Cbold%7BR%7D%20(%5Ctext%7Bmol%20removed%7D)%20%20%5Ccdot%20N_A(%5Cfrac%7B%5Ctext%7Batoms%7D%7D%7B%5Ctext%7Bmol%20removed%7D%7D)%20%5Ccdot%20%5B1%2F%5Ctext%7BAF%7D%5D(%5Cfrac%7B%5Ctext%7Bferritin%7D%7D%7B%5Ctext%7Batoms%7D%7D)%20%20%5Ccdot%20%5B1%2F%5Ctext%7BFB%7D%5D(%5Cfrac%7B%5Ctext%7Bbacterium%7D%7D%7B%5Ctext%7Bferritin%7D%7D)%20%5Ccdot%20%5B1%2F%5Ctext%7BD%7D%5D%20(%5Cfrac%7B%5Ctext%7BL%7D%7D%7B%5Ctext%7Bbacterium%7D%7D)%20" alt="V_b \ (L) = \bold{R} (\text{mol removed})  \cdot N_A(\frac{\text{atoms}}{\text{mol removed}}) \cdot [1/\text{AF}](\frac{\text{ferritin}}{\text{atoms}})  \cdot [1/\text{FB}](\frac{\text{bacterium}}{\text{ferritin}}) \cdot [1/\text{D}] (\frac{\text{L}}{\text{bacterium}}) " />

### Pessimistic analysis

<img src="https://tex.s2cms.ru/svg/V_b%20%5C%20(L)%20%3D%20%5Cbold%7BR%7D%20(%5Ctext%7Bmol%20removed%7D)%20%20%5Ccdot%206.02%20%5Ctimes%2010%5E%7B23%7D%20%5Ccdot%20%5B1%2F24%5D(%5Cfrac%7B%5Ctext%7Bferritin%7D%7D%7B%5Ctext%7Batoms%7D%7D)%20%20%5Ccdot%20%5B1%2F300%5D(%5Cfrac%7B%5Ctext%7Bbacterium%7D%7D%7B%5Ctext%7Bferritin%7D%7D)%20%5Ccdot%20%5B1%2F10%5E%7B11%7D%5D%20(%5Cfrac%7B%5Ctext%7BL%7D%7D%7B%5Ctext%7Bbacterium%7D%7D)%20" alt="V_b \ (L) = \bold{R} (\text{mol removed})  \cdot 6.02 \times 10^{23} \cdot [1/24](\frac{\text{ferritin}}{\text{atoms}})  \cdot [1/300](\frac{\text{bacterium}}{\text{ferritin}}) \cdot [1/10^{11}] (\frac{\text{L}}{\text{bacterium}}) " />

<img src="https://tex.s2cms.ru/svg/V_b%20%3D%208.4%5Ctimes%2010%5E%7B8%7D%20%5Ccdot%20R" alt="V_b = 8.4\times 10^{8} \cdot R" />

### Optimistic analysis

<img src="https://tex.s2cms.ru/svg/V_b%20%5C%20(L)%20%3D%20%5Cbold%7BR%7D%20(%5Ctext%7Bmol%20removed%7D)%20%20%5Ccdot%206.02%20%5Ctimes%2010%5E%7B23%7D%20%5Ccdot%20%5B1%2F24%5D(%5Cfrac%7B%5Ctext%7Bferritin%7D%7D%7B%5Ctext%7Batoms%7D%7D)%20%20%5Ccdot%20%5B1%2F2360%5D(%5Cfrac%7B%5Ctext%7Bbacterium%7D%7D%7B%5Ctext%7Bferritin%7D%7D)%20%5Ccdot%20%5B1%2F10%5E%7B11%7D%5D%20(%5Cfrac%7B%5Ctext%7BL%7D%7D%7B%5Ctext%7Bbacterium%7D%7D)%20" alt="V_b \ (L) = \bold{R} (\text{mol removed})  \cdot 6.02 \times 10^{23} \cdot [1/24](\frac{\text{ferritin}}{\text{atoms}})  \cdot [1/2360](\frac{\text{bacterium}}{\text{ferritin}}) \cdot [1/10^{11}] (\frac{\text{L}}{\text{bacterium}}) " />

<img src="https://tex.s2cms.ru/svg/V_b%20%3D%201.1%5Ctimes%2010%5E%7B8%7D%20%5Ccdot%20R" alt="V_b = 1.1\times 10^{8} \cdot R" />

Under the pessimistic analysis, removing 5<img src="https://tex.s2cms.ru/svg/%5Cmu" alt="\mu" />g of lead from 1 L of water would take (8.4E8*(5E-6/207.2) = 20 L of bacteria to grow, at a cost of $280. This is clearly not great for this application, but such efficacy might be for some sort of laboratory application requiring less volume and with lower concentrations? 
