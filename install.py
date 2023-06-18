import paramiko
import json

lpv_version=''
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='saipv6master.swinfra.net', port=22, username='root', password='iso*help')
cmd="./install -c /root/config.json --external-access-host saipv6master.swinfra.net --nfsprov-server saipv6master.swinfra.net --nfsprov-folder /var/vols/itom/core --db-user cdfapiserveruser --db-password Control123 --db-url jdbc:postgresql://saipv6db.swinfra.net:5432/cdfapiserveruserdb --db-crt /root/postgres_353.crt --capabilities \"NfsProvisioner=true\" --skip-warning"
with open('D:/OMT_Install/install/test/details.txt','r') as f:
    data= json.load(f)

def get_list(path):
    _stdin, _stdout,_stderr=ssh_client.exec_command('cd '+path+';ls')
    for item in iter(_stdout.readline,""):
        return item

def execution(cmd):
    _stdin, _stdout,_stderr=ssh_client.exec_command(cmd)
    for item in iter(_stdout.readline,""):
        return item

  
_stdin, _stdout,_stderr =ssh_client.exec_command("cd /root/cdf_versions;ls")
for item in iter(_stdout.readline,""):
    path_omt = 'cd /root/cdf_versions/'+item.strip() +';'+cmd
    _stdin, _stdout,_stderr =ssh_client.exec_command(path_omt)
    for item in iter(_stdout.readline,""):
        print(item)
    


# _stdin, _stdout,_stderr=ssh_client.exec_command('cd /opt/cdf/charts;ls')
# for item in iter(_stdout.readline,""):
#     if item.__contains__('local-storage-provisioner'):
#         lpv_version= data['lpv']+'/'+item
#         print(lpv_version)
#         lpv='helm install lpv -n core '+lpv_version+' --set global.docker.registry=itom-docker.svsartifactory.swinfra.net:443 --set global.docker.orgName=hpeswitomsandbox'
#         _stdin, _stdout,_stderr=ssh_client.exec_command(lpv)
		
# item=get_list(data['chart'])
# # print(data['apphub_path']+'/cdfctl.sh chart upload '+data['chart']+item+' -u admin -p Control@123')
# apphub_upload=data['apphub_path']+'/cdfctl.sh -u '+data['user']+' -p '+data['password']+' chart upload '+data['chart']+item
# # print(apphub_upload)
# # _stdin, _stdout,_stderr=ssh_client.exec_command('/opt/cdf/scripts/cdfctl.sh chart upload /root/388/opsbridge-suite-chart/charts/opsbridge-suite-2.4.0+20221100.388.tgz -u admin -p Control@123')
# print(execution(apphub_upload))
ssh_client.close()