# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import re
import json
# regrex '[a-z]+
stopwords = set("i,me,my,myself,we,us,our,ours,ourselves,you,your,yours,yourself,yourselves,he,him,his,himself,she,her,hers,herself,it,its,itself,they,them,their,theirs,themselves,what,which,who,whom,whose,this,that,these,those,am,is,are,was,were,be,been,being,have,has,had,having,do,does,did,doing,will,would,should,can,could,ought,i,you,he,she,it,we,they,i,you,we,they,i,you,he,she,we,they,i,you,he,she,we,they,isn,aren,wasn,weren,hasn,haven,hadn,doesn,don,didn,won,wouldn,shan,shouldn,can,cannot,couldn,mustn,let,that,who,what,here,there,when,where,why,how,a,an,the,and,but,if,or,because,as,until,while,of,at,by,for,with,about,against,between,into,through,during,before,after,above,below,to,from,up,upon,down,in,out,on,off,over,under,again,further,then,once,here,there,when,where,why,how,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,so,than,too,very,say,says,said,shall,x,y,your,yours,yourself,yourselves,you,yond,yonder,yon,ye,yet,z,zillion,j,u,umpteen,usually,us,username,uponed,upons,uponing,upon,ups,upping,upped,up,unto,until,unless,unlike,unliker,unlikest,under,underneath,use,used,usedest,r,rath,rather,rathest,rathe,re,relate,related,relatively,regarding,really,res,respecting,respectively,q,quite,que,qua,n,neither,neaths,neath,nethe,nethermost,necessary,necessariest,necessarier,never,nevertheless,nigh,nighest,nigher,nine,noone,nobody,nobodies,nowhere,nowheres,no,noes,nor,nos,no-one,none,not,notwithstanding,nothings,nothing,nathless,natheless,t,ten,tills,till,tilled,tilling,to,towards,toward,towardest,towarder,together,too,thy,thyself,thus,than,that,those,thou,though,thous,thouses,thoroughest,thorougher,thorough,thoroughly,thru,thruer,thruest,thro,through,throughout,throughest,througher,thine,this,thises,they,thee,the,then,thence,thenest,thener,them,themselves,these,therer,there,thereby,therest,thereafter,therein,thereupon,therefore,their,theirs,thing,things,three,two,o,oh,owt,owning,owned,own,owns,others,other,otherwise,otherwisest,otherwiser,of,often,oftener,oftenest,off,offs,offest,one,ought,oughts,our,ours,ourselves,ourself,out,outest,outed,outwith,outs,outside,over,overallest,overaller,overalls,overall,overs,or,orer,orest,on,oneself,onest,ons,onto,a,atween,at,athwart,atop,afore,afterward,afterwards,after,afterest,afterer,ain,an,any,anything,anybody,anyone,anyhow,anywhere,anent,anear,and,andor,another,around,ares,are,aest,aer,against,again,accordingly,abaft,abafter,abaftest,abovest,above,abover,abouter,aboutest,about,aid,amidst,amid,among,amongst,apartest,aparter,apart,appeared,appears,appear,appearing,appropriating,appropriate,appropriatest,appropriates,appropriater,appropriated,already,always,also,along,alongside,although,almost,all,allest,aller,allyou,alls,albeit,awfully,as,aside,asides,aslant,ases,astrider,astride,astridest,astraddlest,astraddler,astraddle,availablest,availabler,available,aughts,aught,vs,v,variousest,variouser,various,via,vis-a-vis,vis-a-viser,vis-a-visest,viz,very,veriest,verier,versus,k,g,go,gone,good,got,gotta,gotten,get,gets,getting,b,by,byandby,by-and-by,bist,both,but,buts,be,beyond,because,became,becomes,become,becoming,becomings,becominger,becomingest,behind,behinds,before,beforehand,beforehandest,beforehander,bettered,betters,better,bettering,betwixt,between,beneath,been,below,besides,beside,m,my,myself,mucher,muchest,much,must,musts,musths,musth,main,make,mayest,many,mauger,maugre,me,meanwhiles,meanwhile,mostly,most,moreover,more,might,mights,midst,midsts,h,huh,humph,he,hers,herself,her,hereby,herein,hereafters,hereafter,hereupon,hence,hadst,had,having,haves,have,has,hast,hardly,hae,hath,him,himself,hither,hitherest,hitherer,his,how-do-you-do,however,how,howbeit,howdoyoudo,hoos,hoo,w,woulded,woulding,would,woulds,was,wast,we,wert,were,with,withal,without,within,why,what,whatever,whateverer,whateverest,whatsoeverer,whatsoeverest,whatsoever,whence,whencesoever,whenever,whensoever,when,whenas,whether,wheen,whereto,whereupon,wherever,whereon,whereof,where,whereby,wherewithal,wherewith,whereinto,wherein,whereafter,whereas,wheresoever,wherefrom,which,whichever,whichsoever,whilst,while,whiles,whithersoever,whither,whoever,whosoever,whoso,whose,whomever,s,syne,syn,shalling,shall,shalled,shalls,shoulding,should,shoulded,shoulds,she,sayyid,sayid,said,saider,saidest,same,samest,sames,samer,saved,sans,sanses,sanserifs,sanserif,so,soer,soest,sobeit,someone,somebody,somehow,some,somewhere,somewhat,something,sometimest,sometimes,sometimer,sometime,several,severaler,severalest,serious,seriousest,seriouser,senza,send,sent,seem,seems,seemed,seemingest,seeminger,seemings,seven,summat,sups,sup,supping,supped,such,since,sine,sines,sith,six,stop,stopped,p,plaintiff,plenty,plenties,please,pleased,pleases,per,perhaps,particulars,particularly,particular,particularest,particularer,pro,providing,provides,provided,provide,probably,l,layabout,layabouts,latter,latterest,latterer,latterly,latters,lots,lotting,lotted,lot,lest,less,ie,ifs,if,i,info,information,itself,its,it,is,idem,idemer,idemest,immediate,immediately,immediatest,immediater,in,inwards,inwardest,inwarder,inward,inasmuch,into,instead,insofar,indicates,indicated,indicate,indicating,indeed,inc,f,fact,facts,fs,figupon,figupons,figuponing,figuponed,few,fewer,fewest,frae,from,failing,failings,five,furthers,furtherer,furthered,furtherest,further,furthering,furthermore,fourscore,followthrough,for,forwhy,fornenst,formerly,former,formerer,formerest,formers,forbye,forby,fore,forever,forer,fores,four,d,ddays,dday,do,doing,doings,doe,does,doth,downwarder,downwardest,downward,downwards,downs,done,doner,dones,donest,dos,dost,did,differentest,differenter,different,describing,describe,describes,described,despiting,despites,despited,despite,during,c,cum,circa,chez,cer,certain,certainest,certainer,cest,canst,cannot,cant,cants,canting,cantest,canted,co,could,couldst,comeon,comeons,come-ons,come-on,concerning,concerninger,concerningest,consequently,considering,e,eg,eight,either,even,evens,evenser,evensest,evened,evenest,ever,everyone,everything,everybody,everywhere,every,ere,each,et,etc,elsewhere,else,ex,excepted,excepts,except,excepting,exes,enough,http,https,just, still, get, go".split(","))

