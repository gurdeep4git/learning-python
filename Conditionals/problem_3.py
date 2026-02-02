status = str('active')
temprature = int(39)

if status == 'active':
    if temprature > 35:
        print(f"Warning too hot")
    else:
        print(f"Normal temprature")    
else:
    print(f"Device is off")
