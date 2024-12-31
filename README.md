# AWX Notification agent for Zabbix

### Description

This script is designed to receive job notifications from AWX using the webhook functionality and then send the JSON response to the Zabbix server. 

Once the data is received in Zabbix server, its parsed using a template called "5G awx". If a job is failed it will trigger a warning. Once the same job is executed again with a "successful" status, the trigger will be resolved.


### Usage

Deploy this service on a server that has access to the AWX server. 

- On AWX go to "**Notifications** > **Add** > **Webhook type**" and set the value of `Target URL` as `http://<agent-ip>:5000/awx/notifications`
- In the docker compose file, make sure the following environment variable are defined:
    - ZABBIX_SERVER
    - ZABBIX_HOST
    - ITEM_KEY

### Resources

Read the AWX notifications [documentation](https://docs.ansible.com/ansible-tower/latest/html/userguide/notifications.html#webhook) for more details