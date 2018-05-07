# -*- coding: utf-8 -*-
import sys
import json

# def arabic_to_bw():
#     return ""

# bw_to_ar_map = {
#     "A": "ا",
#     "b": "ب",
#     "t": "ت",
#     "v": "ث",
#     "j": "ج",
#     "H": "ح",
#     "x": "خ",
#     "d": "د",
#     "*": "ذ",
#     "r": "ر",
#     "z": "ز",
#     "s": "س",
#     "$": "ش",
#     "S": "ص",
#     "D": "ض",
#     "T": "ط",
#     "Z": "ظ",
#     "E": "ع",
#     "g": "غ",
#     "f": "ف",
#     "q": "ق",
#     "k": "ك",
#     "l": "ل",
#     "m": "م",
#     "n": "ن",
#     "h": "ه",
#     "w": "و",
#     "y": "ي",
#     "p": "ة", #teh marbuta
#
#     # "a": '\u064E', # fatha
#     # "u": '\u064f', # damma
#     # "i": '\u0650', # kasra
#     # "F": '\u064B', # fathatayn
#     # "N": '\u064C', # dammatayn
#     # "K": '\u064D', # kasratayn
#     # "~": '\u0651', # shadda
#     # "o": '\u0652', # sukun
#     #
#     # "'": '\u0621', # lone hamza
#     # ">": '\u0623', # hamza on alif
#     # "<": '\u0625', # hamza below alif
#     # "&": '\u0624', # hamza on wa
#     # "}": '\u0626', # hamza on ya
#     #
#     # "|": '\u0622', # madda on alif
#     # "{": '\u0671', # alif al-wasla
#     # "`": '\u0670', # dagger alif
#     # "Y": '\u0649', # alif maqsura
#
#     " ": " "
# }


# def get_imap():
#
#     decoded_map = {}
#     for k in bw_to_ar_map:
#         # nk = k.decode("utf-8")
#         decoded_map[k] = bw_to_ar_map[k].decode("utf-8")
#         # print("%s - %s" % (k, bw_to_ar_map[k].decode("utf-8")))
#
#     imap = {}
#
#     for k in decoded_map:
#         v = bw_to_ar_map[k]
#         imap[v] = k
#
#     return imap


# ar_to_bw_map = get_imap()
#
# def bw_to_arabic(root):
#
#     result = ""
#
#     for c in root:
#         result = result + bw_to_ar_map[c]
#
#     return result.decode("utf-8")
#
#
# def arabic_to_bw(root):
#     root = root.decode("utf-8")
#
#     result = ""
#
#     for k in ar_to_bw_map:
#         print("%s - %s" % (k, ar_to_bw_map[k]))
#
#     for c in root:
#         print("Fetching %s" % c)
#         result = result + ar_to_bw_map[c]
#
#
#     return result

