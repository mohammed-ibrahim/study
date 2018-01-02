# -*- coding: utf-8 -*-
import collections
import json

file_name = "../static/metadata/quranic-corpus-morphology-0.4.txt"

aayaah = []
aayaah.append("start")
aayaah_mapping = []
aayaah_mapping.append("start")

aayaah_map = collections.OrderedDict()


#surah_list = [[],[0,7,5,1,"Al-Faatiha","The Opening"],[7,286,87,40,"Al-Baqara","The Cow"],[293,200,89,20,"Aal-i-Imraan","The Family of Imraan"],[493,176,92,24,"An-Nisaa","The Women"],[669,120,112,16,"Al-Maaida","The Table"],[789,165,55,20,"Al-An'aam","The Cattle"],[954,206,39,24,"Al-A'raaf","The Heights"],[1160,75,88,10,"Al-Anfaal","The Spoils of War"],[1235,129,113,16,"At-Tawba","The Repentance"],[1364,109,51,11,"Yunus","Jonas"],[1473,123,52,10,"Hud","Hud"],[1596,111,53,12,"Yusuf","Joseph"],[1707,43,96,6,"Ar-Ra'd","The Thunder"],[1750,52,72,7,"Ibrahim","Abraham"],[1802,99,54,6,"Al-Hijr","The Rock"],[1901,128,70,16,"An-Nahl","The Bee"],[2029,111,50,12,"Al-Israa","The Night Journey"],[2140,110,69,12,"Al-Kahf","The Cave"],[2250,98,44,6,"Maryam","Mary"],[2348,135,45,8,"Taa-Haa","Taa-Haa"],[2483,112,73,7,"Al-Anbiyaa","The Prophets"],[2595,78,103,10,"Al-Hajj","The Pilgrimage"],[2673,118,74,6,"Al-Muminoon","The Believers"],[2791,64,102,9,"An-Noor","The Light"],[2855,77,42,6,"Al-Furqaan","The Criterion"],[2932,227,47,11,"Ash-Shu'araa","The Poets"],[3159,93,48,7,"An-Naml","The Ant"],[3252,88,49,8,"Al-Qasas","The Stories"],[3340,69,85,7,"Al-Ankaboot","The Spider"],[3409,60,84,6,"Ar-Room","The Romans"],[3469,34,57,3,"Luqman","Luqman"],[3503,30,75,3,"As-Sajda","The Prostration"],[3533,73,90,9,"Al-Ahzaab","The Clans"],[3606,54,58,6,"Saba","Sheba"],[3660,45,43,5,"Faatir","The Originator"],[3705,83,41,5,"Yaseen","Yaseen"],[3788,182,56,5,"As-Saaffaat","Those drawn up in Ranks"],[3970,88,38,5,"Saad","The letter Saad"],[4058,75,59,8,"Az-Zumar","The Groups"],[4133,85,60,9,"Al-Ghaafir","The Forgiver"],[4218,54,61,6,"Fussilat","Explained in detail"],[4272,53,62,5,"Ash-Shura","Consultation"],[4325,89,63,7,"Az-Zukhruf","Ornaments of gold"],[4414,59,64,3,"Ad-Dukhaan","The Smoke"],[4473,37,65,4,"Al-Jaathiya","Crouching"],[4510,35,66,4,"Al-Ahqaf","The Dunes"],[4545,38,95,4,"Muhammad","Muhammad"],[4583,29,111,4,"Al-Fath","The Victory"],[4612,18,106,2,"Al-Hujuraat","The Inner Apartments"],[4630,45,34,3,"Qaaf","The letter Qaaf"],[4675,60,67,3,"Adh-Dhaariyat","The Winnowing Winds"],[4735,49,76,2,"At-Tur","The Mount"],[4784,62,23,3,"An-Najm","The Star"],[4846,55,37,3,"Al-Qamar","The Moon"],[4901,78,97,3,"Ar-Rahmaan","The Beneficent"],[4979,96,46,3,"Al-Waaqia","The Inevitable"],[5075,29,94,4,"Al-Hadid","The Iron"],[5104,22,105,3,"Al-Mujaadila","The Pleading Woman"],[5126,24,101,3,"Al-Hashr","The Exile"],[5150,13,91,2,"Al-Mumtahana","She that is to be examined"],[5163,14,109,2,"As-Saff","The Ranks"],[5177,11,110,2,"Al-Jumu'a","Friday"],[5188,11,104,2,"Al-Munaafiqoon","The Hypocrites"],[5199,18,108,2,"At-Taghaabun","Mutual Disillusion"],[5217,12,99,2,"At-Talaaq","Divorce"],[5229,12,107,2,"At-Tahrim","The Prohibition"],[5241,30,77,2,"Al-Mulk","The Sovereignty"],[5271,52,2,2,"Al-Qalam","The Pen"],[5323,52,78,2,"Al-Haaqqa","The Reality"],[5375,44,79,2,"Al-Ma'aarij","The Ascending Stairways"],[5419,28,71,2,"Nooh","Noah"],[5447,28,40,2,"Al-Jinn","The Jinn"],[5475,20,3,2,"Al-Muzzammil","The Enshrouded One"],[5495,56,4,2,"Al-Muddaththir","The Cloaked One"],[5551,40,31,2,"Al-Qiyaama","The Resurrection"],[5591,31,98,2,"Al-Insaan","Man"],[5622,50,33,2,"Al-Mursalaat","The Emissaries"],[5672,40,80,2,"An-Naba","The Announcement"],[5712,46,81,2,"An-Naazi'aat","Those who drag forth"],[5758,42,24,1,"Abasa","He frowned"],[5800,29,7,1,"At-Takwir","The Overthrowing"],[5829,19,82,1,"Al-Infitaar","The Cleaving"],[5848,36,86,1,"Al-Mutaffifin","Defrauding"],[5884,25,83,1,"Al-Inshiqaaq","The Splitting Open"],[5909,22,27,1,"Al-Burooj","The Constellations"],[5931,17,36,1,"At-Taariq","The Morning Star"],[5948,19,8,1,"Al-A'laa","The Most High"],[5967,26,68,1,"Al-Ghaashiya","The Overwhelming"],[5993,30,10,1,"Al-Fajr","The Dawn"],[6023,20,35,1,"Al-Balad","The City"],[6043,15,26,1,"Ash-Shams","The Sun"],[6058,21,9,1,"Al-Lail","The Night"],[6079,11,11,1,"Ad-Dhuhaa","The Morning Hours"],[6090,8,12,1,"Ash-Sharh","The Consolation"],[6098,8,28,1,"At-Tin","The Fig"],[6106,19,1,1,"Al-Alaq","The Clot"],[6125,5,25,1,"Al-Qadr","The Power, Fate"],[6130,8,100,1,"Al-Bayyina","The Evidence"],[6138,8,93,1,"Az-Zalzala","The Earthquake"],[6146,11,14,1,"Al-Aadiyaat","The Chargers"],[6157,11,30,1,"Al-Qaari'a","The Calamity"],[6168,8,16,1,"At-Takaathur","Competition"],[6176,3,13,1,"Al-Asr","The Declining Day, Epoch"],[6179,9,32,1,"Al-Humaza","The Traducer"],[6188,5,19,1,"Al-Fil","The Elephant"],[6193,4,29,1,"Quraish","Quraysh"],[6197,7,17,1,"Al-Maa'un","Almsgiving"],[6204,3,15,1,"Al-Kawthar","Abundance"],[6207,6,18,1,"Al-Kaafiroon","The Disbelievers"],[6213,3,114,1,"An-Nasr","Divine Support"],[6216,5,6,1,"Al-Masad","The Palm Fibre"],[6221,4,22,1,"Al-Ikhlaas","Sincerity"],[6225,5,20,1,"Al-Falaq","The Dawn"],[6230,6,21,1,"An-Naas","Mankind"]]
surah_list = [[],[0,7,5,1,u'الفاتحة',"Al-Faatiha",'The Opening','Meccan'],[7,286,87,40,u'البقرة',"Al-Baqara",'The Cow','Medinan'],[293,200,89,20,u'آل عمران',"Aal-i-Imraan",'The Family of Imraan','Medinan'],[493,176,92,24,u'النساء',"An-Nisaa",'The Women','Medinan'],[669,120,112,16,u'المائدة',"Al-Maaida",'The Table','Medinan'],[789,165,55,20,u'الأنعام',"Al-An'aam",'The Cattle','Meccan'],[954,206,39,24,u'الأعراف',"Al-A'raaf",'The Heights','Meccan'],[1160,75,88,10,u'الأنفال',"Al-Anfaal",'The Spoils of War','Medinan'],[1235,129,113,16,u'التوبة',"At-Tawba",'The Repentance','Medinan'],[1364,109,51,11,u'يونس',"Yunus",'Jonas','Meccan'],[1473,123,52,10,u'هود',"Hud",'Hud','Meccan'],[1596,111,53,12,u'يوسف',"Yusuf",'Joseph','Meccan'],[1707,43,96,6,u'الرعد',"Ar-Ra'd",'The Thunder','Medinan'],[1750,52,72,7,u'ابراهيم',"Ibrahim",'Abraham','Meccan'],[1802,99,54,6,u'الحجر',"Al-Hijr",'The Rock','Meccan'],[1901,128,70,16,u'النحل',"An-Nahl",'The Bee','Meccan'],[2029,111,50,12,u'الإسراء',"Al-Israa",'The Night Journey','Meccan'],[2140,110,69,12,u'الكهف',"Al-Kahf",'The Cave','Meccan'],[2250,98,44,6,u'مريم',"Maryam",'Mary','Meccan'],[2348,135,45,8,u'طه',"Taa-Haa",'Taa-Haa','Meccan'],[2483,112,73,7,u'الأنبياء',"Al-Anbiyaa",'The Prophets','Meccan'],[2595,78,103,10,u'الحج',"Al-Hajj",'The Pilgrimage','Medinan'],[2673,118,74,6,u'المؤمنون',"Al-Muminoon",'The Believers','Meccan'],[2791,64,102,9,u'النور',"An-Noor",'The Light','Medinan'],[2855,77,42,6,u'الفرقان',"Al-Furqaan",'The Criterion','Meccan'],[2932,227,47,11,u'الشعراء',"Ash-Shu'araa",'The Poets','Meccan'],[3159,93,48,7,u'النمل',"An-Naml",'The Ant','Meccan'],[3252,88,49,8,u'القصص',"Al-Qasas",'The Stories','Meccan'],[3340,69,85,7,u'العنكبوت',"Al-Ankaboot",'The Spider','Meccan'],[3409,60,84,6,u'الروم',"Ar-Room",'The Romans','Meccan'],[3469,34,57,3,u'لقمان',"Luqman",'Luqman','Meccan'],[3503,30,75,3,u'السجدة',"As-Sajda",'The Prostration','Meccan'],[3533,73,90,9,u'الأحزاب',"Al-Ahzaab",'The Clans','Medinan'],[3606,54,58,6,u'سبإ',"Saba",'Sheba','Meccan'],[3660,45,43,5,u'فاطر',"Faatir",'The Originator','Meccan'],[3705,83,41,5,u'يس',"Yaseen",'Yaseen','Meccan'],[3788,182,56,5,u'الصافات',"As-Saaffaat",'Those drawn up in Ranks','Meccan'],[3970,88,38,5,u'ص',"Saad",'The letter Saad','Meccan'],[4058,75,59,8,u'الزمر',"Az-Zumar",'The Groups','Meccan'],[4133,85,60,9,u'غافر',"Al-Ghaafir",'The Forgiver','Meccan'],[4218,54,61,6,u'فصلت',"Fussilat",'Explained in detail','Meccan'],[4272,53,62,5,u'الشورى',"Ash-Shura",'Consultation','Meccan'],[4325,89,63,7,u'الزخرف',"Az-Zukhruf",'Ornaments of gold','Meccan'],[4414,59,64,3,u'الدخان',"Ad-Dukhaan",'The Smoke','Meccan'],[4473,37,65,4,u'الجاثية',"Al-Jaathiya",'Crouching','Meccan'],[4510,35,66,4,u'الأحقاف',"Al-Ahqaf",'The Dunes','Meccan'],[4545,38,95,4,u'محمد',"Muhammad",'Muhammad','Medinan'],[4583,29,111,4,u'الفتح',"Al-Fath",'The Victory','Medinan'],[4612,18,106,2,u'الحجرات',"Al-Hujuraat",'The Inner Apartments','Medinan'],[4630,45,34,3,u'ق',"Qaaf",'The letter Qaaf','Meccan'],[4675,60,67,3,u'الذاريات',"Adh-Dhaariyat",'The Winnowing Winds','Meccan'],[4735,49,76,2,u'الطور',"At-Tur",'The Mount','Meccan'],[4784,62,23,3,u'النجم',"An-Najm",'The Star','Meccan'],[4846,55,37,3,u'القمر',"Al-Qamar",'The Moon','Meccan'],[4901,78,97,3,u'الرحمن',"Ar-Rahmaan",'The Beneficent','Medinan'],[4979,96,46,3,u'الواقعة',"Al-Waaqia",'The Inevitable','Meccan'],[5075,29,94,4,u'الحديد',"Al-Hadid",'The Iron','Medinan'],[5104,22,105,3,u'المجادلة',"Al-Mujaadila",'The Pleading Woman','Medinan'],[5126,24,101,3,u'الحشر',"Al-Hashr",'The Exile','Medinan'],[5150,13,91,2,u'الممتحنة',"Al-Mumtahana",'She that is to be examined','Medinan'],[5163,14,109,2,u'الصف',"As-Saff",'The Ranks','Medinan'],[5177,11,110,2,u'الجمعة',"Al-Jumu'a",'Friday','Medinan'],[5188,11,104,2,u'المنافقون',"Al-Munaafiqoon",'The Hypocrites','Medinan'],[5199,18,108,2,u'التغابن',"At-Taghaabun",'Mutual Disillusion','Medinan'],[5217,12,99,2,u'الطلاق',"At-Talaaq",'Divorce','Medinan'],[5229,12,107,2,u'التحريم',"At-Tahrim",'The Prohibition','Medinan'],[5241,30,77,2,u'الملك',"Al-Mulk",'The Sovereignty','Meccan'],[5271,52,2,2,u'القلم',"Al-Qalam",'The Pen','Meccan'],[5323,52,78,2,u'الحاقة',"Al-Haaqqa",'The Reality','Meccan'],[5375,44,79,2,u'المعارج',"Al-Ma'aarij",'The Ascending Stairways','Meccan'],[5419,28,71,2,u'نوح',"Nooh",'Noah','Meccan'],[5447,28,40,2,u'الجن',"Al-Jinn",'The Jinn','Meccan'],[5475,20,3,2,u'المزمل',"Al-Muzzammil",'The Enshrouded One','Meccan'],[5495,56,4,2,u'المدثر',"Al-Muddaththir",'The Cloaked One','Meccan'],[5551,40,31,2,u'القيامة',"Al-Qiyaama",'The Resurrection','Meccan'],[5591,31,98,2,u'الانسان',"Al-Insaan",'Man','Medinan'],[5622,50,33,2,u'المرسلات',"Al-Mursalaat",'The Emissaries','Meccan'],[5672,40,80,2,u'النبإ',"An-Naba",'The Announcement','Meccan'],[5712,46,81,2,u'النازعات',"An-Naazi'aat",'Those who drag forth','Meccan'],[5758,42,24,1,u'عبس',"Abasa",'He frowned','Meccan'],[5800,29,7,1,u'التكوير',"At-Takwir",'The Overthrowing','Meccan'],[5829,19,82,1,u'الإنفطار',"Al-Infitaar",'The Cleaving','Meccan'],[5848,36,86,1,u'المطففين',"Al-Mutaffifin",'Defrauding','Meccan'],[5884,25,83,1,u'الإنشقاق',"Al-Inshiqaaq",'The Splitting Open','Meccan'],[5909,22,27,1,u'البروج',"Al-Burooj",'The Constellations','Meccan'],[5931,17,36,1,u'الطارق',"At-Taariq",'The Morning Star','Meccan'],[5948,19,8,1,u'الأعلى',"Al-A'laa",'The Most High','Meccan'],[5967,26,68,1,u'الغاشية',"Al-Ghaashiya",'The Overwhelming','Meccan'],[5993,30,10,1,u'الفجر',"Al-Fajr",'The Dawn','Meccan'],[6023,20,35,1,u'البلد',"Al-Balad",'The City','Meccan'],[6043,15,26,1,u'الشمس',"Ash-Shams",'The Sun','Meccan'],[6058,21,9,1,u'الليل',"Al-Lail",'The Night','Meccan'],[6079,11,11,1,u'الضحى',"Ad-Dhuhaa",'The Morning Hours','Meccan'],[6090,8,12,1,u'الشرح',"Ash-Sharh",'The Consolation','Meccan'],[6098,8,28,1,u'التين',"At-Tin",'The Fig','Meccan'],[6106,19,1,1,u'العلق',"Al-Alaq",'The Clot','Meccan'],[6125,5,25,1,u'القدر',"Al-Qadr",'The Power, Fate','Meccan'],[6130,8,100,1,u'البينة',"Al-Bayyina",'The Evidence','Medinan'],[6138,8,93,1,u'الزلزلة',"Az-Zalzala",'The Earthquake','Medinan'],[6146,11,14,1,u'العاديات',"Al-Aadiyaat",'The Chargers','Meccan'],[6157,11,30,1,u'القارعة',"Al-Qaari'a",'The Calamity','Meccan'],[6168,8,16,1,u'التكاثر',"At-Takaathur",'Competition','Meccan'],[6176,3,13,1,u'العصر',"Al-Asr",'The Declining Day, Epoch','Meccan'],[6179,9,32,1,u'الهمزة',"Al-Humaza",'The Traducer','Meccan'],[6188,5,19,1,u'الفيل',"Al-Fil",'The Elephant','Meccan'],[6193,4,29,1,u'قريش',"Quraish",'Quraysh','Meccan'],[6197,7,17,1,u'الماعون',"Al-Maa'un",'Almsgiving','Meccan'],[6204,3,15,1,u'الكوثر',"Al-Kawthar",'Abundance','Meccan'],[6207,6,18,1,u'الكافرون',"Al-Kaafiroon",'The Disbelievers','Meccan'],[6213,3,114,1,u'النصر',"An-Nasr",'Divine Support','Medinan'],[6216,5,6,1,u'المسد',"Al-Masad",'The Palm Fibre','Meccan'],[6221,4,22,1,u'الإخلاص',"Al-Ikhlaas",'Sincerity','Meccan'],[6225,5,20,1,u'الفلق',"Al-Falaq",'The Dawn','Meccan'],[6230,6,21,1,u'الناس',"An-Naas",'Mankind','Meccan'],[6236,1]]
ruku_list = [[],[1,1],[2,1],[2,8],[2,21],[2,30],[2,40],[2,47],[2,60],[2,62],[2,72],[2,83],[2,87],[2,97],[2,104],[2,113],[2,122],[2,130],[2,142],[2,148],[2,153],[2,164],[2,168],[2,177],[2,183],[2,189],[2,197],[2,211],[2,217],[2,222],[2,229],[2,232],[2,236],[2,243],[2,249],[2,254],[2,258],[2,261],[2,267],[2,274],[2,282],[2,284],[3,1],[3,10],[3,21],[3,31],[3,42],[3,55],[3,64],[3,72],[3,81],[3,92],[3,102],[3,110],[3,121],[3,130],[3,144],[3,149],[3,156],[3,172],[3,181],[3,190],[4,1],[4,11],[4,15],[4,23],[4,26],[4,34],[4,43],[4,51],[4,60],[4,71],[4,77],[4,88],[4,92],[4,97],[4,101],[4,105],[4,113],[4,116],[4,127],[4,135],[4,142],[4,153],[4,163],[4,172],[5,1],[5,6],[5,12],[5,20],[5,27],[5,35],[5,44],[5,51],[5,57],[5,67],[5,78],[5,87],[5,94],[5,101],[5,109],[5,116],[6,1],[6,11],[6,21],[6,31],[6,42],[6,51],[6,56],[6,61],[6,71],[6,83],[6,91],[6,95],[6,101],[6,111],[6,122],[6,130],[6,141],[6,145],[6,151],[6,155],[7,1],[7,11],[7,26],[7,32],[7,40],[7,48],[7,54],[7,59],[7,65],[7,73],[7,85],[7,94],[7,100],[7,109],[7,127],[7,130],[7,142],[7,148],[7,152],[7,158],[7,163],[7,172],[7,182],[7,189],[8,1],[8,11],[8,20],[8,29],[8,38],[8,45],[8,49],[8,59],[8,65],[8,70],[9,1],[9,7],[9,17],[9,25],[9,30],[9,38],[9,43],[9,60],[9,67],[9,73],[9,81],[9,90],[9,100],[9,111],[9,119],[9,123],[10,1],[10,11],[10,21],[10,31],[10,41],[10,54],[10,61],[10,71],[10,83],[10,93],[10,104],[11,1],[11,9],[11,25],[11,36],[11,50],[11,61],[11,69],[11,84],[11,96],[11,110],[12,1],[12,7],[12,21],[12,30],[12,36],[12,43],[12,50],[12,58],[12,69],[12,80],[12,94],[12,105],[13,1],[13,8],[13,19],[13,27],[13,32],[13,38],[14,1],[14,7],[14,13],[14,22],[14,28],[14,35],[14,42],[15,1],[15,16],[15,26],[15,45],[15,61],[15,80],[16,1],[16,10],[16,22],[16,26],[16,35],[16,41],[16,51],[16,61],[16,66],[16,71],[16,77],[16,84],[16,90],[16,101],[16,111],[16,120],[17,1],[17,11],[17,23],[17,31],[17,41],[17,53],[17,61],[17,71],[17,78],[17,85],[17,94],[17,101],[18,1],[18,13],[18,18],[18,23],[18,32],[18,45],[18,50],[18,54],[18,60],[18,71],[18,83],[18,102],[19,1],[19,16],[19,41],[19,51],[19,66],[19,83],[20,1],[20,25],[20,55],[20,77],[20,90],[20,105],[20,116],[20,129],[21,1],[21,11],[21,30],[21,42],[21,51],[21,76],[21,94],[22,1],[22,11],[22,23],[22,26],[22,34],[22,39],[22,49],[22,58],[22,65],[22,73],[23,1],[23,23],[23,33],[23,51],[23,78],[23,93],[24,1],[24,11],[24,21],[24,27],[24,35],[24,41],[24,51],[24,58],[24,62],[25,1],[25,10],[25,21],[25,35],[25,45],[25,61],[26,1],[26,10],[26,34],[26,53],[26,70],[26,105],[26,123],[26,141],[26,160],[26,176],[26,192],[27,1],[27,15],[27,32],[27,45],[27,59],[27,67],[27,83],[28,1],[28,14],[28,22],[28,29],[28,43],[28,51],[28,61],[28,76],[29,1],[29,14],[29,23],[29,31],[29,45],[29,52],[29,64],[30,1],[30,11],[30,20],[30,28],[30,41],[30,54],[31,1],[31,12],[31,20],[32,1],[32,12],[32,23],[33,1],[33,9],[33,21],[33,28],[33,35],[33,41],[33,53],[33,59],[33,69],[34,1],[34,10],[34,22],[34,31],[34,37],[34,46],[35,1],[35,8],[35,15],[35,27],[35,38],[36,1],[36,13],[36,33],[36,51],[36,68],[37,1],[37,22],[37,75],[37,114],[37,139],[38,1],[38,15],[38,27],[38,41],[38,65],[39,1],[39,10],[39,22],[39,32],[39,42],[39,53],[39,64],[39,71],[40,1],[40,10],[40,21],[40,28],[40,38],[40,51],[40,61],[40,69],[40,79],[41,1],[41,9],[41,19],[41,26],[41,33],[41,45],[42,1],[42,10],[42,20],[42,30],[42,44],[43,1],[43,16],[43,26],[43,36],[43,46],[43,57],[43,68],[44,1],[44,30],[44,43],[45,1],[45,12],[45,22],[45,27],[46,1],[46,11],[46,21],[46,27],[47,1],[47,12],[47,20],[47,29],[48,1],[48,11],[48,18],[48,27],[49,1],[49,11],[50,1],[50,16],[50,30],[51,1],[51,24],[51,47],[52,1],[52,29],[53,1],[53,26],[53,33],[54,1],[54,23],[54,41],[55,1],[55,26],[55,46],[56,1],[56,39],[56,75],[57,1],[57,11],[57,20],[57,26],[58,1],[58,7],[58,14],[59,1],[59,11],[59,18],[60,1],[60,7],[61,1],[61,10],[62,1],[62,9],[63,1],[63,9],[64,1],[64,11],[65,1],[65,8],[66,1],[66,8],[67,1],[67,15],[68,1],[68,34],[69,1],[69,38],[70,1],[70,36],[71,1],[71,21],[72,1],[72,20],[73,1],[73,20],[74,1],[74,32],[75,1],[75,31],[76,1],[76,23],[77,1],[77,41],[78,1],[78,31],[79,1],[79,27],[80,1],[81,1],[82,1],[83,1],[84,1],[85,1],[86,1],[87,1],[88,1],[89,1],[90,1],[91,1],[92,1],[93,1],[94,1],[95,1],[96,1],[97,1],[98,1],[99,1],[100,1],[101,1],[102,1],[103,1],[104,1],[105,1],[106,1],[107,1],[108,1],[109,1],[110,1],[111,1],[112,1],[113,1],[114,1]]
surah_metadata = {}

