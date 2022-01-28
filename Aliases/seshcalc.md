# Session Rewards Calculator Alias

This alias enables you to calculate rewards, guild dues, insurance fees, and sidekick cuts quickly and easily!

It runs a little something like this: `!seshcalc 03 13892 unaffiliated 1000 "Yes"`

Now, that may seem a little daunting. But it's not too bad. I'll explain what these are:

* `03` : this is the level of the player for calculating insurance. If they are opting **out** of insurance, use `01` instead of their level.
* `13892` : this is their earnings in copper. It might require a bit of number crunching in your head to turn platinum, gold, silver, and electrum into copper.
* `unaffiliated` : this is their guild rank for the guild they completed a contract or bounty for. If no contracts or bounties were complete, just write `unaffiliated`; see the list of ranks below.
* `1000` : this is the rewards gifted the player by the guild. In this case, the guild paid the PC 10gp for their efforts.
* `"Yes"` : this says "I had a sidekick in this adventure!" and will subtract 30% of the players earnings for the sidekick's cut of the money.

This is the preferred method of tracking gold rewards as it does it in a certain order.

* Insurance is applied before guild rewards and guild dues
* Guild dues are applied after insurance but before guild rewards
* Sidekick dues apply to everything

This should probably be modified to handle hoards. Guilds do not benefit from hoards. Insurance and sidekick dues **DO** still apply to hoards, however.

## Guild Ranks

| Rank | Bonus Contribution |
| -- | -- |
| Unaffiliated | 110% |
| Apprentice | 115% |
| Journeyman | 120% |
| Adept | 130% |
| Expert | 140% |
| Master | 150% |
| Grandmaster | 175% |

If I made 100gp in a session as an unaffiliated nonmember of a guild, then the guild would make 110gp (1.1*100). They'd also make money from my guild dues (5% of post-insurance earnings), in addition to losing the gold reward they paid out to me. If they owed me 10gp and I didn't take insurance, I'd owe 5gp (5% of 100) in guild dues.

I'd make 105gp and they'd make 105gp. They make more money when they send members out to do their work.

## The Seshcalc Alias

```py
!alias seshcalc embed
{{a = (&ARGS& + ['','','','',''])[:5]}}
<drac2>
grs = {"unaffiliated": .1,"apprentice": .15,"journeyman": .20,"adept": .30,"expert": .40,"master": .50,"grandmaster": .75}
ins = {"Level 01": 0,"Level 02": 2000,"Level 03": 3000,"Level 04": 4000,"Level 05": 5000,"Level 06": 30000,"Level 07": 35000,"Level 08": 40000,"Level 09": 45000,"Level 10": 50000,"Level 11": 275000,"Level 12": 300000,"Level 13": 325000,"Level 14": 350000,"Level 15": 375000}
l,i,gr,grwds,n,sk = a[0],int(a[1]),a[2].lower(),int(a[3]),"\n",a[4]
skd=0
fi=0
d=0
gincome=0
bi = ins["Level " + l]
grm = grs[gr]
if i*.2 > bi and bi != 0:
    ins=i*.2
else:
    ins=bi
pi = i-ins
if grwds != 0:
    d=pi*.05
    gincome=(pi*(1+grm))+d-grwds
    fi=pi-d+grwds
else:
    fi=pi
if sk=='Yes':
    skd=fi*.3
    fi=fi*.7

</drac2>
-title "Session Rewards Calculator!"
-f "{{f"Insurance Fees|{'A level ' + l + ' character with a base session earnings of ' + i + 'cp must pay ' + ins + 'cp.'}"}}"
-f "{{f"Guild Dues|{'5% of your post insurance earnings of ' + pi + ' results in Guild Dues of ' + round(d,0) + 'cp.'}"}}"
-f "{{f"Guild Income|{'Your efforts have profited the guild! Thanks to you,  ' + round(gincome,0) + 'cp has been added to their coffers.' + n + 'The guild has also paid you ' + grwds + 'cp for your services.'}"}}"
-f "{{f"Sidekick Cut|{'Your sidekick took ' + round(skd,0) + 'cp.'}"}}"
-f "{{f"PC Session Earnings|{'After insurance fees, guild dues, guild rewards, and your sidekick cut, your net gain is  ' + round(fi,0) + 'cp!'}"}}" 
-f "Parameters | Level (01-15), Income (in cp), Guild Rank (unaffiliated-grandmaster), Guild Rewards (earnings in copper), Sidekick Present (Yes/No)
i.e. `!seshcalc 03 13892 unaffiliated 1000 "Yes"`"
-footer "Made by @""glynyon#5020"
-thumb https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Abacus_6.png/220px-Abacus_6.png
```