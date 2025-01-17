# Stop words
STOP_WORDS = set(
    """
'n 'r a ac achos achosi addas ag agos ai ail all allan allu am ambell amgylch aml amlwg amryw
 amrywiaeth and angen ar arall ardal arfer arnaf aros at ati awr 
 
 bach bai bant barod bawb bellach ben beth blaen ble blith bob bobl bobman bod bosib bron bryd bwysig byd bydd byddaf 
 byddai bydden byddwn bynnag byth 
 
 cadw cael cant cefnogi cei ceisio chael chdi chei chi chwarae chwe chwech chwi codi colli credu cwestiynau cyd cyfamser cyfan cyfer cymryd cyn 
 cynt cyntaf 
 
 da dal dan dangos dau daw dda ddau ddechrau ddefnyddio ddifrifol ddigon ddim ddiweddar ddod ddweud ddwy ddydd ddylai ddyle ddylen debyg dechrau defnydd defnyddio deg 
 derbyn deuddeg deugain dewis di difrifol digon digwydd digwyddiad dilyn dim dipyn disgwyl 
 diwedd diweddar diwethaf diwrnod do dod does draws dros drwy dweud dwi dwy dy dydd dylai 
 dyle dylen dyma dyna 
 
 ef efallai efo ei eich ein eisiau eisioes eisoes enwedig er eraill erbyn erioed ers eto eu 
 
 fach faint fan fath fawr fe fel felly fesul fewn ffwrdd fi fo fod fodd for fwy fwyaf fy fydd
 fyddaf fyddai fydden fynd fyny fyth 
 
 gadael gadw gael gafodd gall gallai gallu galw gan geisio gen gennych gerllaw gilydd gobeithio gorau gosod gwaelod gwag 
 gwahanol gweld gwelwch gwirioneddol gwmpas gwnaeth gwnaf gwnawn gwneud gwybod gyd gyda 
 gydag gyfan gyfer gymryd gynt gyntaf gywir 
 
 hanfodol hanner heb heddiw hefyd hi hir holl hon hun hunain hwn hwynt hyd hyn hynny hytrach 
 
 i iawn iddi iddo iddyn iddynt in is isod 
 
 lawer lawn lawr llai llawer llawn lle lleiaf lot 
 
 mae maen maent maes mai maint math mawr meddai megis methu mewn mi mod modd mor munud mwy 
 mwyaf mwyn mynd 
 
 na nad naddo nag naill naw nawr neb nesaf neu nhw ni nid nifer nis nodi nos nunlle 
 
 o ochr oddi oedd oes of ogystal oherwydd olaf on ond oni os 
 
 pa pam pan parhau pawb pedair pedwar penodol peth pethau plentyn plith plîs pob pobman popeth
 prif pryd pum pump pymtheg 
 
 rai ran rhag rhai rhaid rhain rhan rheini rheiny rhoi rhwng rhyw rhywbeth rhywbryd rhywfaint rhywle rhywsut rioed roedd 
 roeddwn roi rwy rwyf rydw rydych rydym rywfaint rywsut 
 
 saith sawl sef sicrhau siŵr siwr sut sy sydd symud 
 
 tair tan tebyg the ti tipyn to top tra tri tro tros trwy tu tua tuag 
  
 uchel uchod ugain un unig unigolyn union unlle unrhyw unwaith uwch uwchben wahanol 
 
 wahân waith wedi wedyn weithiau weithio wel well wir wirioneddol wnaeth wnaf wnes wneud wrth 
 wybod wyf wyth 
 
 y ychwanegol ychydig ydwyf ydy ydych ydym ym yma ymddangos ymddengys ymlaen ymysg yn yna yng ynglŷn yno yr ystod yw â ôl
""".split()
)