arabic_content =  """nwq,nwr,nws,Hzn,nwy,Ehd,nwb,Ehn,nwm,nwn,mwr,xtr,mwt,Hzb,nwA,mwj,xtm,mwh,mwl,wjl,wjh,wjf,wjd,wjb,nw$,wjs,fhm,*xr,Ezz,Ezw,Ezr,Ezl,Ezm,Ezb,slw,mSr,SbA,jyd,SbE,SbH,*Ab,Sbr,Sbw,slm,Sbb,Sbg,wdE,xff,xfy,glZ,drA,xft,dry,wdd,glm,sjr,glb,drr,HSHS,xfD,glf,wdq,drk,drj,sjn,sjl,wdy,sjd,glw,brz,TfA,brr,brq,lwH,brk,brj,brd,Tfl,lwy,mAy,ZmA,brS,lwt,dnw,lwn,dnr,Tfq,brA,qdd,nkd,nkf,qdm,nkl,EDl,qdw,nkr,nks,qdr,qds,jml,jmm,jmd,bDE,EDD,nkH,qdH,lw*,jmH,nkS,jmE,Abb,Abd,*kw,Abl,*kr,Abq,Abw,Aby,qHm,fEl,yqZ,All,yqn,Alh,Alf,Alw,Alt,Eyb,Eyl,Eyn,*yE,Eyy,zlzl,SEq,Ey$,mxr,zwj,zwl,$hd,zwd,$hb,dhq,$hw,zwr,$hr,$hq,mdn,hyl,mdd,hym,smE,wsq,smw,dsw,dsr,smr,wqb,smn,smm,smk,smd,ntq,dAb,mvl,kft,kfr,bEl,Swb,bEd,kfy,kff,Hnjr,vql,nhr,bEr,kfl,Swr,vqf,Swt,kAs,SwE,bED,kfA,kwkb,drhm,A*y,Smt,gyb,gyv,gyr,A*n,gyD,ktm,*Am,nzg,nzf,gyZ,ktb,nzl,lbs,lbv,SyH,SyS,lbb,lbd,lbn,Ass,Asr,Asw,Syf,Syd,Dgn,Syr,Dgv,Asf,Asn,tyn,tyh,bsq,bsr,bss,bsl,qyl,Swf,sAm,sAl,bsT,Tgy,qTmr,mHS,qyD,hrE,wzE,wH$,*hb,ldd,wzr,*hl,wzn,hrb,SmE,wHd,wHy,Efr,Efw,qSS,Eff,qSf,qSd,qSm,qSr,qSw,xDE,zbd,zbn,jAr,wtd,zbr,wtn,xDd,Hjr,fny,Hjz,fnd,xDr,Hjb,fnn,Hjj,nqr,kwb,kwd,frE,frD,frH,kwn,SdE,kwr,bTA,frT,kwy,frg,Sdq,Sdr,bTr,frj,frh,Sdy,Sdd,frr,Sdf,ETf,frv,frt,bTl,fry,bTn,ETl,slT,wfD,slH,gll,slx,fr$,gny,slq,wfd,sll,bT$,wfy,slk,wfr,slf,wfq,drs,slb,gnm,lqT,sjw,qwl,lqH,dmdm,dhn,dhm,lqy,gly,lqm,dhy,lqf,dhr,lqb,yAs,qwb,glq,xSf,fxr,xSm,xSS,bny,nDr,f$l,bnn,Trd,Trf,ArD,jyA,Trq,Trw,TrH,$xS,brm,Sxr,jyb,Sxx,ywm,Ark,Ewj,Ewn,Ewm,Ewl,Ewd,Ewr,Ewq,$ks,*wq,Arb,Hkm,*wd,Ew*,wEd,wEy,$jr,j*E,wEZ,xyr,Tff,TEm,TEn,xyb,xyl,xym,rkD,xyT,brH,xwD,mtE,xwy,xwr,xwn,xwl,mtn,xwf,vwy,nkb,vwr,khl,khn,nwS,khf,EDd,DwA,srb,sqy,kvb,fsH,mrd,kvr,sqm,sqf,ESw,fsd,ESr,nxr,Sgr,Sgw,sqT,ESf,fsr,ESb,nxl,ESm,Hvv,EDw,bqE,$yx,nkv,$yd,$yb,bql,jvw,jvv,bqr,jvm,$yE,$yA,bqy,Zhr,fH$,jhd,jhl,jhr,b$r,jhz,wDn,zrE,$kw,$kr,wDE,zrq,zry,$kl,$kk,xTw,xTf,xTb,ydy,hbT,xTT,xTA,hbw,tEs,qrTs,msH,msx,msw,mss,r$d,msk,Hbr,lHf,lHd,lHn,lHm,wvq,flH,l**,wvn,lHq,Evr,lHy,Evw,Hly,flq,Hlq,Hlm,Hll,fln,Hlf,gzl,kyn,kyl,dxr,kyd,dxn,dxl,SfH,gzw,Sfw,Sfr,Sfn,nyl,Sff,Sfd,lZy,snd,snn,snm,xzy,snh,snw,HbT,xzn,Edd,Edl,Eds,Edw,zny,Enkb,$Hn,$Hm,lsn,nsl,TbE,$HH,Tbq,qhr,Shr,xlE,shr,tjr,xlT,xlS,xll,xlf,xld,THw,xlw,xlq,Afl,Afk,Aff,Dll,fqd,blE,Afq,blw,bls,zEm,bld,blg,DbH,Tlq,lms,Tlb,sTw,lmm,sTr,jwE,Tll,jwz,tbE,jwr,jws,sTH,jww,lmH,vjj,TlE,mkn,jwb,TlH,jwd,jwf,srbl,SEr,wqy,wqt,wqr,SEd,nhy,wqf,wqd,HmA,qnTr,Hmy,rHq,Hmr,Hml,Hmm,rHm,rHl,Hmd,wqE,rHb,ZEn,E*b,$rT,Alm,wq*,E*r,rzq,lhm,$dd,H$r,gT$,x$y,mrH,mrD,mrA,DHk,mry,mrr,$rq,mrj,DHw,HSb,bAr,bAs,HSd,HSn,HSl,HSr,xmT,Hry,HSy,Skk,xmS,xmd,ytm,msd,xmr,xms,fqE,dyn,Er$,fqh,rTb,bSr,bSl,Eyr,fqr,Tms,x$b,Tmv,rmz,rmy,rmd,Hrd,rmn,Tmm,Tmn,rmm,x$E,Awy,Awl,TmE,Awh,rmH,Awd,Awb,Zfr,jfA,gwT,gwS,sEr,gwl,sEy,sEd,gwr,gwy,dkk,xrTm,qsTs,SlSl,Dmm,qsm,qss,wTA,Dmr,qsw,jfn,wTr,hdy,hdd,qsT,hdm,hzz,wTn,Hn*,mqt,gwv,vwb,Etq,Etw,Hnf,Hnk,Hnn,*rw,Etb,*rr,Etd,Hnv,Etl,*rE,*rA,jfw,gdq,gdr,gdw,grb,EbA,k$f,dHw,dHr,Ebd,zlf,wbr,wbq,zlm,zll,dHD,Ebv,zlq,Ebr,Ebs,k$T,wbl,lwm,kmm,kml,kmh,gvw,qnt,qnw,HTb,srE,HTm,Drr,qny,nml,Drb,hAt,mxD,qnT,xns,srf,srd,srj,srr,qnE,srq,sry,DrE,qrb,qrd,qrf,n$A,Dnn,Dnk,Ady,Add,bjs,qry,nAy,w*r,n$T,qrA,qrD,qrE,qrH,n$z,n$r,$tw,$tt,nSH,rjs,rjz,rjf,zHzH,rjm,rjl,rjj,nSb,bEvr,Avr,Avl,nSy,rjE,nSr,nSt,$TA,Esr,fSl,fSm,Esy,ESy,srdq,Esl,fsq,fSH,w$y,rbT,hwn,wAl,hwd,wAd,n*r,ftr,hwy,$fE,hwr,$fy,qsr,$fw,$fq,fty,zqm,$fh,dvr,rxw,mny,jHd,jHm,dss,wSb,mnn,wSd,lEb,zml,lEn,zmr,mnE,hyA,rDw,wsE,AHd,Hqq,wsT,brhn,Hqb,Hqf,hyj,wsm,wsl,wsn,rDE,hyt,nbz,qmr,nbt,Smm,qml,Smd,qmS,nbT,qmH,nbA,qmE,nbE,fwD,nb*,vEb,fwm,fwh,fwj,snbl,knn,fwz,fwt,fwq,fwr,jrf,hTE,jrd,rks,jrm,rkz,rkd,jrr,rkb,rkm,rkn,*b*b,jrz,jry,twb,jrE,jrH,twr,rkE,klA,klH,jdl,klf,klb,kll,jdd,Erjn,klw,kZm,jdr,$gf,ryE,$gl,*bH,ryn,Tyn,ryb,SHb,Tyb,*bb,Tyr,bkm,gSS,bkr,Akl,bky,lhb,ry$,lhw,lhv,rEy,hzA,Hrv,Hrq,Hrs,Hrr,Hrm,Hrk,Hrj,rEb,Swm,Hrf,rEd,Hrb,wrd,hzm,hzl,HrS,wrv,wrq,HrD,HZZ,wry,m$j,Erw,rwd,Err,rwg,ynE,Ery,Erf,m$y,lTf,Erb,Erm,nhj,Hwt,Erj,rwD,rwE,rwH,ErD,Enb,End,gfr,ftA,Enq,HDD,Ent,j**,gfl,Enw,ftH,rSS,ftq,byd,HDr,rSd,bEv,$r*m,ftl,ftn,sbq,sbt,j*w,sbb,sbg,gTw,sbl,kbkb,wly,zjj,sbT,wlj,SHf,sbE,zjw,sbH,wld,zjr,slsl,dfE,dfA,vxn,dfq,Sly,qly,Slw,qll,qlm,Sld,qld,tfv,qlb,Slb,stt,SlH,str,qlE,zyl,bhj,bhm,bhl,Ajr,Ajj,Ajl,bht,zyt,DhA,jsd,sHq,sHr,sHt,rhq,jsm,Thr,rhw,sHb,qbD,rhn,qbH,rhb,sHl,vny,Aty,qbr,qbs,rhT,bzg,qbl,*qn,nzE,rtl,Eqr,vqb,rtq,Eql,Eqb,Eqd,rtE,kEb,ymm,ymn,rfE,kns,rfq,rfv,rft,rfd,q*f,Ebqr,Hsb,jzA,Hsd,Hsn,Hsm,Hsr,Hss,zkw,qTT,qTE,qTr,qTf,swH,swA,swE,hDm,swT,swm,swl,H*r,wkz,swd,swg,swy,swq,swr,Emd,mlA,Emm,Eml,mlH,Emh,Emq,Emr,Emy,mlk,mll,mlq,mlw,rbb,vbr,tqn,mHn,syb,mHl,$Er,syl,syr,$El,fyl,mHw,$Eb,mHq,gsq,jbt,jbr,knd,syH,jby,vyb,knz,jbb,jbn,jbl,gsl,jbh,hjr,ldn,hjd,x*l,hjE,rgb,rgd,rgm,mhn,qwm,nDj,ljA,nDd,nDx,qwy,qwt,qws,$wr,ljj,qwE,$wy,$wb,$wk,gDD,gDb,DEf,Hbl,bgD,Hbk,xnzr,Hbb,*nb,Hbs,klm,qEd,bsm,bgl,qEr,bgt,bgy,nsk,Eln,Elm,nsb,jss,nsf,nsx,nsy,nsr,Elq,Elw,fzE,nsw,SrSr,fzz,nsA,mkw,mkv,mkr,sdr,sds,sdy,sdd,wny,zhq,zhr,Htm,zhd,fdy,lyt,SnE,lys,sxr,lyl,lyn,*En,grw,grr,grq,Snm,grf,Snw,sxT,grm,$Tn,xbT,EZm,$Tr,xbA,xbz,xbt,xbw,xbv,xbr,xbl,$TT,nEl,nEm,nEj,bvv,wSf,wSl,q$Er,wSy,nEs,nEq,mEn,qvA,$wZ,DjE,mEy,mEz,vll,Azf,Azz,Azr,bxE,vlv,trk,bxs,trb,trf,bxl,HZr,trq,Eqm,bdE,qDD,bdA,qDb,bdl,bdn,flk,E$r,bdw,E$w,bdr,srH,qDy,$bh,rdA,vbT,fAy,wsws,rdy,Ahl,rdd,rdf,vbt,rdm,vby,fAd,dEw,sgb,nmm,dEE,xnq,kyf,dwr,HTT,dwn,dwl,dwm,rfrf,Ekf,mjd,mjs,shw,qmTr,vmn,kbb,Ayd,jny,tsE,kbd,jnb,Ayy,jnf,jnd,kbr,DyE,byD,byE,vmr,jnn,kbt,nf$,Dyz,nTq,byt,Dyq,Dyr,byn,Dyf,jnH,nTf,nfE,nfH,lzm,qrn,lzb,nfd,nfl,lAlA,qrr,nfv,nfs,nfr,nfq,nfy,nfx,lff,lft,lfw,hll,hlk,lfH,hlE,lfZ,nZr,bwr,Znn,bwb,zmhr,bwl,Aml,$qw,$qq,Amn,mDg,bwA,mDy,jdv,rjw,ASr,Amd,ASl,$ml,$ms,$mt,$mx,$mz,rsl,Hdv,fTr,Hdq,Hdd,rsx,Hdb,*ll,rsw,rss,nHb,nHl,ybs,nHt,nHs,nHr,Ejl,Ejm,Ejf,Ejb,nqb,znm,Ejz,xrS,nqm,k*b,nqS,xrj,xrb,nqD,nqE,xrq,xrr,whb,whn,sfr,whj,sfn,sfl,sfk,sfh,nq*,why,jEl,rAf,fjj,zfr,rAs,sfH,fjr,sfE,fjw,zff,rAy,ngD,Aym,dbb,dbr,ksw,ksd,ksf,ksb,ksl,h$m,bHr,bHv,xdd,SfSf,xdn,tbr,tbb,xdE,nTH,gbn,h$$,gbr,shl,Avv,qtr,btr,wtr,shm,$rH,nSf,Ax*,btl,qtl,$rE,btk,Ddd,$ry,Avm,dlk,$rr,dll,$rk,dlw,$rb,$rd,Axr,Srf,Axw,vry,Srm,Srr,vrb,Srx,tlw,SrE,SrH,qfw,qfl,SrT,tll,nf*,*mm,EsEs,hmz,lgb,tHt,rbS,hmr,hms,hmm,hmn,rbH,hmd,rbE,lgw,Anf,rbw,Anm,Anv,Ans,ysr,Any,wkl,wkd,DfdE,gSb,HwT,fkh,Hwl,fkk,Hwj,wkA,Hwb,Hwz,Hwy,fkr,Hwr,$nA,mzq,mzn,mzj,zyg,zyd,Hw*,zyn,Hw$,zxrf,gmD,skt,xrdl,gmm,skr,gmz,skb,gmr,skn,Hyd,nvr,Hyf,Hyn,Hyq,Hyr,xsA,Hyv,Hyy,xsr,mhl,fyA,HyD,fyD,mhd,HyS,xsf,jlw,jls,njd,njm,njs,jld,njw,kdy,jlb,jll,kdr,kdH,$Am,$An,tmm,A$r,mTr,mTw,b*r,ETw,ndm,krr,krs,frd,ndd,krh,krm,krb,ndw,Twf,Twd,jzE,fDl,Twl,Twr,Twq,hdhd,fDw,zHf,Twy,Amm,fDD,TwE,fDH,frq,jzy,Amr,Amt,Amw,dmE,g$w,Zlm,Zll,dmg,dmr,dmw,myz,DAn,myr,myl,r*l,myd,lmz,srmd,hnA,rqq,Hfr,Hfw,rqy,rqd,rqb,rqm,Hfd,Hff,fZZ,HfZ"""