def populateMetaMapping():

    surah = collections.OrderedDict()
    for i in range(1, 115):
        surah[str(i)] = {
            "ayah_offset": surah_list[i][0],
            "num_of_aayaah": surah_list[i][1],
            "num_of_ruku": surah_list[i][3],
            "name": surah_list[i][4],
            "english_name": surah_list[i][5],
            "english_meaning": surah_list[i][6],
            "revelation_phase": surah_list[i][7],
            "ruku": list()
        }


    for i in range(1, len(ruku_list)):
        #print(surah_list[i])
        #print(ruku_list[i])
        surah_number_str = str(ruku_list[i][0])
        surah[surah_number_str]["ruku"].append(getRukuMetaData(ruku_list[i], i, len(surah[surah_number_str]["ruku"])))

    print(json.dumps(surah, indent=4, ensure_ascii=False).encode('utf8'))

    return surah


def getRukuMetaData(ruku, ruku_index, num_of_previous_ruku):
    surah_number = ruku[0]
    ayah_number = ruku[1]
    key = str(surah_number) + ":" + str(ayah_number)
    index = aayaah_mapping.index(key)
    num_of_aayaah_in_ruku = 1
    aayaah_in_ruku = ["114:1", "114:2", "114:3", "114:4", "114:5", "114:6"]

    if (surah_number == 114):
        test = []
        test.append("1")
    else:
        aayaah_in_ruku = []
        next_key = str(ruku_list[ruku_index+1][0]) + ":" + str(ruku_list[ruku_index+1][1])
        next_index = aayaah_mapping.index(next_key)
        

        for i in range(index, next_index):
            aayaah_in_ruku.append(aayaah_mapping[i])


    return {
        "surah_number": surah_number,
        #"ayah_number": ayah_number,
        #"start_verse_number": str(surah_number) + ":" + str(ayah_number),
        "ruku_index": ruku_index,
        "ruku_number_of_surah": (num_of_previous_ruku + 1),
        "aayaah_in_ruku": aayaah_in_ruku
    }

