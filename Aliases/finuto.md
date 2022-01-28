# Session Tracker -- !finuto

Ok, so here is the Alias I use for generating a blurb at the end of an encounter so that it'll track all the important information. I can then pin this which will notate the begining and end of a single encounter.

It is used like:
 	`!finuto 1 1 "2x CR1 Giants" 3246 2 100 400 "Link to encounter starting point"`

This is pretty Simple,
* **1 1** -> Quest 1, Encounter 1:
	* This helps track my progress towards an RP challenge between multiple sessions.
* **"2x CR1 Giants"** -> Encounter Details:
	* This can be any important details from the encounter you wish.
* **3246** -> Coins looted off the creature(s) in CP.
* **2** -> Number of gems looted from this encounter.
* **100** -> type of gem looted from this encounter.
* **400** -> Total experience from this encounter.
* **"Link to encounter starting point"** -> Just paste the link inside quotation marks.

```py
!alias finuto tembed 
<drac2>
q=int("&1&") if "&1&".strip('-+').isdigit() else 1
e=int("&2&") if "&2&".strip('-+').isdigit() else 1
monsters=str("&3&")
cp=int("&4&") if "&4&".strip('-+').isdigit() else 0
G1=int("&5&") if "&5&".strip('-+').isdigit() else 0
G2=int("&6&") if "&6&".strip('-+').isdigit() else 10
X=int("&7&") if "&7&".strip('-+').isdigit() else 0
Start=str("&8&")
</drac2>
-title "<name> finishes an Encounter!" -f "Encounter Q{{q}}E{{e}} (Quest#Encounter#)|{{monsters}}" -f "Rolled Loot|{{cp}}cp" -f "Gems|{{G1}}x {{G2}}gp each" -f "Experience|{{X}}xp" -f "[Combat Start Point]({{Start}})" -footer "!finuto [quest#][Encounter#][Monster][Loot in cp][Gems#][Gems worth][XP][Combat start] - Cobbled together by Pat13nce."
```