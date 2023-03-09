from io import BytesIO
import io
from PIL import Image,ImageFont,ImageDraw,ImageEnhance,ImageFilter
import codecs,json
import os 
import itertools
from collections import Counter
import base64

from PIL import ImageFile 
ImageFile.LOAD_TRUNCATED_IMAGES = True

def culculate_op(data:dict):

    cwd = os.path.dirname(os.path.abspath(__file__))
    with codecs.open(f'{cwd}/Assets/duplicate.json', 'r',encoding='utf-8') as f:
        dup = json.load(f)
    with codecs.open(f'{cwd}/Assets/subopM.json', 'r',encoding='utf-8') as f:
        mapping = json.load(f)

    res = [None,None,None,None]
    keymap = list(map(str,data.keys()))

    is_dup = []
    #重複するものがあるか判定
    for ctg,state in data.items():
        dup_value = dup[ctg]['ov']
        if str(state) in dup_value:
            is_dup.append((ctg,state))


    #フラグの設定
    counter_flag = 0
    dup_ctg = [i[0] for i in is_dup]
    maxium_state_ct = 9

    #重複が 0 の時の処理
    if not len(is_dup):
        for ctg,state in data.items():
            idx = keymap.index(ctg)
            res[idx] = mapping[ctg][str(state)]
        return res
            


    #重複するものが一つの場合
    
    if len(is_dup) == 1:
        #重複のないもの
        single_state = {c:s for c,s in data.items() if c not in dup_ctg}
        for ctg,state in single_state.items():
            idx = keymap.index(ctg)
            res[idx] = mapping[ctg][str(state)]
            counter_flag += len(mapping[ctg][str(state)])

        #重複するもの
        dup_state = {c:s for c,s in data.items() if c in dup_ctg}
        long = maxium_state_ct - counter_flag
        possiblity = []

        for ctg,state in dup_state.items():
            possiblity = dup[ctg][str(state)]
            for p in possiblity:
                if len(p) == long or len(p) == long-1:
                    idx = keymap.index(ctg)
                    res[idx] = p
                    return res


    

            

        
        


    #重複するものが複数の場合
    if len(is_dup) == 2:
        single_state = {c:s for c,s in data.items() if c not in dup_ctg}
        for ctg,state in single_state.items():
            idx = keymap.index(ctg)
            res[idx] = mapping[ctg][str(state)]
            counter_flag += len(mapping[ctg][str(state)])

        dup_state = {c:s for c,s in data.items() if c in dup_ctg}
        long = maxium_state_ct - counter_flag
        
        sample = [[ctg,state]for ctg,state in dup_state.items()]

        possiblity1 = dup[sample[0][0]][str(sample[0][1])]
        possiblity2 = dup[sample[1][0]][str(sample[1][1])]

        p1 = [len(p) for p in possiblity1]
        p2 = [len(p) for p in possiblity2]

        p = itertools.product(p1, p2)
        r = None
        for v in p:
            if sum(v) == long or sum(v) == long-1:
                r = v
                break

        idx1 = keymap.index(sample[0][0])
        idx2 = keymap.index(sample[1][0])

        res[idx1] = possiblity1[p1.index(v[0])]
        res[idx2] = possiblity2[p2.index(v[1])]
        return res

    if len(is_dup) == 3:
        single_state = {c:s for c,s in data.items() if c not in dup_ctg}
        for ctg,state in single_state.items():
            idx = keymap.index(ctg)
            res[idx] = mapping[ctg][str(state)]
            counter_flag += len(mapping[ctg][str(state)])

        dup_state = {c:s for c,s in data.items() if c in dup_ctg}
        long = maxium_state_ct - counter_flag
        
        sample = [[ctg,state]for ctg,state in dup_state.items()]

        possiblity1 = dup[sample[0][0]][str(sample[0][1])]
        possiblity2 = dup[sample[1][0]][str(sample[1][1])]
        possiblity3 = dup[sample[2][0]][str(sample[2][1])]

        p1 = [len(p) for p in possiblity1]
        p2 = [len(p) for p in possiblity2]
        p3 = [len(p) for p in possiblity3]

        p = itertools.product(p1, p2,p3)
        r = None
        for v in p:
            if sum(v) == long or sum(v) == long-1:
                r = v
                break

        idx1 = keymap.index(sample[0][0])
        idx2 = keymap.index(sample[1][0])
        idx3 = keymap.index(sample[2][0])

        res[idx1] = possiblity1[p1.index(v[0])]
        res[idx2] = possiblity2[p2.index(v[1])]
        res[idx3] = possiblity3[p3.index(v[2])]

        return res

    if len(is_dup) == 4:
        dup_state = {c:s for c,s in data.items() if c in dup_ctg}
        long = maxium_state_ct - counter_flag
        
        sample = [[ctg,state]for ctg,state in dup_state.items()]

        possiblity1 = dup[sample[0][0]][str(sample[0][1])]
        possiblity2 = dup[sample[1][0]][str(sample[1][1])]
        possiblity3 = dup[sample[2][0]][str(sample[2][1])]
        possiblity4 = dup[sample[3][0]][str(sample[3][1])]

        p1 = [len(p) for p in possiblity1]
        p2 = [len(p) for p in possiblity2]
        p3 = [len(p) for p in possiblity3]
        p4 = [len(p) for p in possiblity4]

        p = itertools.product(p1, p2,p3,p4)
        r = None
        for v in p:
            if sum(v) == long or sum(v) == long-1:
                r = v
                break

        idx1 = keymap.index(sample[0][0])
        idx2 = keymap.index(sample[1][0])
        idx3 = keymap.index(sample[2][0])
        idx4 = keymap.index(sample[3][0])

        res[idx1] = possiblity1[p1.index(v[0])]
        res[idx2] = possiblity2[p2.index(v[1])]
        res[idx3] = possiblity3[p3.index(v[2])]
        res[idx4] = possiblity4[p4.index(v[3])]

        return res
    return

