import paramiko
from time import sleep
from locaters import Locators
from baseclass import Baseclass

json_path= "D:/OMT_Install/install/test/details.txt" 

class Mytest(Baseclass):

    def baseclass_init(self):
        b=Baseclass()
        return b

    def json_init(self,base_cls_obj):
        data=base_cls_obj.load_json(json_path)
        return data

    def ssh_init(self,data_obj):
        ssh_client=paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=data_obj['external_access_host'], port=int(data_obj['port_ssh']), username=data_obj['ssh_usr'], password=data_obj['ssh_pwd'])
        return ssh_client
    
    def test_Omt(self,base_obj,ssh_obj,data_obj):
        item=base_obj.get_list(ssh_obj,data_obj['cdf_version_list'])
        path_omt = data_obj['cdf_version']+item.strip()+data_obj['cmd']
        base_obj.execution(ssh_obj,path_omt)
       

    def test_lpv_install(self,base_obj,ssh_obj,data_obj):
        item=base_obj.lpv_version(ssh_obj,data_obj['lpv_version'])
        lpv_full_cmd=data_obj['lpv_cmd']+data_obj['lpv']+'/'+item
        base_obj.execution(ssh_obj,lpv_full_cmd)


    def test_apphub_upload(self,base_obj,ssh_obj,data_obj):
        item=base_obj.get_list(ssh_obj,data_obj['chart'])
        apphub_upload=data_obj['apphub_path']+'/cdfctl.sh -u '+data_obj['user']+' -p '+data_obj['password']+' chart upload '+data_obj['chart']+item
        base_obj.execution(ssh_obj,apphub_upload)
        ssh_obj.close()
        sleep(20)


    def test_apphub_install(self,base_obj,data_obj):
        driver=base_obj.get_browser()
        base_obj.open_url(driver,data_obj['url'])
        sleep(5)
        base_obj.send_keys(driver,Locators.l_username,data_obj['user'])
        base_obj.send_keys(driver,Locators.l_pwd,data_obj['password'])
        base_obj.click(driver,Locators.l_submit)
        sleep(10)
        base_obj.click(driver,Locators.l_configure)
        base_obj.waitforele(driver,Locators.l_external_host,10)
        base_obj.send_keys(driver,Locators.l_external_host,data_obj['external_access_host'])
        base_obj.send_keys(driver,Locators.l_registry,data_obj['registry'])
        base_obj.send_keys(driver,Locators.l_orgename,data_obj['orge_name'])
        base_obj.click(driver,Locators.l_deploysize)
        base_obj.click(driver,Locators.l_k8s)

        base_obj.click(driver,Locators.l_capability)


        base_obj.click(driver,Locators.l_security)
        base_obj.send_keys(driver,Locators.l_userpwd,data_obj['password'])
        base_obj.send_keys(driver,Locators.l_confirnuserpwd,data_obj['password'])
        ele=base_obj.waitforele(driver,Locators.cert_upload,10)
        base_obj.scrolltoview(driver,ele)
        base_obj.js_browserview(driver,Locators.js_viewbrowser)
        base_obj.send_keys(driver,Locators.browser_ele,data_obj['cert_path1'])
        base_obj.send_keys(driver,Locators.browser_ele,data_obj['cert_path2'])
        base_obj.click(driver,Locators.cert_verify)


        base_obj.click(driver,Locators.database_section)
        base_obj.send_keys(driver,Locators.db_host,data_obj['postgres_server'])
        base_obj.send_keys(driver,Locators.db_port,data_obj['postgres_port'])
        base_obj.click(driver,Locators.auto_create)
        base_obj.send_keys(driver,Locators.postgres_admin,data_obj['postgres_user'])
        base_obj.send_keys(driver,Locators.postgres_admin_pwd,data_obj['postgres_pwd'])
        # base_obj.send_keys(driver,Locators.postgres_dbadmin,data_obj['postgres_user'])
        base_obj.click(driver,Locators.postgres_verify)


        base_obj.send_keys(driver,Locators.idm_pwd,data_obj['password'])
        # base_obj.send_keys(driver,Locators.idm_confirm,data_obj['password'])

        base_obj.send_keys(driver,Locators.bvd_pwd,data_obj['password'])
        # base_obj.send_keys(driver,Locators.bvd_confirm,data_obj['password'])

        base_obj.send_keys(driver,Locators.apls,data_obj['password'])
        # base_obj.send_keys(driver,Locators.apls_confirm,data_obj['password'])

        base_obj.send_keys(driver,Locators.monitoring_admin,data_obj['password'])
        # base_obj.send_keys(driver,Locators.monitoring_admin_confirm,data_obj['password'])

        base_obj.send_keys(driver,Locators.credential_mang,data_obj['password'])
        # base_obj.send_keys(driver,Locators.credential_mang_confirm,data_obj['password'])

        # base_obj.send_keys(driver,Locators.aec,data_obj['password'])
        # base_obj.send_keys(driver,Locators.aec_confirm,data_obj['password'])

        base_obj.send_keys(driver,Locators.monitoring_snf,data_obj['password'])
        # base_obj.send_keys(driver,Locators.monitoring_snf_confirm,data_obj['password'])

        # base_obj.click(driver,Locators.external_vertica)
        base_obj.send_keys(driver,Locators.vertica_host,data_obj['vertica_host'])
        base_obj.send_keys(driver,Locators.rw_pwd,data_obj['password_vertica'])
        base_obj.send_keys(driver,Locators.vertica_bd,data_obj['vertica_db'])
        base_obj.send_keys(driver,Locators.rw_pwd,data_obj['password_vertica'])
        base_obj.click(driver,Locators.rw_verify)
        base_obj.send_keys(driver,Locators.ro_pwd,data_obj['password_vertica'])
        base_obj.click(driver,Locators.ro_verify)
        base_obj.click(driver,Locators.advanced_page)
        base_obj.send_keys(driver,Locators.storage_class1,data_obj['storage_class'])
        # base_obj.send_keys(driver,Locators.storage_class2,data_obj['storage_class'])
        sleep(5)
        base_obj.click(driver,Locators.deploy)
        base_obj.waitforele(driver,Locators.show_advance,300)
        base_obj.click(driver,Locators.show_advance)
        base_obj.click(driver,Locators.deploy_now)
        base_obj.send_keys(driver,Locators.deployment_name,data_obj['deploy_name'])
        base_obj.click(driver,Locators.create_ns)
        base_obj.send_keys(driver,Locators.ns,data_obj['ns'])
        base_obj.click(driver,Locators.check_box)
        # base_obj.click(driver,Locators.final_deploy)
        sleep(30)
        base_obj.close(driver)

if __name__ == "__main__":
    a=Mytest()
    base_obj=a.baseclass_init()
    a.test_Omt(base_obj,a.ssh_init(a.json_init(base_obj)),a.json_init(base_obj))
    # a.test_lpv_install(base_obj,a.ssh_init(a.json_init(base_obj)),a.json_init(base_obj))
    # a.test_apphub_upload(base_obj,a.ssh_init(a.json_init(base_obj)),a.json_init(base_obj))
    # a.test_apphub_install(base_obj,a.json_init(base_obj))