def displayRukuMetadata():
    ruku_metadata = collections.OrderedDict()

    for key in surah_metadata:
        for ruku in surah_metadata[key]["ruku"]:
            ruku_metadata[str(ruku["ruku_index"])] = ruku

    print(json.dumps(ruku_metadata, indent=4))

def displayRukuIndex():
    ruku_map = collections.OrderedDict()
    for key in surah_metadata:
        for ruku in surah_metadata[key]["ruku"]:
            ruku_map[ruku["ruku_index"]] = {
                "surah_number": str(ruku["surah_number"]),
                "ruku_number_of_surah": str(ruku["ruku_number_of_surah"])
            }


    print(json.dumps(ruku_map, indent=4))

def getRoot(features):

    if "ROOT" in features:
        parts = features.split("|")

        for part in parts:
            if part.startswith("ROOT"):
                return part.split(":")[1]

    return None

def populateArabicContent():
    with open(file_name, 'r') as file_pointer: 
        d = collections.OrderedDict()
        ayah_root_sequence = collections.OrderedDict()
        root_statistics = collections.OrderedDict()
        line = file_pointer.readline()
        count = 0

        while line:
            count = count + 1

            if line[0] == "(":

                parts = line.split("\t")
                full_key = parts[0].replace("(", "").replace(")", "")
                bw_representation = parts[1]
                tag = parts[2]
                features = parts[3].replace("\r\n", "")

                parts_of_key = full_key.split(":")
                surah_number = parts_of_key[0];
                verse_number = parts_of_key[1];
                ayah_index = surah_number + ":" + verse_number

                if ayah_index not in d:
                    d[ayah_index] = {
                        "ayah_index": "",
                        "content": list()
                    }

                d[ayah_index]["ayah_index"] = ayah_index;
                d[ayah_index]["content"].append({
                        "bw_representation": bw_representation,
                        "tag": tag,
                        "features": features,
                        "full_key": full_key
                    })

                bw_root_text = getRoot(features);

                # Check if root information is available.
                if bw_root_text is not None:

                    if ayah_index not in ayah_root_sequence:
                        ayah_root_sequence[ayah_index] = list()

                    ayah_root_sequence[ayah_index].append(bw_root_text)

                    if bw_root_text not in root_statistics:
                        root_statistics[bw_root_text] = {
                            'cardinality': 0,
                            'appears_in_surah_number': set()
                        }

                    root_statistics[bw_root_text]['cardinality'] = root_statistics[bw_root_text]['cardinality'] + 1
                    root_statistics[bw_root_text]['appears_in_surah_number'].add(surah_number)

            line = file_pointer.readline()

        for bw_root_text in root_statistics:
            root_statistics[bw_root_text]['appears_in_surah_number'] = list(root_statistics[bw_root_text]['appears_in_surah_number'])
            root_statistics[bw_root_text]['appears_number_of_surah'] = len(root_statistics[bw_root_text]['appears_in_surah_number'])

        for key, value in d.iteritems():
            aayaah_mapping.append(key);
            aayaah.append(value);

    print(json.dumps(ayah_root_sequence, indent=4))
    print(json.dumps(root_statistics, indent=4))
    #print(json.dumps(d, indent=4))

populateArabicContent()
surah_metadata = populateMetaMapping()

displayRukuIndex()
#displayRukuMetadata()