# %%
# read files and concat -> contents_concat

# sport = ['RealSkipBayless', 'ShannonSharpe', 'PatMcAfeeShow', 'stephenasmith', 'maxkellerman']
# actor = ['EmmaWatson', 'AnnaKendrick47', 'VancityReynolds', 'Matt_Leblanc', 'RobertDowneyJr']
# nba = ['KingJames', 'KDTrey5', 'Giannis_An34', 'StephenCurry30', 'JoelEmbiid']
# musician = ['steveaoki', 'CousinStizz', 'trvisXX', 'justinbieber', 'ladygaga']
# entrepreneur =['mcuban', 'travisk', 'ev', 'TonyRobbins']
# cornell = ['Jsipple', 'informor', 'soumitradutta', 'DrMaureenHanson', 'GeoffreyWCoates']
# groups = [sport, actor, nba, musician, entrepreneur, cornell]

groups = {}
groups["sport"] = ['RealSkipBayless', 'ShannonSharpe', 'PatMcAfeeShow', 'stephenasmith', 'maxkellerman']
groups["actor"] = ['EmmaWatson', 'AnnaKendrick47', 'VancityReynolds', 'Matt_Leblanc', 'RobertDowneyJr']
groups["nba"] = ['KingJames', 'KDTrey5', 'Giannis_An34', 'StephenCurry30', 'JoelEmbiid']
groups["musician"] = ['steveaoki', 'CousinStizz', 'trvisXX', 'justinbieber', 'ladygaga']
groups["entrepreneur"] =['mcuban', 'travisk', 'ev', 'TonyRobbins']
groups["cornell"] = ['Jsipple', 'informor', 'soumitradutta', 'DrMaureenHanson', 'GeoffreyWCoates']

for group_name in groups.keys():
    group = groups.get(group_name)
    li = []
    for username in group:
        tweets_df = pd.read_csv('../cleaned-data/user-{}-tweets-cleaned.csv'.format(username))
        li.append(tweets_df)

    tweets_concat = pd.concat(li, axis=0, ignore_index=True)
    contents_concat = tweets_concat.loc[:,"content"]

    # count word frequency -> freq
    contents_concat[0].lower()

    freq = {}

    for content in contents_concat:
        text_string = str(content).lower()
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
        for word in match_pattern:
            count = freq.get(word,0)
            freq[word] = count + 1

    # filter stop words
    for key in set(freq.keys()):
        if key in stopwords:
            freq.pop(key)

    # sort frequency map -> 2d array
    freq_sorted = sorted(freq.items(), key = lambda kv:(kv[1]), reverse = True)
    # freq_sorted[0:5]

    # list->json
    freq_sorted_json = json.dumps(freq_sorted[0:100])
    f = open("word-freq-sorted.json", "w")
    f.write(freq_sorted_json)
    f.close()

    # # list->dict->json
    freq_sorted_dict = []

    for i in freq_sorted:
        ele = {}
        ele["text"] = i[0]
        ele["value"] = i[1]
        freq_sorted_dict.append(ele)

    freq_sorted_dict_json = json.dumps(freq_sorted_dict[0:40])
    f = open("word-freq-sorted-{}.json".format(group_name), "w")
    f.write(freq_sorted_dict_json)
    f.close()



# %%
