import zipfile
import time

folder_path=input('enter the file path: ')
zip_f=zipfile.ZipFile(folder_path)
if not zip_f:
    print("no passward protected . you can open it.")

else :
    start_time=time.time()
    result=0
    c=0
    characters=['0','1','2','3','4','5','6','7','8','9']
    print("brootforce started..")
    if result==0:
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess=str(i)+str(j)+str(k)+str(l)
                        password=guess.encode('utf8').strip()
                        c+=1
                        try:
                            with zipfile.ZipFile(folder_path,'r')as zf:
                                zf.extractall(pwd=password)
                                print('success the passward is: '+guess)
                                end_time=time.time()
                                result=1
                                break
                        except:
                            pass
                    if result==1:
                        break
                if result==1:
                    break
            if result==1:
                break
    if result==0:
        print('passward is not found')
    else:
        duration=end_time-start_time
        print('congratulation passward found after trying '+str(c)+' combinations '+str(duration)+' seconds')

                
                        




