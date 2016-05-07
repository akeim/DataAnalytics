def create_master_turnstile_file(filenames, output_file):
    
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for name in filenames:
            with open(name) as open_file:
                for line in open_file.readlines():
                    master_file.write(line)