def read_json(path):
    with codecs.open(path,encoding='utf-8') as f:
        data = json.load(f)
    return data

def generation(data):
    #config 
    element = data.get('元素')
    
    CharacterData :dict = data.get('Character')
    CharacterName : str = CharacterData.get('Name')
    CharacterConstellations :int = CharacterData.get('Const')
    CharacterLevel : int = CharacterData.get('Level')
    FriendShip : int = CharacterData.get('Love')
    CharacterStatus : dict = CharacterData.get('Status')
    CharacterBase : dict = CharacterData.get('Base')
    CharacterTalent:dict = CharacterData.get('Talent')
    
    Weapon : dict = data.get('Weapon')
    WeaponName : str =Weapon.get('name')
    WeaponLevel : int =Weapon.get('Level')
    WeaponRank : int =Weapon.get('totu')
    WeaponRarelity : int =Weapon.get('rarelity')
    WeaponBaseATK: int = Weapon.get('BaseATK')
    WeaponSubOP : int = Weapon.get('Sub')
    WeaponSubOPKey : str = WeaponSubOP.get('name')
    WeaponSubOPValue : str = WeaponSubOP.get('value')
    
    ScoreData : dict = data.get('Score')
    ScoreCVBasis:str = ScoreData.get('State')
    ScoreFlower :float = ScoreData.get('flower')
    ScoreWing :float = ScoreData.get('wing')
    ScoreClock:float = ScoreData.get('clock')
    ScoreCup :float = ScoreData.get('cup')
    ScoreCrown :float = ScoreData.get('crown')
    ScoreTotal :float = ScoreData.get('total')
    
    ArtifactsData : dict = data.get('Artifacts')


    cwd = os.path.abspath(os.path.dirname(__file__))
    config_font = lambda size : ImageFont.truetype(f'{cwd}/Assets/ja-jp.ttf',size)
    
    Base = Image.open(f'{cwd}/Base/{element}.png')
    
    
    #キャラクター
    CharacterCostume = CharacterData.get('Costume')
    if CharacterName in ['蛍','空']:
        CharacterImage = Image.open(f'{cwd}/character/{CharacterName}({element})/avatar.png').convert("RGBA")
    else:
        if CharacterCostume:
            CharacterImage = Image.open(f'{cwd}/character/{CharacterName}/{CharacterCostume}.png').convert("RGBA")
        else:
            CharacterImage = Image.open(f'{cwd}/character/{CharacterName}/avatar.png').convert("RGBA")
            
    
    
    Shadow = Image.open(f'{cwd}/Assets/shadow.png').resize(Base.size)
    CharacterImage = CharacterImage.crop((289,0,1728,1024))
    CharacterImage = CharacterImage.resize((int(CharacterImage.width*0.75), int(CharacterImage.height*0.75)))
    
    CharacterAvatarMask = CharacterImage.copy()
    
    if CharacterName == 'アルハイゼン':
        CharacterAvatarMask2 = Image.open(f'{cwd}/Assets/Alhaitham.png').convert('L').resize(CharacterImage.size)
    else:
        CharacterAvatarMask2 = Image.open(f'{cwd}/Assets/CharacterMask.png').convert('L').resize(CharacterImage.size)
    CharacterImage.putalpha(CharacterAvatarMask2)
    
    CharacterPaste = Image.new("RGBA",Base.size,(255,255,255,0))
    
    CharacterPaste.paste(CharacterImage,(-160,-45),mask=CharacterAvatarMask)
    Base = Image.alpha_composite(Base,CharacterPaste)
    Base = Image.alpha_composite(Base,Shadow)
    
    
    #武器
    Weapon = Image.open(f'{cwd}/weapon/{WeaponName}.png').convert("RGBA").resize((128,128))
    WeaponPaste = Image.new("RGBA",Base.size,(255,255,255,0))
    
    WeaponMask = Weapon.copy()
    WeaponPaste.paste(Weapon,(1430,50),mask=WeaponMask)
    
    Base = Image.alpha_composite(Base,WeaponPaste)
    
    WeaponRImage = Image.open(f'{cwd}/Assets/Rarelity/{WeaponRarelity}.png').convert("RGBA")
    WeaponRImage = WeaponRImage.resize((int(WeaponRImage.width*0.97),int(WeaponRImage.height*0.97)))
    WeaponRPaste = Image.new("RGBA",Base.size,(255,255,255,0))
    WeaponRMask = WeaponRImage.copy()
    
    WeaponRPaste.paste(WeaponRImage,(1422,173),mask=WeaponRMask)
    Base = Image.alpha_composite(Base,WeaponRPaste)
    
    #天賦
    TalentBase = Image.open(f'{cwd}/Assets/TalentBack.png')
    TalentBasePaste = Image.new("RGBA",Base.size,(255,255,255,0))
    TalentBase = TalentBase.resize((int(TalentBase.width/1.5),int(TalentBase.height/1.5)))
    
    for i,t in enumerate(['通常','スキル',"爆発"]):
        TalentPaste = Image.new("RGBA",TalentBase.size,(255,255,255,0))
        Talent = Image.open(f'{cwd}/character/{CharacterName}/{t}.png').resize((50,50)).convert('RGBA')
        TalentMask = Talent.copy()
        TalentPaste.paste(Talent,(TalentPaste.width//2-25,TalentPaste.height//2-25),mask=TalentMask)
        
        TalentObject = Image.alpha_composite(TalentBase,TalentPaste)
        TalentBasePaste.paste(TalentObject,(15,330+i*105))
        
    Base = Image.alpha_composite(Base,TalentBasePaste)
    
    #凸
    CBase = Image.open(f'{cwd}/命の星座/{element}.png').resize((90,90)).convert('RGBA')
    Clock = Image.open(f'{cwd}/命の星座/{element}LOCK.png').resize((90,90)).convert('RGBA')
    ClockMask = Clock.copy()
    
    CPaste = Image.new("RGBA",Base.size,(255,255,255,0))
    for c in range(1,7):
        if c > CharacterConstellations:
            CPaste.paste(Clock,(666,-10+c*93),mask=ClockMask)
        else:
            CharaC = Image.open(f'{cwd}/character/{CharacterName}/{c}.png').convert("RGBA").resize((45,45))
            CharaCPaste = Image.new("RGBA",CBase.size,(255,255,255,0))
            CharaCMask = CharaC.copy()
            CharaCPaste.paste(CharaC,(int(CharaCPaste.width/2)-25,int(CharaCPaste.height/2)-23),mask=CharaCMask)
            
            Cobject = Image.alpha_composite(CBase,CharaCPaste)
            CPaste.paste(Cobject,(666,-10+c*93))
    
    Base = Image.alpha_composite(Base,CPaste)
    D = ImageDraw.Draw(Base)
    
    D.text((30,20),CharacterName,font=config_font(48))
    levellength = D.textlength("Lv."+str(CharacterLevel),font=config_font(25))
    friendshiplength = D.textlength(str(FriendShip),font=config_font(25))
    D.text((35,75),"Lv."+str(CharacterLevel),font=config_font(25))
    D.rounded_rectangle((35+levellength+5,74,77+levellength+friendshiplength,102),radius=2,fill="black")
    FriendShipIcon = Image.open(f'{cwd}/Assets/Love.png').convert("RGBA")
    FriendShipIcon = FriendShipIcon.resize((int(FriendShipIcon.width*(24/FriendShipIcon.height)),24))
    Fmask = FriendShipIcon.copy()
    Base.paste(FriendShipIcon,(42+int(levellength),76),mask=Fmask)
    D.text((73+levellength,74),str(FriendShip),font=config_font(25))
    
    D.text((42,397),f'Lv.{CharacterTalent["通常"]}',font=config_font(17),fill='aqua' if CharacterTalent["通常"] >= 10 else None)
    D.text((42,502),f'Lv.{CharacterTalent["スキル"]}',font=config_font(17),fill='aqua' if CharacterTalent["スキル"] >= 10 else None)
    D.text((42,607),f'Lv.{CharacterTalent["爆発"]}',font=config_font(17),fill='aqua' if CharacterTalent["爆発"] >= 10 else None)
    
    def genbasetext(state):
        sumv = CharacterStatus[state]
        plusv = sumv - CharacterBase[state]
        basev = CharacterBase[state]
        return f"+{format(plusv,',')}",f"{format(basev,',')}",D.textlength(f"+{format(plusv,',')}",font=config_font(12)),D.textlength(f"{format(basev,',')}",font=config_font(12))
    
    disper = ['会心率','会心ダメージ','攻撃パーセンテージ','防御パーセンテージ','HPパーセンテージ','水元素ダメージ','物理ダメージ','風元素ダメージ','岩元素ダメージ','炎元素ダメージ','与える治癒効果','与える治療効果','雷元素ダメージ','氷元素ダメージ','草元素ダメージ','与える治癒効果','元素チャージ効率']
    StateOP = ('HP','攻撃力',"防御力","元素熟知","会心率","会心ダメージ","元素チャージ効率")
    for k,v in CharacterStatus.items():
        if k in ['氷元素ダメージ','水元素ダメージ','岩元素ダメージ','草元素ダメージ','風元素ダメージ','炎元素ダメージ','物理ダメージ','与える治癒効果','雷元素ダメージ'] and v == 0:
            k = f'{element}元素ダメージ'
        try:
            i = StateOP.index(k)
        except:
            i = 7
            D.text((844,67+i*70),k,font=config_font(26))
            opicon = Image.open(f'{cwd}/emotes/{k}.png').resize((40,40))
            oppaste = Image.new('RGBA',Base.size,(255,255,255,0))
            opmask = opicon.copy()
            oppaste.paste(opicon,(789,65+i*70))
            Base = Image.alpha_composite(Base,oppaste)
            D = ImageDraw.Draw(Base)
        
        if k not in disper:
            statelen = D.textlength(format(v,","),config_font(26))
            D.text((1360-statelen,67+i*70),format(v,","),font=config_font(26))
        else:
            statelen = D.textlength(f'{float(v)}%',config_font(26))
            D.text((1360-statelen,67+i*70),f'{float(v)}%',font=config_font(26))
            
        if k in ['HP','防御力','攻撃力']:
            HPpls,HPbase,HPsize,HPbsize = genbasetext(k)
            D.text((1360-HPsize,97+i*70),HPpls,fill=(0,255,0,180),font=config_font(12))
            D.text((1360-HPsize-HPbsize-1,97+i*70),HPbase,font=config_font(12),fill=(255,255,255,180))
    
        
    D.text((1582,47),WeaponName,font=config_font(26))
    wlebellen = D.textlength(f'Lv.{WeaponLevel}',font=config_font(24))
    D.rounded_rectangle((1582,80,1582+wlebellen+4,108),radius=1,fill='black')
    D.text((1584,82),f'Lv.{WeaponLevel}',font=config_font(24))
    

    BaseAtk = Image.open(f'{cwd}/emotes/基礎攻撃力.png').resize((23,23))
    BaseAtkmask = BaseAtk.copy()
    Base.paste(BaseAtk,(1600,120),mask=BaseAtkmask)
    D.text((1623,120),f'基礎攻撃力  {WeaponBaseATK}',font=config_font(23))
    
    optionmap = {
        "攻撃パーセンテージ":"攻撃%",
        "防御パーセンテージ":"防御%",
        "元素チャージ効率":"元チャ効率",
        "HPパーセンテージ":"HP%",
    }
    if WeaponSubOPKey != None:
        BaseAtk = Image.open(f'{cwd}/emotes/{WeaponSubOPKey}.png').resize((23,23))
        BaseAtkmask = BaseAtk.copy()
        Base.paste(BaseAtk,(1600,155),mask=BaseAtkmask)
        
        D.text((1623,155),f'{optionmap.get(WeaponSubOPKey) or WeaponSubOPKey}  {str(WeaponSubOPValue)+"%" if WeaponSubOPKey in disper else format(WeaponSubOPValue,",")}',font=config_font(23))
    
        
    
    D.rounded_rectangle((1430,45,1470,70),radius=1,fill='black')
    D.text((1433,46),f'R{WeaponRank}',font=config_font(24))
    
    ScoreLen = D.textlength(f'{ScoreTotal}',config_font(75))
    D.text((1652-ScoreLen//2,420),str(ScoreTotal),font=config_font(75))
    blen = D.textlength(f'{ScoreCVBasis}換算',font=config_font(24))
    D.text((1867-blen,585),f'{ScoreCVBasis}換算',font=config_font(24))
    
    if ScoreTotal >= 220:
        ScoreEv =Image.open(f'{cwd}/artifactGrades/SS.png')
    elif ScoreTotal >= 200:
        ScoreEv =Image.open(f'{cwd}/artifactGrades/S.png')
    elif ScoreTotal >= 180:
        ScoreEv =Image.open(f'{cwd}/artifactGrades/A.png')
    else:
        ScoreEv =Image.open(f'{cwd}/artifactGrades/B.png')
    
    ScoreEv = ScoreEv.resize((ScoreEv.width//8,ScoreEv.height//8))
    EvMask = ScoreEv.copy()
    
    Base.paste(ScoreEv,(1806,345),mask=EvMask)
    
    #聖遺物
    atftype = list()
    for i,parts in enumerate(['flower',"wing","clock","cup","crown"]):
        details = ArtifactsData.get(parts)
        
        if not details:
            continue
        atftype.append(details['type'])
        PreviewPaste = Image.new('RGBA',Base.size,(255,255,255,0))
        Preview = Image.open(f'{cwd}/Artifact/{details["type"]}/{parts}.png').resize((256,256))
        enhancer = ImageEnhance.Brightness(Preview)
        Preview = enhancer.enhance(0.6)
        Preview= Preview.resize((int(Preview.width*1.3),int(Preview.height*1.3)))
        Pmask1 = Preview.copy()
        
        Pmask = Image.open(f'{cwd}/Assets/ArtifactMask.png').convert('L').resize(Preview.size)
        Preview.putalpha(Pmask)
        if parts in ['flower','crown']:
            PreviewPaste.paste(Preview,(-37+373*i,570),mask=Pmask1)
        elif parts in ['wing','cup']:
            PreviewPaste.paste(Preview,(-36+373*i,570),mask=Pmask1)
        else:
            PreviewPaste.paste(Preview,(-35+373*i,570),mask=Pmask1)
        Base = Image.alpha_composite(Base,PreviewPaste)
        D = ImageDraw.Draw(Base)
        
        mainop = details['main']['option']
        
        mainoplen = D.textlength(optionmap.get(mainop) or mainop,font=config_font(29))
        D.text((375+i*373-int(mainoplen),655),optionmap.get(mainop) or mainop,font=config_font(29))
        MainIcon = Image.open(f'{cwd}/emotes/{mainop}.png').convert("RGBA").resize((35,35))
        MainMask = MainIcon.copy()
        Base.paste(MainIcon,(340+i*373-int(mainoplen),655),mask=MainMask)
        
        mainv = details['main']['value']
        if mainop in disper:
            mainvsize = D.textlength(f'{float(mainv)}%',config_font(49))
            D.text((375+i*373-mainvsize,690),f'{float(mainv)}%',font=config_font(49))
        else:
            mainvsize = D.textlength(format(mainv,","),config_font(49))
            D.text((375+i*373-mainvsize,690),format(mainv,","),font=config_font(49))
        levlen = D.textlength(f'+{details["Level"]}',config_font(21))
        D.rounded_rectangle((373+i*373-int(levlen),748,375+i*373,771),fill='black',radius=2)
        D.text((374+i*373-levlen,749),f'+{details["Level"]}',font=config_font(21))
        
        if details['Level'] == 20 and details['rarelity'] == 5:
            c_data = {}
            for a in details["sub"]:
                if a ['option'] in disper:
                    c_data[a['option']] = str(float(a["value"]))
                else:
                    c_data[a['option']] = str(a["value"])
            psb = culculate_op(c_data)
            
        if len(details['sub']) == 0:
            continue
        
        for a,sub in enumerate(details['sub']):
            SubOP = sub['option']
            SubVal = sub['value']
            if SubOP in ['HP','攻撃力','防御力']:
                D.text((79+373*i,811+50*a),optionmap.get(SubOP) or SubOP,font=config_font(25),fill=(255,255,255,190))
            else:
                D.text((79+373*i,811+50*a),optionmap.get(SubOP) or SubOP,font=config_font(25))
            SubIcon = Image.open(f'{cwd}/emotes/{SubOP}.png').resize((30,30))
            SubMask = SubIcon.copy()
            Base.paste(SubIcon,(44+373*i,811+50*a),mask=SubMask)
            if SubOP in disper:
                SubSize = D.textlength(f'{float(SubVal)}%',config_font(25))
                D.text((375+i*373-SubSize,811+50*a),f'{float(SubVal)}%',font=config_font(25))
            else:
                SubSize = D.textlength(format(SubVal,","),config_font(25))
                if SubOP in ['防御力','攻撃力','HP']:
                    D.text((375+i*373-SubSize,811+50*a),format(SubVal,","),font=config_font(25),fill=(255,255,255,190))
                else:
                    D.text((375+i*373-SubSize,811+50*a),format(SubVal,","),font=config_font(25),fill=(255,255,255))
            
            if details['Level'] == 20 and details['rarelity'] == 5:
                nobi = D.textlength("+".join(map(str,psb[a])),font=config_font(11))
                D.text((375+i*373-nobi,840+50*a),"+".join(map(str,psb[a])),fill=(255, 255, 255, 160),font=config_font(11))
        
        Score = float(ScoreData[parts])
        ATFScorelen = D.textlength(str(Score),config_font(36))
        D.text((380+i*373-ATFScorelen,1016),str(Score),font=config_font(36))
        D.text((295+i*373-ATFScorelen,1025),'Score',font=config_font(27),fill=(160,160,160))
        
        PointRefer = {
            "total": {
                "SS": 220,
                "S": 200,
                "A": 180
            },
            "flower": {
                "SS": 50,
                "S": 45,
                "A": 40
            },
            "wing": {
                "SS": 50,
                "S": 45,
                "A": 40
            },
            "clock": {
                "SS": 45,
                "S": 40,
                "A": 35
            },
            "cup": {
                "SS": 45,
                "S": 40,
                "A": 37
            },
            "crown": {
                "SS": 40,
                "S": 35,
                "A": 30
            }
        }
        
        if Score >= PointRefer[parts]['SS']:
            ScoreImage =Image.open(f'{cwd}/artifactGrades/SS.png')
        elif Score >= PointRefer[parts]['S']:
            ScoreImage =Image.open(f'{cwd}/artifactGrades/S.png')
        elif Score >= PointRefer[parts]['A']:
            ScoreImage =Image.open(f'{cwd}/artifactGrades/A.png')
        else:
            ScoreImage =Image.open(f'{cwd}/artifactGrades/B.png')
            
        ScoreImage = ScoreImage.resize((ScoreImage.width//11,ScoreImage.height//11))
        SCMask = ScoreImage.copy()
        
        Base.paste(ScoreImage,(85+373*i,1013),mask=SCMask)
        
    SetBounus = Counter([x for x in atftype if atftype.count(x) >= 2])
    for i,(n,q) in enumerate(SetBounus.items()):
        if len(SetBounus) == 2:
            D.text((1536,243+i*35),n,fill=(0,255,0),font=config_font(23))
            D.rounded_rectangle((1818,243+i*35,1862,266+i*35),1,'black')
            D.text((1835,243+i*35),str(q),font=config_font(19))
        if len(SetBounus) == 1:
            D.text((1536,263),n,fill=(0,255,0),font=config_font(23))
            D.rounded_rectangle((1818,263,1862,288),1,'black')
            D.text((1831,265),str(q),font=config_font(19))
            
    premium = read_json(f'{cwd}/Assets/premium.json')
    user_badge = premium.get(f'{data.get("uid")}')
    if user_badge:
        for i,b in enumerate(user_badge):
            badge = Image.open(f'{cwd}/badge/{b}.png').convert('RGBA').resize((38,38))
            badge_mask = badge.copy()
            
            Base.paste(badge,(1843-i*45,533),mask=badge_mask)
            
    Base.show()
    Base.save(f'{cwd}/Tests/Image.png')
            
        
            
        
        
        
    
    
    return pil_to_base64(Base,format='png')
        
    
    
def pil_to_base64(img, format="jpeg"):
    buffer = BytesIO()
    img.save(buffer, format)
    img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

    return img_str




generation(read_json('data.json'))