near_words = ["SD", "s$", "tT", "AE", "sv", "Ss", "wy", "z*", "qk", "DZ", "lm", "mn"]


all_roots = arabic_content.split(",")
# all_roots = [x.decode("utf-8") for x in all_roots]
all_roots.sort()

def generate_map():
    map = {}

    for word in near_words:
        for i in word:
            for j in word:

                if i != j:
                    if i not in map:
                        map[i] = []

                    if j not in map[i]:
                        map[i].append(j)

    return map


nw = generate_map()


def is_similar(a, b):
    if a in nw and b in nw[a]:
        return True

    return False


# level 1 - two consequent characters on same positions, with 3rd one a different characters
def suggest_level10(root):
    suggestions = []

    for alt_root in all_roots:
        places_matched = 0

        # for c in root:
        for pos in range(len(root)):
            if pos < len(alt_root) and root[pos] == alt_root[pos]:
                # print("%s matched %s at pos: %d places_matched: %d" % (root, alt_root, pos, places_matched))
                places_matched = places_matched + 1

        if places_matched == 2:
            # print("%s matched %s places_matched: %d" % (root, alt_root, places_matched))
            suggestions.append(alt_root)


    print("Len of suggestions: %d" % len(suggestions))
    return suggestions

def suggest_level1(root):
    suggestions = []

    for alt_root in all_roots:
        matched = False

        if len(alt_root) >= len(root) and alt_root != root:

            if root[0] == alt_root[0] and root[1] == alt_root[1] and is_similar(root[2], alt_root[2]):
                matched = True

            if root[1] == alt_root[1] and root[2] == alt_root[2] and is_similar(root[0], alt_root[0]):
                matched = True

            if root[0] == alt_root[0] and root[2] == alt_root[2] and is_similar(root[1], alt_root[1]):
                matched = True

        if matched:
            suggestions.append(alt_root)

    return suggestions

def suggest_root(root):
    # print(str(nw))
    suggestions = suggest_level1(root)
    return suggestions

def get_all_suggestions():
    content = []

    for root in all_roots:
        suggestions = suggest_root(root)
        buffer = [root]

        buffer.extend(suggestions)
        content.append(buffer)

    return content


def write_to_file(file_name, content):
    with open(file_name, "w") as file_pointer:
        file_pointer.write(content)

    print("File write complete: " + file_name)


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print("Usage: python root_suggestions.py root")
    #     sys.exit(1)
    #
    # root = sys.argv[1]
    # resp = suggest_root(root)
    #
    # for r in resp:
    #     print(r)

    suggestions = get_all_suggestions()
    write_to_file("./sim_suggestions.json", json.dumps(suggestions, indent=4, ensure_ascii=False).encode('utf8'))
    print("Completed..")
