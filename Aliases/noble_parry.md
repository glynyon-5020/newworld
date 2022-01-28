# Noble Parry Alias

This file contains the alias for the [Noble](https://www.dndbeyond.com/monsters/noble) monster block's **parry** ability. This is useful when you have a noble sidekick.

## Parry Alias

```py
!noble_parry [#, attack roll, character|?]

!alias noble_parry embed
<drac2>
response = ''
if "?" in (&ARGS&[0]):
    response = f'-title "How to Noble Parry!" -desc "Simply type `!noble_parry [damage taken], [attack roll that hit you], [name of the noble] [?]`" -thumb https://i.imgur.com/AJG1itx.png'
else:
    c=combat()
    H=&ARGS&
    ar=int(H[1])
    gc=c.get_combatant(H[2])
    previous_hp=gc.hp_str()
    d=int(H[0]) if ar < gc.ac+2 else 0
    new_hp=gc.modify_hp(d) if ar < gc.ac+2 else gc.hp_str()
    name=gc.name
    response = f'-title "{name} attempts to parry!" -desc "**Parry.** {name}, a [noble](https://www.dndbeyond.com/monsters/noble), adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon." -f "Results | Previous Attack Roll: {ar} versus parried AC of **{gc.ac+2}**\nPrevious Hit Points: {previous_hp}\nParry Results: {new_hp} **(+{d})**" -thumb https://i.imgur.com/AJG1itx.png'
return response
</drac2>
```